import string
import matplotlib.pyplot as plt


# reading text file
text = open("read.txt", encoding="utf-8").read()

# converting to lowercase
lower_case = text.lower()

# remove punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# tokenize words
tokenized_words = cleaned_text.split()

# get stopwords
stopwords = set(open("stopwords.txt", 'r').read().split('\n'))

# get pos words
positive = set(open("positive.txt", 'r').read().split('\n'))

# get pos words
negative = set(open("negative.txt", 'r').read().split('\n'))

# remove stopwords
final_words = []
for word in tokenized_words:
    if word not in stopwords:
        final_words.append(word)

# get score
POS = NEG = 0
for i in tokenized_words:
    if(i in positive):
        POS += 1
    elif(i in negative):
        NEG += 1
print(POS, NEG)

fig, ax1 = plt.subplots()
ax1.bar(['Positive', 'Negative'], [POS, NEG])
fig.autofmt_xdate()
# plt.savefig('graph.png')
plt.show()
