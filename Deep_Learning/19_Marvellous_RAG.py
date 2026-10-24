import chromadb
from sentence_transformers import SentenceTransformer, util
from ollama import chat

# Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to existing ChromaDB
client = chromadb.PersistentClient(path="./MarvellousDB")

collection = client.get_collection(name = "marvellous_knowledge")

# Accept question
query = input("Enter your question")

# generate query embedding
query_embedding = model.encode(query,convert_to_tensor=True)

# Retrive top 2 results
results = collection.query(query_embeddings = [query_embedding.tolist()], n_results = 2)

# Create context from retrived documents
documents = results["documents"][0]

context = "\n".join(documents)

print("Retrived context : ")
print(context)

# create prompt for LLM

prompt = f"""
Answer the question using only the given context.

Context: {context}

Question: {query}

If the answer is not available in context,
Say "Information not available"
"""

# Send the context and question to olllama (llama)
response = chat(
    model = "llama3.2:1b",
    messages = [
        {
            "role" : "user",
            "content" : prompt
        }
    ]
)

answer = response.message.content

print("Marvellous GENAI : RAG Answer : ")
print(answer)
