def longestWord(sentence):
    import re
    wordLength = []

    #Obtain all the words in the sentence
    regex = re.findall(r'[A-Za-z0-9\s]+', sentence)
    sentence = ''.join(regex).split()

    #Obtain the length of the words in the sentence
    for word in sentence:
        wordLength.append(len(word))

    #Obtain the longest word in the sentence
    maxIndex = wordLength.index(max(wordLength))
    return sentence[maxIndex]


