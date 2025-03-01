from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pymongo import MongoClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import GPT4AllEmbeddings


class RAG:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["runtime_db"]
        self.collection = self.db["runtime_instruct"]

        self.documents = []
        for doc in self.collection.find({}):
            self.documents.append(doc["instructions"])

        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        self.splitted_docs = self.text_splitter.create_documents(self.documents)

        self.vectorstore = Chroma(collection_name="runtime_collection", embedding_function=GPT4AllEmbeddings())

        self.vectorstore.reset_collection()
        self.vectorstore.add_documents(self.splitted_docs)

    def search_runtime_docs(self, query, top_k=3):
        results = self.vectorstore.similarity_search(query, k=top_k)
        return [doc.page_content for doc in results]


class runtimeEngine:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.2-90b-vision-preview",
            temperature=0,
            max_tokens=None,
            timeout=None
        )
        self.rag = RAG()

        # Default Mode: Shell
        self.memory = ConversationBufferMemory(memory_key="history", return_messages=True)

        search_results = self.rag.search_runtime_docs("Shell mode, program")
        retrieved_context = "\n".join(search_results)

        self.system_instruction = f"{retrieved_context}"

        # Update prompt to include history placeholder
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_instruction),
            ("assistant", "{history}"),
            ("human", "{input} Always `import os` Don't  ever give comments"),
        ])

        # Create an LLM chain with system instructions and memory
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=self.prompt,
            verbose=False
        )

    def predict(self, input):
        return self.conversation.run(input=input)


if __name__ == "__main__":
    runtime = runtimeEngine()
    query = "check my CPU temperatures"
    print(runtime.predict(input=query))
    query = "show it in a table"
    print(runtime.predict(input=query))
