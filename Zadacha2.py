def most_common_word(sentence):
    words = sentence.split()

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common = max(word_counts, key=word_counts.get)

    return most_common


sentence = input("Введите предложение: ")
print("Самое частое слово:", most_common_word(sentence))