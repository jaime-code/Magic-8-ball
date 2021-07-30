# this imports the random module that will allow us to generate a random number from a range when using .radint() function from the random module
import random

# person asking the question
name = "Zuku"

# a Yes/No question is asked
question = "Can lighting hit the same spot twice?"

# answer to question
answer = ""

# variable to store randomly generated value between 1-12.
random_number = random.randint(1, 12)
#print(random_number)

# answer is the possible 1 -  options that the 8-Ball can reply with
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer ="It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "What were you asking again?"
elif random_number == 11:
  answer = "You may not like like it?"
elif random_number == 12:
  answer = "Try again"
else:
  answer = "Error"

# Person asks their question, added an if statemen if the name is not provided the question will still print in a good format.
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

# 8-Ball response, added an if statement in the event their is no question asked
if question == "":
  print("The Magic 8-Ball is not able to provide you an answer without asking a question first")
else:
  print("Magic 8-Ball's answer: " + answer)