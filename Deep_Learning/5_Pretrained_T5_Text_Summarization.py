import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = 'google/flan-t5-small'

def header(step, title):
    print('\n' + '=' * 70)
    print(f'Step {step}: {title}')
    print('=' * 70)

header(1, 'Load pretrained FLAN-T5 tokenizer and model')
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
model.eval()
print('Model:', MODEL_NAME)

paragraph = (
    'Transformers are neural network architectures that use attention to model relationships '
    'between tokens. Unlike recurrent neural networks, Transformer encoders can process input '
    'tokens in parallel. An encoder-decoder Transformer reads a source sequence with the encoder '
    'and generates an output sequence with the decoder. The decoder uses cross-attention to '
    'refer to the encoder output while predicting the next token.'
)
prompt = 'Summarize the following text in one sentence: ' + paragraph
header(2, 'Prepare summarization instruction')
print('Input:', paragraph)
print('Prompt:', prompt)

header(3, 'Tokenize encoder input')
inputs = tokenizer(prompt, return_tensors='pt', truncation=True, max_length=256)
print('Encoder input IDs shape:', tuple(inputs['input_ids'].shape))
print('Encoder token count:', int(inputs['attention_mask'].sum()))

header(4, 'Generate summary using pretrained encoder-decoder')
with torch.no_grad():
    generated_ids = model.generate(
        **inputs,
        max_new_tokens=50,
        num_beams=4,
        do_sample=False,
        early_stopping=True
    )
summary = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
print('Generated token IDs:', generated_ids[0].tolist())
print('Summary:', summary)
