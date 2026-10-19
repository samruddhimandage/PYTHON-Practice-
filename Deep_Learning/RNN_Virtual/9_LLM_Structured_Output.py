from ollama import chat
import json

# Prompt for LLM
prompt = """ 
        Give me the information about python programming language .
        return the result as json with these keys : 
        language 
        type
        creator
        """
# Execute LLM 

response = chat(
        model = "llama3.2:1b",
        messages =[{
            "role":"user",
            "content":prompt
        }]
    )

Answer = response.message

print("LLM response :")
print(Answer)


