import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = 'distilbert/distilgpt2'

torch.set_num_threads(1)

def header(step, title):
    print('\n' + '=' * 70)
    print(f'Step {step}: {title}')
    print('=' * 70)

header(1, 'Load pretrained DistilGPT-2 tokenizer and model')
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
# Use standard eager attention for predictable classroom CPU inference.
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    attn_implementation='eager'
)

model = model.to('cpu')
with torch.no_grad():
    for parameter in model.parameters():
        parameter.data = parameter.detach().clone()

model.eval()
print('Independent CPU model weights prepared successfully', flush=True)
print('Model:', MODEL_NAME)

prompt = 'Artificial intelligence will change the way students'
header(2, 'Tokenize the prompt')
inputs = tokenizer(prompt, return_tensors='pt')
print('Prompt:', prompt)
print('Token IDs:', inputs['input_ids'][0].tolist())
print('Tokens:', tokenizer.convert_ids_to_tokens(inputs['input_ids'][0]))

header(3, 'Inspect next-token logits and probabilities')
with torch.no_grad():
    outputs = model(**inputs)
next_token_logits = outputs.logits[0, -1, :]
next_token_probs = torch.softmax(next_token_logits, dim=-1)
top_probs, top_ids = torch.topk(next_token_probs, k=5)
for rank, (token_id, probability) in enumerate(zip(top_ids, top_probs), start=1):
    print(f'{rank}. {repr(tokenizer.decode([int(token_id)]))}: {float(probability):.2%}')

header(4, 'Greedy generation')
with torch.no_grad():
    greedy_ids = model.generate(
        **inputs,
        max_new_tokens=35,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id
    )
print(tokenizer.decode(greedy_ids[0], skip_special_tokens=True))

header(5, 'Sampling with temperature and top-k')
torch.manual_seed(42)
with torch.no_grad():
    sampled_ids = model.generate(
        **inputs,
        max_new_tokens=35,
        do_sample=True,
        temperature=0.8,
        top_k=30,
        pad_token_id=tokenizer.eos_token_id
    )
print(tokenizer.decode(sampled_ids[0], skip_special_tokens=True))
