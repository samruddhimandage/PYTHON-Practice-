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
        }],
        format="json"
    )

Answer = response.message

print("LLM response :")
print(Answer)

# convert JSON string to python Dictionary

data = json.loads(Answer)
print("Data from dictory is :",data)

print("Data form Dictionary ")
print("language :",data.get("language"))
print("type :",data.get("type"))
print("creator :",data.get("creator"))

