import numpy as np

def MarvellousEmbedding():

    token_ids = [1, 2, 3]

    # Each word will have 3 numerical features
    embedding_table = np.array([
        [0.0, 0.0, 0.0],  # Padding
        [0.2, 0.4, 0.1],  # i
        [0.8, 0.3, 0.5],  # love
        [0.6, 0.9, 0.7]   # programming
    ])

    print("Token IDs:", token_ids)

    # Lookup the vector for each token ID
    embeddings = embedding_table[token_ids]

    print("\nEmbedding Vectors:")
    print(embeddings)

    print("\nEmbedding Shape:", embeddings.shape)

def main():
    MarvellousEmbedding()

if __name__ == "__main__":
    main()