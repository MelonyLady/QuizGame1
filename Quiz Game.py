#making a quiz game
print("Welcome to the Quiz")

#checking for user participation
playing = input("Are you ready? ")
score = 0

if playing.lower() != "yes":
    quit()

# confirmation for user
print("And so it begins... ")

#questions begin
#question 1 of 5
answer = input("""1. What is the colour of a sunny sky?
 A. Orange 
 B. Blue
 C. Green
 D. Pink
 
 Answer: """)
if answer == "B":
    print("Correct, get ready for question 2")
    score += 1
elif answer == "b":
    print("Correct, get ready for question 2")
    score += 1
    #this elif is to show that you can check your user input this way, but there are better ways like in questions below
else:
    print("Incorrect. The correct answer was B")

#adding space between questions
print()
print()
print()

#question 2 of 5
answer = input("""2. What type of animal is a common house cat?
 A. Mammal
 B. Amphibian
 C. Reptile
 D. Bird

 Answer: """)
if answer.lower() == "a":
    #adding the .lower() makes the input that the user typed into all lowercase
    print("Correct, get ready for question 3")
    score += 1
else:
    print("Incorrect. The correct answer was A")

#adding space between questions
print()
print()
print()

#question 3 of 5
answer = input("""3. What is the force that acts on us to keep us on the Earth's surface?
 A. Stupidity
 B. Lack of science funding
 C. Gravity
 D. Invisible men

 Answer: """) .lower()
#adding the .lower() at the end of the string input also puts the user's input into lowercase
if answer == "c":
    print("Correct, get ready for question 4")
    score += 1
else:
    print("Incorrect. The correct answer was C")

#adding space between questions
print()
print()
print()

#question 4 of 5
answer = input("""4. Which bone below is found in the arm?
 A. Patella
 B. Phalanges
 C. Femur
 D. Radius

 Answer: """) .lower()
if answer == "d":
    print("Correct, get ready for question 5")
    score += 1
else:
    print("Incorrect. The correct answer was D")

#adding space between questions
print()
print()
print()

#question 5 of 5
answer = input("""5. What does CPU stand for?
 A. Catch Pedofiles Upselling
 B. Central Processing Unit
 C. Computer Processing Unit
 D. Creepy Pirates Unite

 Answer: """) .lower()
if answer == "b":
    print("Correct, get ready for your score")
    score += 1
else:
    print("Incorrect. The correct answer was B. Here is your score")

#adding space
print()
print()
print()
print()

print("Your score is " + str(score) + " out of 5")
print("That is " + str((score / 5) * 100) +"%")
if score >= 4:
    print("Well Done!")
else:
    print("Better luck next time!")