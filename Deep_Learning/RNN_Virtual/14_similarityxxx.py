from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Load Pretrained Embedding Model 
model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1 ="i dont love to play cricket",
sentence2 ="i love to play cricket",
    

embedding1= model.encode(sentence1,convert_to_tensor=True)
embedding2= model.encode(sentence2,convert_to_tensor=True)


# Calculate cosine similarity
similarity = util.cos_sim(embedding1,embedding2)

print("sentence1 :",sentence1)
print("sentence2 :",sentence2)

print("cosine similarity :")
print(similarity.item())