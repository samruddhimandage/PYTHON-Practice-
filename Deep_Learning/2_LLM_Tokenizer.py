from transformers import AutoTokenizer

#load pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

#input sentence
sentence = "python is easy programming language I love it"

#convert the sentence into tokens
tokens = tokenizer.tokenize(sentence)

token_Ids = tokenizer.encode(
                            sentence,
                            add_special_tokens = False
)

#convert token ids back to text
decoded = tokenizer.decode(token_Ids)

print("original sentence :",sentence)

print("Tokens :",tokens)

print("Token ids :",token_Ids)

print("Decoded sentence :",decoded)





