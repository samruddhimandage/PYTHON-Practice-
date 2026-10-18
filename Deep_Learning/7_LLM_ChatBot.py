from ollama import chat

messages = [
    {
        "role": "system",
        "content":"You are python pogramming teacher"
    }
]

print("Marvellous Python tutor")
print("type exit to stop ")

while True:
    # Accept user input 
    print("_"*40)
    question = input("\nYou :").strip()
    
    # to stop chat bot
    if question.lower()=="exit":
        print("Thank you for using Marvellous bot")
        break
    
    if not question:
        continue
    
    messages.append(
        {
            "role":"user",
            "content":question
        }
    )
    
    response = chat(
        model ="llama3.2:1b",
        messages=messages
    )
    
    answer = response.message.content 
    
    print("\n Marvellous Ai :",answer)
    
    messages.append({
        "role":"assistant",
        "content":answer
    })