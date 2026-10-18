import torch

from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

# Pretrained Model Name 
model_name = "Distilgpt2"

# Load Tokenizer 
tokenizer = AutoTokenizer.from_pretrained(model_name)

# load pretrained language model
model = AutoModelForCausalLM.from_pretrained(model_name)

# Input Prompt
prompt = " I love"

# convert input into token ids
inputs = tokenizer(
    prompt,
    return_tensor="pt"
)

# Unable evaluation mode
model.eval()

# Performs inference withour gradient calculaation
with torch.no_grad():
    outputs = model(**inputs) 
    
# Extract logic for final input position
logits = outputs.logits[0,-1,:]

# Convert logits into probabilities 
probabilities = torch.softmax(
    logits,
    dim=-1
)

values,indices = torch.topk(
    probabilities ,
    5
)

print("Input :",prompt)

for values,index in zip(values,indices):
    token=tokenizer.decode([index.item()])
    print(repr(token),round(values.item(),4))