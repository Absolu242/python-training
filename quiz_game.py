from tkinter.messagebox import YES


print('Welcome to my compuer quiz')

playing = input("Do you want to play ? ")
score = 0

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    YES
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%")
