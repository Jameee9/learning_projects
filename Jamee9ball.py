import random

name = "Rebecca"
question = input("What is your question for Jamee? \n")
answer = ""

random_number = random.randint(1,9)

if name == "":
  name = "Question: "
else:
  name = name + " asks: "

if random_number == 1:
  answer = "Yes"
elif random_number == 2:
  answer = "Maybe"
elif random_number == 3:
  answer = "We'll See"
elif random_number == 4:
  answer = "Nothing"
elif random_number == 5:
  answer = "I was not paying attention"
elif random_number == 6:
  answer = "Can you ask that again? I wasn't listening"
elif random_number == 7:
  answer = "I am busy"
elif random_number == 8:
  answer = "meh"
elif random_number == 9:
  answer = "No"
else:
  answer = "Error, Try again"

if question == "":
  print("Sorry, There is no question to answer")
else:
 print(name + question)
 print("Jamee said " + answer)
