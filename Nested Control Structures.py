'''
Programmer:Xander Warner
Date: 10/15/19
Program: Double For Loop

This program will nest a For Loop inside of another
For Loop
'''

for i in range(3):
    print("Outer For Loop: " + str(i))
    for l in range(2):
        print("     Inner For Loop: " + str(l))
<<<<<<< HEAD
        
print("\n_____________________\n")
=======

print("\n___________________________________________\n")

'''

Programmer:Xander Warner
Date: 10/22/19
Program: Average Test Scores

This program asks for the test scores for multiple people
and reports the average test score for each portion
'''

num_people = int(input("How many people are taking the test? : "))
test_per_person = int(input("How many tests are going to be averaged? : "))

for i in range(num_people):
    name = input("Enter your name: ")
    sum = 0
    for j in range(test_per_person):
        score = int(input("   Enter your score: "))
        sum = sum + score
    average =  float(sum) / test_per_person
    print("     Average for " + name + ": " + str(round(average, 2)))
>>>>>>> AvgTestScore
