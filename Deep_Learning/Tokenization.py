def MarvellousTokenization():

    sentence = "I love programming"

    print("Original Sentence:", sentence)

    # Step 1: Split sentence into words
    tokens = sentence.lower().split()

    print("Tokens:", tokens)

    # Step 2: Create vocabulary
    vocabulary = {
        word: index + 1
        for index, word in enumerate(tokens)
    }

    print("Vocabulary:", vocabulary)

    # Step 3: Convert words into integer IDs
    token_ids = [vocabulary[word] for word in tokens]

    print("Token IDs:", token_ids)

def main():
    MarvellousTokenization()

if __name__ == "__main__":
    main()