from ollama import chat
model ="llama3.2:1b"

prompts=[
    "explain recursion",
    "explain recursion in python in  3 simple points",
    """  
    you are a python programming teacher.
    expalin recurssion for beginners.
    give one simple example of recursion .
    """,
    """  
    convert programming languages to upper case.
    example 1 :
    input : python
    output : PYTHON
    
    example 2 :
    input : java
    output : JAVA
    
    input: javascript
    output :
    """
]

# Execute the prompt and get the response
for index , prompt in enumerate(prompts,start=1):
    print("_"*40)
    print(f"Prompt {index} : input prompt {prompt}")

    response = chat(
        model = model,
        messages =[{
            "role":"user",
            "content":prompt
        }]
    )
    
    print("\n Response from llm is :")
    print(response.message.content)