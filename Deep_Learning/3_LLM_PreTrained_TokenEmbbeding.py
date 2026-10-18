import torch

from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

# Pretrained Model Name 
model_name = "Distilgpt2"

# Load Tokenizer 
tokenizer = AutoTokenizer.from_pretrained(model_name)

# load pretrained language model
model = AutoModelForCausalLM.from_pretrained(model_name)

# Input Sentence 
sentence = "i love ai"

# Convert text into pytorch tensor
inputs = tokenizer(
    sentence,
    return_tensors ="pt"        #pt = py torch
)

# Extract Token Id 
token_ids = inputs["input_ids"]

# Access the pre trained input embedding layer
embedding_layer = model.get_input_embeddings()

# retrive the embedding vectors
embeddings = embedding_layer(token_ids)

print("input sentence :",sentence)

print("token ids :",token_ids)

print("embedding shape :",embeddings.shape)

print("1st token embedding :",embeddings[0,0,:10])
