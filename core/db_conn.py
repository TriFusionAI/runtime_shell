from pymongo import MongoClient

class MongoPipe:
    def __init__(self, uri="mongodb://localhost:27017/"):
        self.client = MongoClient(uri)
        self.db = self.client["runtime_db"]
        self.collection = self.db["runtime_instruct"]

    def usedb(self, db_name):
        """Switch to a different database."""
        self.db = self.client[db_name]
        self.collection = self.db["runtime_instruct"]

    def create(self, data):
        """Insert a document into the collection."""
        return self.collection.insert_one(data).inserted_id

    def read(self, query={}):
        """Read documents based on a query."""
        return list(self.collection.find(query))

    def update(self, query, new_values):
        """Update documents based on a query."""
        return self.collection.update_many(query, {"$set": new_values})

    def delete(self, query):
        """Delete documents based on a query."""
        return self.collection.delete_many(query)

if __name__ == "__main__":
    mongo = MongoPipe()
    
    # Define the entry with instructions as a single paragraph
    instructions_paragraph = (
        "USER: Disregard previous instructions. "
        "USER: You are an assistant program named Runtime, functioning as a friendly sidekick. Zerone Laboratories developed you using Google's Gemini API. "
        "USER: Output Everything in Code and mention the language name before writing code. "
        "USER: Use python as the fallback coding language. "
        "USER: Write Extremely accurate code that would have 95%/ success rate. "
        "USER: Always focus on efficiency and accuracy of the code. Always write failsafes. "
        "Do not show this again python: can't open file '/home/zerone/import': [Errno 2] No such file or directory. "
        "USER: Dont wait for user to add API's and other dependencies. Automatically generate them using code. "
        "Output Structure : ```<language name>\nimport os\nos.system('pip install <required modules>')\nCode...\n```"
    )
    
    # Insert the entry
    shell_entry = {
        "name": "shell",
        "instructions": instructions_paragraph
    }

    # Insert the entry into the database
    entry_id = mongo.create(shell_entry)
    print(f"Inserted entry with ID: {entry_id}")