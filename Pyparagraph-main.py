print("Paragraph Analysis")
print("-------------------------------")
from collections import Counter
wordcounts = []
fname = input("Enter file name here: ")
# Paragraph_1.txt
with open(fname, 'r') as file:
    file_contents = file.read()
    sentences = file_contents.split('.')
    for sentence in sentences:
        words = sentence.split(' ')
        wordcounts.append(len(words))
    average_wordcount = sum(wordcounts)/len(wordcounts)
    
    counts = Counter([len(word.strip('?!,.')) for word in file_contents.split()])
    # {key(avg work length) : value(number of words)}
    #print(counts)
    avg = sum(counts.keys())
    

    print("Approximate Word Count: ", len(file_contents.split()))
    print("Approximate Sentence Count", file_contents.count('.'))
    print("Average Letter Count: " + str(avg))
    print("Average Sentence Length: " + str(average_wordcount))