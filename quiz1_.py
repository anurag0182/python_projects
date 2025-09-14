print("Welcome to GK quiz!")

playing = input("Do you want to play? (yes/no)")
if playing != "yes":
    quit()

print("Okay! Let's play quiz:)")
answer = input("What does CPU stand for?\n")
if answer =="central processing unit":
    print("Correct answer!")
else:
    print("incorrect!")
    if answer != "central processing unit":
        quit()
answer1 = input("Who is the prime minister of India?\n")
if answer1 =="narendra modi":
    print("Correct!")
else:
    print("incorrect!")
    if answer1 != "narender modi":
        quit()
answer2 = input("What Galaxy S series models Samsung will launch in 2026?\n")
if answer2 == "galaxy S26 series":
    print("Correct!")
else:
    print("incorrect!")
    if answer2 != "galaxy S26 series":
        quit()
answer3 = input("Apple event 2025 release date?\n")
if answer3 =="9 september":
    print("Corrent!")
else:
    print("incorrect!")
    if answer3 != "9 september":
        quit()

end = print("Congratulations!!! you score 4/4")
