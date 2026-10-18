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

print("Creating small English to Marathi translation dataset.")

english_sentences = [
    "i love ai",
    "i love python",
    "we learn transformer",
    "this course is good",
    "teacher explains well",
    "students are learning",
    "machine learning is interesting",
    "deep learning is powerful",
    "i like this session",
    "this class is helpful"
]

marathi_sentences = [
    "mala ai avadte",
    "mala python avadte",
    "apan transformer shikto",
    "ha course changla aahe",
    "teacher changle samjavtat",
    "students shikat aahet",
    "machine learning interesting aahe",
    "deep learning powerful aahe",
    "mala ha session avadto",
    "ha class helpful aahe"
]

# Decoder output requires start and end tokens
target_sentences = ["start " + sentence + " end" for sentence in marathi_sentences]

for eng, mar in zip(english_sentences, target_sentences):
    print(eng, " ---> ", mar)


# ============================================================
# Step 2: Text Vectorization
# ============================================================

Marvellous_Header(2, "Tokenization and Padding")

print("Explanation: Converting English and Marathi words into token numbers.")

vocab_size = 1000
sequence_length = 8

english_vectorizer = layers.TextVectorization(
    max_tokens=vocab_size,
    output_sequence_length=sequence_length
)

marathi_vectorizer = layers.TextVectorization(
    max_tokens=vocab_size,
    output_sequence_length=sequence_length + 1
)

english_vectorizer.adapt(english_sentences)
marathi_vectorizer.adapt(target_sentences)

encoder_input_data = english_vectorizer(english_sentences)
target_token_data = marathi_vectorizer(target_sentences)

# Decoder input: start mala ai avadte
decoder_input_data = target_token_data[:, :-1]

# Decoder target: mala ai avadte end
decoder_target_data = target_token_data[:, 1:]

print("\nEnglish Vocabulary:")
for i, word in enumerate(english_vectorizer.get_vocabulary()):
    print(i, ":", word)

print("\nMarathi Vocabulary:")
for i, word in enumerate(marathi_vectorizer.get_vocabulary()):
    print(i, ":", word)

print("\nSample Encoder Input:")
print(english_sentences[0])
print(encoder_input_data[0].numpy())

print("\nSample Decoder Input:")
print(decoder_input_data[0].numpy())

print("\nSample Decoder Target:")
print(decoder_target_data[0].numpy())


# ============================================================
# Step 3: Positional Embedding Layer
# ============================================================

Marvellous_Header(3, "Token Embedding and Positional Embedding")

print("Transformer needs word meaning plus word position.")

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


# ============================================================
# Step 4: Transformer Encoder Block
# ============================================================

Marvellous_Header(4, "Transformer Encoder Block")

print("""
Encoder reads the complete English sentence.
It uses Multi-Head Self-Attention to understand relationships between words.
""")

class TransformerEncoder(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim):
        super().__init__()

        self.attention = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )

        self.ffn = tf.keras.Sequential([
            layers.Dense(ff_dim, activation="relu"),
            layers.Dense(embed_dim)
        ])

        self.layernorm1 = layers.LayerNormalization()
        self.layernorm2 = layers.LayerNormalization()

        self.dropout1 = layers.Dropout(0.1)
        self.dropout2 = layers.Dropout(0.1)

    def call(self, inputs, training=False):

        attention_output = self.attention(
            query=inputs,
            key=inputs,
            value=inputs
        )

        attention_output = self.dropout1(attention_output, training=training)

        out1 = self.layernorm1(inputs + attention_output)

        ffn_output = self.ffn(out1)

        ffn_output = self.dropout2(ffn_output, training=training)

        encoder_output = self.layernorm2(out1 + ffn_output)

        return encoder_output


# ============================================================
# Step 5: Transformer Decoder Block
# ============================================================

Marvellous_Header(5, "Transformer Decoder Block")

print("""
Decoder generates Marathi output.
It uses:
1. Masked Self-Attention
2. Encoder-Decoder Attention
3. Feed Forward Network
""")

class TransformerDecoder(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim):
        super().__init__()

        self.masked_attention = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )

        self.encoder_decoder_attention = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )

        self.ffn = tf.keras.Sequential([
            layers.Dense(ff_dim, activation="relu"),
            layers.Dense(embed_dim)
        ])

        self.layernorm1 = layers.LayerNormalization()
        self.layernorm2 = layers.LayerNormalization()
        self.layernorm3 = layers.LayerNormalization()

        self.dropout1 = layers.Dropout(0.1)
        self.dropout2 = layers.Dropout(0.1)
        self.dropout3 = layers.Dropout(0.1)

    def get_causal_attention_mask(self, inputs):
        batch_size = tf.shape(inputs)[0]
        seq_len = tf.shape(inputs)[1]

        i = tf.range(seq_len)[:, None]
        j = tf.range(seq_len)

        mask = tf.cast(i >= j, dtype="int32")
        mask = tf.reshape(mask, (1, seq_len, seq_len))

        mult = tf.concat(
            [tf.expand_dims(batch_size, -1), tf.constant([1, 1], dtype=tf.int32)],
            axis=0
        )

        return tf.tile(mask, mult)

    def call(self, decoder_inputs, encoder_outputs, training=False):

        causal_mask = self.get_causal_attention_mask(decoder_inputs)

        # 1. Masked Self-Attention
        attention_output1 = self.masked_attention(
            query=decoder_inputs,
            key=decoder_inputs,
            value=decoder_inputs,
            attention_mask=causal_mask
        )

        attention_output1 = self.dropout1(attention_output1, training=training)

        out1 = self.layernorm1(decoder_inputs + attention_output1)

        # 2. Encoder-Decoder Attention
        attention_output2 = self.encoder_decoder_attention(
            query=out1,
            key=encoder_outputs,
            value=encoder_outputs
        )

        attention_output2 = self.dropout2(attention_output2, training=training)

        out2 = self.layernorm2(out1 + attention_output2)

        # 3. Feed Forward Network
        ffn_output = self.ffn(out2)

        ffn_output = self.dropout3(ffn_output, training=training)

        decoder_output = self.layernorm3(out2 + ffn_output)

        return decoder_output


# ============================================================
# Step 6: Model Building
# ============================================================

Marvellous_Header(6, "Complete Transformer Model Building")

print("Connecting Encoder and Decoder together.")

embed_dim = 32
num_heads = 2
ff_dim = 64

encoder_inputs = layers.Input(shape=(sequence_length,), dtype=tf.int64, name="encoder_inputs")
decoder_inputs = layers.Input(shape=(sequence_length,), dtype=tf.int64, name="decoder_inputs")

encoder_embedding = TokenAndPositionEmbedding(
    sequence_length,
    vocab_size,
    embed_dim
)(encoder_inputs)

encoder_outputs = TransformerEncoder(
    embed_dim,
    num_heads,
    ff_dim
)(encoder_embedding)

decoder_embedding = TokenAndPositionEmbedding(
    sequence_length,
    vocab_size,
    embed_dim
)(decoder_inputs)

decoder_outputs = TransformerDecoder(
    embed_dim,
    num_heads,
    ff_dim
)(decoder_embedding, encoder_outputs)

decoder_outputs = layers.Dense(vocab_size, activation="softmax")(decoder_outputs)

model = tf.keras.Model(
    [encoder_inputs, decoder_inputs],
    decoder_outputs
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()


# ============================================================
# Step 7: Training
# ============================================================

Marvellous_Header(7, "Model Training")

print("""
Encoder input  : English sentence
Decoder input  : Marathi sentence starting with start token
Decoder target : Marathi sentence shifted by one word
""")

decoder_target_data = np.expand_dims(decoder_target_data, -1)

model.fit(
    [encoder_input_data, decoder_input_data],
    decoder_target_data,
    epochs=300,
    batch_size=2,
    verbose=1
)


# ============================================================
# Step 8: Reverse Vocabulary for Prediction
# ============================================================

Marvellous_Header(8, "Reverse Vocabulary Creation")

print("Creating index-to-word dictionary for Marathi output.")

marathi_vocab = marathi_vectorizer.get_vocabulary()
index_to_word = dict(enumerate(marathi_vocab))

for i in range(15):
    print(i, ":", index_to_word.get(i, ""))


# ============================================================
# Step 9: Sentence Translation Function
# ============================================================

Marvellous_Header(9, "Translation Function")

print("""
During prediction, decoder generates one word at a time.
First input is 'start'.
Then predicted word is added back to decoder input.
""")

def translate_sentence(input_sentence):
    print("\nInput Sentence:", input_sentence)

    encoder_input = english_vectorizer([input_sentence])

    decoded_sentence = "start"

    for i in range(sequence_length):

        decoder_input = marathi_vectorizer([decoded_sentence])[:, :-1]

        prediction = model.predict(
            [encoder_input, decoder_input],
            verbose=0
        )

        predicted_token_index = np.argmax(prediction[0, i, :])

        predicted_word = index_to_word.get(predicted_token_index, "")

        if predicted_word == "end" or predicted_word == "":
            break

        decoded_sentence += " " + predicted_word

    final_sentence = decoded_sentence.replace("start", "").strip()

    return final_sentence


# ============================================================
# Step 10: Final Testing
# ============================================================

Marvellous_Header(10, "Final Translation Testing")

test_sentences = [
    "i love ai",
    "i love python",
    "this course is good",
    "teacher explains well",
    "students are learning",
    "deep learning is powerful"
]

for sentence in test_sentences:
    output = translate_sentence(sentence)

    print("-" * 60)
    print("English :", sentence)
    print("Marathi :", output)