import time
print(('-'*13) + ' Typing Test ' + ('-' *13))
sentence = "The quick brown fox jumped over the lazy dog."
start = False
while start == False:
    choice = input("To begin, press 'Y' ")
    if(choice == 'Y'):
        start = True

start = time.time()
print(sentence)
input = input("->")
count = 0
i = 0
words_in_sentence = sentence.split()
number_of_words = len(words_in_sentence)
for word in input.split():
    if i == number_of_words:
        break
    original_word = words_in_sentence[i]
    for j in range(len(word)):
        if(j == len(original_word)):
            break
        if word[j] == original_word[j]:
            count += 1
    i += 1
accuracy = (count/(len(sentence) - sentence.count(" ")))*100
print("Accuracy: " + str(round(accuracy,1)) + "%")
end = time.time()
print("Time Taken: " + str(round((end - start),1)) + "s")
wpm = (len(input.split())*60)/(end - start)
print("Words Per Minute: " + str(round(wpm,1)))

