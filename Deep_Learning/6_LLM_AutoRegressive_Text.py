from transformers import pipeline

# load pretrained text generation pipeline
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

# Input prompt
prompt = "Artifical intelligence is"

# Generate Text
result = generator(
    prompt,
    max_new_tokens = 30,
    do_sample = False,
    pad_token_ids=generator.tokenizer.eos_token_id
)

print("generated text :")
print(result[0]["generated_text"])
