import time
import random
print(('-'*13) + ' Typing Test ' + ('-' *13))
sentences = ["The quick brown fox jumped over the lazy dog.", 
"A late 20th century trend in typing, primarily used with devices with small keyboards (such as PDAs and Smartphones), is thumbing or thumb typing. This can be accomplished using one or both thumbs. Similar to desktop keyboards and input devices, if a user overuses keys which need hard presses and/or have small and unergonomic layouts, it could cause thumb tendonitis or other repetitive strain injury.", 
"Word processors evolved dramatically once they became software programs rather than dedicated machines. They can usefully be distinguished from text editors, the category of software they evolved from.",
"The basic technique stands in contrast to hunt and peck typing in which the typist keeps his or her eyes on the source copy at all times. Touch typing also involves the use of the home row method, where typists keep their wrists up, rather than resting them on a desk or keyboard (which can cause carpal tunnel syndrome). To avoid this, typists should sit up tall, leaning slightly forward from the waist, place their feet flat on the floor in front of them with one foot slightly in front of the other, and keep their elbows close to their sides with forearms slanted slightly upward to the keyboard; fingers should be curved slightly and rest on the home row.",
"Business casual is an ambiguously defined dress code that has been adopted by many professional and white-collar workplaces in Western countries. It entails neat yet casual attire and is generally more casual than informal attire but more formal than casual or smart casual attire. Casual Fridays preceded widespread acceptance of business casual attire in many offices.",
"A teacher's professional duties may extend beyond formal teaching. Outside of the classroom teachers may accompany students on field trips, supervise study halls, help with the organization of school functions, and serve as supervisors for extracurricular activities. In some education systems, teachers may have responsibility for student discipline.",
"Two common terms used to describe a salesperson are Farmer and Hunter. The reality is that most professional salespeople have a little of both. A hunter is often associated with aggressive personalities who use aggressive sales technique. In terms of sales methodology, a hunter refers to a person whose focus is on bringing in and closing deals. This process is called sales capturing. An example is a commodity sale such as a long distance salesperson, shoe salesperson and to a degree a car salesperson. Their job is to find and convert buyers. A sales farmer is someone who creates sales demand through activities that directly influence and alter the buying process.",
"Many touch typists also use keyboard shortcuts or hotkeys when typing on a computer. This allows them to edit their document without having to take their hands off the keyboard to use a mouse. An example of a keyboard shortcut is pressing the Ctrl key plus the S key to save a document as they type, or the Ctrl key plus the Z key to undo a mistake. Many experienced typists can feel or sense when they have made an error and can hit the Backspace key and make the correction with no increase in time between keystrokes.",]
sentence = random.choice(sentences)
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

