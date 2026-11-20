# The 8 questions are in the form of a list
questions = [
"""which is the correct file extension for Python files?
A. .pt
B. .pyt
C. .py
D. .python """,

 """How do you write a single-line comment in Python?
 A. // This is a comment
 B. /* This is a comment */
 C. # This is a comment
 D. -- This is a comment""",

"""What is the output of print(type(10.5))?
A. <class 'int'>
B. <class 'float'>
C. <class 'double'>
D. <class 'decimal'>""",

"""Which operator is used for exponentiation (power) in Python?
A. ^
B. **
C. //
D. % """,

"""Which built-in function finds the number of items in a list?
A. size()
B. count()
C. len()
D. length()""",

"""Which keyword is used to define a function in Python?
A. func
B. define
C. function
D. def""",

"""Which of these data types is mutable (can be changed after creation)?
A. Tuple
B. String
C. List
D. Integer""",

"""What is the output of print(10//3)?
A. 3.33
B. 3
C. 1
D. 3.0""",
]
# Now the corect answers to the questions acrespectively
answers = ["C","C","B","B","C","D","C","B"]
score = 0
print("WELCOME TO THE QUIZ")
for i in range(8):
    print()
    print("Questions",i+1)
    print(questions[i])
    while True:
        user = input("Your answer (A/B/C/D): ")
        user = user.strip().upper()
        if user == "A" or user == "B" or user == "C" or user == "D" :
            break
        print("Invalid! Please type only A, B, C, or D ")
    if user == answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is", answers[i])

percentage = score/8*100
print()
print("QUIZ FINISHED")
print("Your score: ", score," out of 8")
print("Percentage: ",percentage, " %")








    

