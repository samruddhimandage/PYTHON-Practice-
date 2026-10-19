from sentence_transformers import SentenceTransformer

# Load Pretrained Embedding Model 
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "python is a programming language ",
    "python is used fro data scienece",
    "i support indian cricket team"
    ]

embedding = model.encode(sentences)

# Display sentence embedding

for index , embedding in enumerate(embedding):
    print("_"*40)
    print("\n sentence :",sentences[index])
    
    print("Embedding :")
    print(embedding[:10])
    
    print("Total dimension :",len(embedding))