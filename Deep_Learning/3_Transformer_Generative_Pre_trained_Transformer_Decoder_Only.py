import tensorflow as tf
from tensorflow.keras import layers
import numpy as np

# ------------------------------------------------------------
# Utility Header
# ------------------------------------------------------------

def Marvellous_Header(step, title):
    print("\n" + "=" * 75)
    print(f"Step {step}: {title}")
    print("=" * 75)


# ============================================================
# Step 1: Dataset Creation
# ============================================================

Marvellous_Header(1, "Dataset Creation")

print("Creating simple text data for next-word prediction.")

sentences = [
    "i love artificial intelligence",
    "i love machine learning",
    "i love deep learning",
    "machine learning is powerful",
    "deep learning is amazing",
    "artificial intelligence is future",
    "transformer is powerful model",
    "decoder transformer generates text",
    "gpt is decoder only transformer",
    "students learn artificial intelligence",
    "students learn python programming",
    "python is useful language",
    "ai helps students learn",
    "transformer learns word relations",
    "masked attention prevents future words",
    "language model predicts next word",
    "gpt predicts next token",
    "decoder only model generates output",
    "self attention understands context",
    "positional encoding gives word order"
]

for sentence in sentences:
    print(sentence)


# ============================================================
# Step 2: Text Vectorization
# ============================================================

Marvellous_Header(2, "Tokenization and Padding")

print("Converting words into token numbers.")

vocab_size = 1000
sequence_length = 6

vectorizer = layers.TextVectorization(
    max_tokens=vocab_size,
    output_sequence_length=sequence_length + 1
)

vectorizer.adapt(sentences)

tokenized_data = vectorizer(sentences)

vocabulary = vectorizer.get_vocabulary()

print("\nVocabulary:")
for index, word in enumerate(vocabulary):
    print(index, ":", word)

print("\nTokenized Sentences:")
for sentence, tokens in zip(sentences[:5], tokenized_data.numpy()[:5]):
    print(sentence)
    print(tokens)
    print("-" * 50)


# ============================================================
# Step 3: Prepare Input and Target
# ============================================================

Marvellous_Header(3, "Input and Target Preparation")

print("""
For Decoder-only Transformer, model learns next-word prediction.

Input  : previous words
Target : next words
""")

x_data = tokenized_data[:, :-1]
y_data = tokenized_data[:, 1:]

print("\nSample Sentence:")
print(sentences[0])

print("\nInput Tokens:")
print(x_data[0].numpy())

print("\nTarget Tokens:")
print(y_data[0].numpy())

print("""
Example:
If sentence is: i love artificial intelligence

Input sequence  : i love artificial
Target sequence : love artificial intelligence
""")


# ============================================================
# Step 4: Token and Positional Embedding
# ============================================================

Marvellous_Header(4, "Token Embedding and Positional Embedding")

print("""
Token Embedding gives meaning to words.
Positional Embedding gives word order information.
""")

class TokenAndPositionEmbedding(layers.Layer):
    def __init__(self, max_len, vocab_size, embed_dim):
        super().__init__()

        self.token_embedding = layers.Embedding(
            input_dim=vocab_size,
            output_dim=embed_dim
        )

        self.position_embedding = layers.Embedding(
            input_dim=max_len,
            output_dim=embed_dim
        )

    def call(self, x):
        length = tf.shape(x)[-1]

        positions = tf.range(start=0, limit=length, delta=1)

        token_embeddings = self.token_embedding(x)
        position_embeddings = self.position_embedding(positions)

        return token_embeddings + position_embeddings


# Demonstration of embedding output
embed_dim = 32

sample_embedding_layer = TokenAndPositionEmbedding(
    sequence_length,
    vocab_size,
    embed_dim
)

sample_embedding_output = sample_embedding_layer(x_data[:1])

print("\nSample Input Tokens:")
print(x_data[:1].numpy())

print("\nEmbedding Output Shape:")
print(sample_embedding_output.shape)

print("\nSample Embedding Vector of First Word:")
print(sample_embedding_output[0][0].numpy())


# ============================================================
# Step 5: Decoder-Only Transformer Block
# ============================================================

Marvellous_Header(5, "Decoder-Only Transformer Block")

print("""
This block uses Masked Self-Attention.

Masked Self-Attention means:
Current word can see only previous words.
It cannot see future words.
""")

class DecoderOnlyTransformerBlock(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim):
        super().__init__()

        self.masked_attention = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )

        self.feed_forward = tf.keras.Sequential([
            layers.Dense(ff_dim, activation="relu"),
            layers.Dense(embed_dim)
        ])

        self.layernorm1 = layers.LayerNormalization()
        self.layernorm2 = layers.LayerNormalization()

        self.dropout1 = layers.Dropout(0.1)
        self.dropout2 = layers.Dropout(0.1)

    def get_causal_attention_mask(self, inputs):
        batch_size = tf.shape(inputs)[0]
        seq_len = tf.shape(inputs)[1]

        i = tf.range(seq_len)[:, None]
        j = tf.range(seq_len)

        mask = tf.cast(i >= j, dtype="int32")
        mask = tf.reshape(mask, (1, seq_len, seq_len))

        mult = tf.concat(
            [tf.expand_dims(batch_size, -1),
             tf.constant([1, 1], dtype=tf.int32)],
            axis=0
        )

        return tf.tile(mask, mult)

    def call(self, inputs, training=False):
        causal_mask = self.get_causal_attention_mask(inputs)

        attention_output = self.masked_attention(
            query=inputs,
            key=inputs,
            value=inputs,
            attention_mask=causal_mask
        )

        attention_output = self.dropout1(attention_output, training=training)

        out1 = self.layernorm1(inputs + attention_output)

        ffn_output = self.feed_forward(out1)

        ffn_output = self.dropout2(ffn_output, training=training)

        return self.layernorm2(out1 + ffn_output)


# ============================================================
# Step 6: Demonstrate Mask Matrix
# ============================================================

Marvellous_Header(6, "Causal Mask Demonstration")

print("This mask prevents model from seeing future words.")

dummy_block = DecoderOnlyTransformerBlock(
    embed_dim=32,
    num_heads=2,
    ff_dim=64
)

dummy_input = tf.random.normal((1, sequence_length, embed_dim))

mask = dummy_block.get_causal_attention_mask(dummy_input)

print("\nCausal Mask:")
print(mask[0].numpy())

print("""
In this matrix:
1 means visible
0 means hidden

For example:
Word at position 0 can see only position 0.
Word at position 1 can see position 0 and 1.
Word at position 2 can see position 0, 1 and 2.
""")


# ============================================================
# Step 7: Model Building
# ============================================================

Marvellous_Header(7, "Model Building")

print("""
Building Mini GPT using:
1. Token + Positional Embedding
2. Decoder-only Transformer Block
3. Dense layer with Softmax
""")

num_heads = 2
ff_dim = 64

inputs = layers.Input(shape=(sequence_length,), dtype=tf.int64)

x = TokenAndPositionEmbedding(
    sequence_length,
    vocab_size,
    embed_dim
)(inputs)

x = DecoderOnlyTransformerBlock(
    embed_dim,
    num_heads,
    ff_dim
)(x)

x = DecoderOnlyTransformerBlock(
    embed_dim,
    num_heads,
    ff_dim
)(x)

outputs = layers.Dense(vocab_size, activation="softmax")(x)

model = tf.keras.Model(inputs, outputs)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()


# ============================================================
# Step 8: Model Training
# ============================================================

Marvellous_Header(8, "Model Training")

print("""
Model learns to predict next word at every position.
""")

y_data = np.expand_dims(y_data, -1)

history = model.fit(
    x_data,
    y_data,
    epochs=300,
    batch_size=2,
    verbose=1
)


# ============================================================
# Step 9: Reverse Vocabulary
# ============================================================

Marvellous_Header(9, "Reverse Vocabulary Creation")

print("Creating index-to-word dictionary for prediction.")

index_to_word = dict(enumerate(vocabulary))
word_to_index = {word: index for index, word in enumerate(vocabulary)}

for i in range(min(25, len(vocabulary))):
    print(i, ":", index_to_word[i])


# ============================================================
# Step 10: Next Word Prediction Function
# ============================================================

Marvellous_Header(10, "Next Word Prediction Function")

print("""
Given a partial sentence, model predicts the next word.
""")

def predict_next_word(input_text):
    tokenized_input = vectorizer([input_text])[:, :-1]

    prediction = model.predict(tokenized_input, verbose=0)

    input_words = input_text.split()
    position = len(input_words) - 1

    if position < 0:
        position = 0

    if position >= sequence_length:
        position = sequence_length - 1

    predicted_token_index = np.argmax(prediction[0, position, :])

    predicted_word = index_to_word.get(predicted_token_index, "")

    return predicted_word


test_inputs = [
    "i love",
    "machine learning is",
    "deep learning is",
    "gpt is",
    "language model predicts",
    "masked attention prevents"
]

for text in test_inputs:
    predicted_word = predict_next_word(text)

    print("-" * 60)
    print("Input Text      :", text)
    print("Predicted Word  :", predicted_word)


# ============================================================
# Step 11: Text Generation Function
# ============================================================

Marvellous_Header(11, "Autoregressive Text Generation")

print("""
The model predicts one word.
Then that word is added to input.
Then next word is predicted.
This is called autoregressive generation.
""")

def generate_text(start_text, number_of_words=5):
    generated_text = start_text

    for i in range(number_of_words):
        next_word = predict_next_word(generated_text)

        if next_word == "" or next_word == "[UNK]":
            break

        generated_text = generated_text + " " + next_word

    return generated_text


generation_inputs = [
    "i love",
    "machine learning",
    "decoder transformer",
    "gpt",
    "students learn"
]

for text in generation_inputs:
    output = generate_text(text, number_of_words=4)

    print("-" * 60)
    print("Start Text     :", text)
    print("Generated Text :", output)
    