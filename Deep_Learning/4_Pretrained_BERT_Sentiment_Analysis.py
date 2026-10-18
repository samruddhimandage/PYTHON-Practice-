import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = 'distilbert-base-uncased-finetuned-sst-2-english'

def header(step, title):
    print('\n' + '=' * 70)
    print(f'Step {step}: {title}')
    print('=' * 70)

header(1, 'Load pretrained tokenizer and sentiment model')
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()
print('Model:', MODEL_NAME)
print('Classes:', model.config.id2label)

sentences = [
    'This course is excellent and easy to understand.',
    'The session was confusing and boring.',
    'I really enjoyed learning about transformers.',
    'I did not like this lecture.'
]
header(2, 'Tokenize sample sentences')
inputs = tokenizer(sentences, return_tensors='pt', padding=True, truncation=True)
print('Token IDs shape:', tuple(inputs['input_ids'].shape))
print('First sentence tokens:', tokenizer.convert_ids_to_tokens(inputs['input_ids'][0]))

header(3, 'Run pretrained inference (no model.fit)')
with torch.no_grad():
    outputs = model(**inputs)
logits = outputs.logits
probabilities = torch.softmax(logits, dim=-1)
print('Logits shape:', tuple(logits.shape))

header(4, 'Interpret predicted labels and confidence')
for sentence, raw_logits, probs in zip(sentences, logits, probabilities):
    predicted_id = int(torch.argmax(probs))
    label = model.config.id2label[predicted_id]
    confidence = float(probs[predicted_id])
    print('\nSentence:', sentence)
    print('Logits:', [round(float(x), 4) for x in raw_logits])
    print('Prediction:', label)
    print('Confidence:', f'{confidence:.2%}')

header(5, 'Summary')
