import numpy as np

def MarvellousSelfAttention():

    words = ["i", "love", "programming"]

    # Input embeddings
    X = np.array([
        [0.2, 0.4, 0.1],
        [0.8, 0.3, 0.5],
        [0.6, 0.9, 0.7]
    ])

    print("Input Embeddings:")
    print(X)

    # Step 1: Create Query, Key and Value
    # Simplification: Q, K and V are equal to X
    Q = X
    K = X
    V = X

    # Step 2: Calculate attention scores
    scores = np.dot(Q, K.T)

    # Step 3: Scale scores
    d_k = K.shape[1]
    scores = scores / np.sqrt(d_k)

    # Step 4: Apply softmax
    exp_scores = np.exp(
        scores - np.max(scores, axis=1, keepdims=True)
    )

    attention_weights = exp_scores / np.sum(
        exp_scores, axis=1, keepdims=True
    )

    # Step 5: Calculate contextual representations
    output = np.dot(attention_weights, V)

    print("\nAttention Weights:")
    print(np.round(attention_weights, 3))

    print("\nContextual Representations:")
    print(np.round(output, 3))

    print("\nAttention for word:", words[1])

    for word, weight in zip(words, attention_weights[1]):
        print(word, ":", round(weight, 3))

def main():
    MarvellousSelfAttention()

if __name__ == "__main__":
    main()