reference_words = set()
print("reading the reference dictionary...!!!")
with open('IITB.en-hi.hi', 'r', encoding='utf-8') as ref_file:
    for line in ref_file:
        reference_words.update(line.split())

print("reading the corpus....!!!")
with open('covid_19_corpus.txt','r', encoding='utf-8') as corpus_file:
    corpus_words = corpus_file.read().split()

print("applying the filtering...!!!")
filtered_words = [word for word in corpus_words if word not in reference_words]

print("Saving the filtered words...!!!")
with open('filtered_corpus.txt','w', encoding='utf-8') as filtered_file:
    filtered_file.write('\n'.join(filtered_words))