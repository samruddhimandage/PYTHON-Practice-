from sentence_transformers import SentenceTransformer, util

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

# Find top 2 matching documents
top_result = scores.topk(2)

print("Top 2 relevent documents")

for index in top_result.indices:
    print(documents[index.item()])