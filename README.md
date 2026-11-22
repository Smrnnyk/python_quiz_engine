toREADME.md
# Explaining the problem
A quiz with 8 multiple-choice questions on python basics. The user answers with A, B, C or D then it checks each answer and gives feedback. At the end it shows the score and the percentage.
# How to run the program
Install python 3.10
Run : python Interactive Quiz Engine.py
# My approach to the problem statement
-I used two lists. One list to store the 8 questions and the other list to store the correct answers in the same order.
-I wrote each question between triple quotes """ """. Normal quotes only work on one line, but triple quotes let me write the question
and its 4 options on separate lines. This made the questions easy to read and comprehend.

-Use of loops
  * 'for' loop goes through the questions one by one
  * 'while' loop keeps asking until the user types A, B, C or D.
    
-Use of conditional statements
  * I also used an if inside the while loop to check the input. If the user inputs A, B, C or D, the loop stops using break. If not, the        program prints "Invalid" and asks the question again until A, B, C or D is typed by the user.
  * I used if and else to check the answer. If the letter typed by the user is the same as the correct answer, the program prints
    "Correct!" and adds 1 to the score. Else (if it is not the same), it prints "Wrong!" and shows the correct answer
    
-Use of Built-in Methhod
  *I used .upper() so that a small letter like c is changed to C before checking to avoid case mismatch, as the program treats a small      letter and a capital letter as two different answers. (Since Python is case sensitive)
  
At the end I find the percentage using score / 8 * 100.
# Edge Case
If the user types something wrong like E, a number or nothing, the program says "Invalid" and asks again. No marks are lost and the
program does not crash.
# My 5 test cases
1. I answered all questions correctly. I got 8 out of 8 (100%).
2. I answered all questions wrong. I got 0 out of 8 (0%).
3. I got 5 right. The result was 62.5% .
4. I typed AB as the answer. It said Invalid and asked again, because only one letter is allowed.
5. I typed " b " with spaces around it. It was accepted as B because .strip() removes the extra spaces.
# Acknowledgement of AI Assistance
I used an AI assistant as a guide while learning to build this project. I studied the code line by line, ran it, tested it with different inputs, and fixed an indentation error in my own copy. Working through it taught me how lists, loops and conditions fit together.



    
      
   
