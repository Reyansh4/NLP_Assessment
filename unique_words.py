from collections import Counter

with open('filtered_corpus.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()

word_counts = Counter(words)

unique_words_with_counts = dict(word_counts)

# for word, count in unique_words_with_counts.items():
#     print(f"{word}: {count}")

with open('unique_words_with_counts.txt', 'w', encoding='utf-8') as output_file:
    for word, count in unique_words_with_counts.items():
        output_file.write(f"{word}: {count}\n")
