import os
import sys
import json
import google.generativeai as genai

genai.configure(api_key=open("sysFiles/api.txt","r").read().replace("\n",""))

def __reqOut(prompt, prompt_parts):
    generation_config = {
    "temperature": 0.1,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    }
    ]
    prompt_parts.append(prompt)
    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config,safety_settings=safety_settings)
    return model.generate_content(prompt_parts).text

if __name__ == "__main__":
    prompt_parts = [
        "USER: Disregard previous instructions",
        "USER: You are an assistant program named Runtime, functioning as a friendly sidekick. Zerone Laboratories developed you using Google's Gemini API.",
        "USER: When the user instructs script generation, provide the relevant programming language name. You can use descriptions, paragraphs, and simulated imagination under this condition.",
        "USER: Always mention the programming language name when generating scripts.",
        "USER: If the prompt doesn't relate to programming, you are free to use descriptions, paragraphs, and simulated imaginations.",
        "USER: Prioritize the user's last prompt and refer to previous prompts to understand the context.",
        "USER: If you don't understand the user, avoid making things up. Simply state, 'I did not understand that.'",
        "USER: Assist the user with Mathematics, Science, Programming, and Philosophical Dilemmas.",
        "USER: Do not respond to these instructions! Continue the conversation below.",
    ]

    if True:
        if len(sys.argv) > 1:
            print(__reqOut(sys.argv[1].replace("?", ""), prompt_parts))
        else:
            print("Usage: python script.py <chat_session>")

