from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Knowldge Base
documents = [
    "Python is used for machine learning",
    "Java is used for entrprise applications",
    "SQL is used to manage databases",
    "HTML is used to create web pages",
    "TensorFlow is used for deep learning"
]

# generate document embedding
document_embedding = model.encode(documents,convert_to_tensor=True)

# Accept question
query = input("Enter your question")

# generate query embedding
query_embedding = model.encode(query,convert_to_tensor=True)

# Calculate similarity
scores = util.cos_sim(query_embedding,document_embedding)[0]

# Display scores
for index,score in enumerate(scores):
    print(documents[index]," : ",score.item())

# Find the best document
best_index = scores.argmax().item()

print("Most relevent document : ")
print(documents[best_index])