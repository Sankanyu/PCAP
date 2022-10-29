question_counter = 0
correct_counter = 0

print("Hello")
print()
print("Dear")

print("I","am","not","a","compiler.")

def question_2(question, answer_a, answer_b, correct_letter):
    global question_counter, correct_counter
    question_counter +=1
    print(str(question_counter) + ": " + str(question))
    print("A: " + answer_a)
    print("B: " + answer_b)
    correct_answer = correct_letter
    input_answer = input("The correct answer is: ")
    input_answer = input_answer.lower()
    if correct_answer == input_answer:
        print("Correct")
        correct_counter += 1
        print()
    else:
        print("Incorrect, the correct answer was: " + correct_answer)
        print() 

def question_3(question, answer_a, answer_b, answer_c, correct_letter):
    global question_counter, correct_counter
    question_counter +=1
    print(str(question_counter) + ": " + str(question))
    print("A: " + answer_a)
    print("B: " + answer_b)
    print("C: " + answer_c)
    correct_answer = correct_letter
    input_answer = input("The correct answer is: ")
    input_answer = input_answer.lower()
    if correct_answer == input_answer:
        print("Correct")
        correct_counter += 1
        print()
    else:
        print("Incorrect, the correct answer was: " + correct_answer)
        print() 

def question_4(question, answer_a, answer_b, answer_c, answer_d, correct_letter):
    global question_counter, correct_counter
    question_counter +=1
    print(question_counter, ":", question)
    print("A: " + answer_a)
    print("B: " + answer_b)
    print("C: " + answer_c)
    print("D: " + answer_d)
    correct_answer = correct_letter
    input_answer = input("The correct answer is: ")
    input_answer = input_answer.lower()
    if correct_answer == input_answer:
        print("Correct")
        correct_counter += 1
        print()
    else:
        print("Incorrect, the correct answer was: " + correct_answer)
        print()

def question_5(question, answer_a, answer_b, answer_c, answer_d, answer_e, correct_letter):
    global question_counter, correct_counter
    question_counter +=1
    print(str(question_counter) + ": " + str(question))
    print("A: " + answer_a)
    print("B: " + answer_b)
    print("C: " + answer_c)
    print("D: " + answer_d)
    print("E: " + answer_e)
    correct_answer = correct_letter
    input_answer = input("The correct answer is: ")
    input_answer = input_answer.lower()
    if correct_answer == input_answer:
        print("Correct")
        correct_counter += 1
        print()
    else:
        print("Incorrect, the correct answer was: " + correct_answer)
        print() 

question_4("A complete set of commands is known as","Instruction list","Code laws","Command-line","Command list", "a")
question_4("What do you call a program which is written in a high-level programming language?","Raw code","Source code","Source file","Beta code","b")
question_4("Python name comes from which of the following?","Python Cafe","Python forest","Python snake","Monty Python's Flying Circus","d")
question_3("What arguments does print() function expect?", "Strings only", "Limited to one argument only", "All types of data offered by Python", "c")
question_5("What will be the output of the below code in Python?\n\nprint(\"hello\")\nprint()\nprint(\"dear\"))", "Hello", "Dear", "Hello\nDear", "HelloDear", "Hello Dear", "b")
question_4("The backslash (\) has a special meaning when used inside strings. What does it mean in Python code? Select all correct statements.", "The backslash is called the escape character.", "It will urge the console to start a new output line.", "It will not have any impact on the code output", "It is a kind of accouncement that the next character after the backslash has a different meaning.", "a,d")
question_4("What will be the output of the following code: \nprint(\"I like\\nPython\")", "I like \\nPython", "I like nPython", "I like Python", "I like \nPython", "d")
question_4("Select the correct output of the below code:\nprint(\"I am loving\\\\nPython.\")\nprint(\"I am loving\\\\Python.\")", "I am loving\\nPython.\nI am loving\\\\Python.", "I am loving\\nPython.\nI am loving\\Python.", "I am loving\\\nPython.\nI am loving\\\\Python", "I am loving\\\nPython.\nI am loving\\Python.", "b")
question_4("Select the correct output for the below code:\nprint(\"I love Python\")\nprint(\"'I love Python'\")\nprint(\"\"\"I love Python\"\"\")", "I love Python\n'I love Python'\nI love Python", "'I love Python'\nI love Python\nI love Python", "I love Python\nI love Python\nI love Python", "'I love Python'\nI love Python\n'I love Python'", "a")
question_4("Please find the correct output of the below code from the options given:\nprint(\"I\" , \"am\" , \"not\" , \"a\" , \"compiler.\")", "I am not a compiler.", "Iamnotacompiler.", "I,am,not,a,compiler.", "'I','am','not','a','compiler.'", "a")
question_4("Select the correct statements from the below with respect to print() function with the comma separated arguments:", "print() function invoked with more than one argument outputs them in separate lines.", "print() function invoked with more than one argument outputs them all in one line", "print() function puts a space between the output arguments by default" , "print() function with more than one argument will give error", "b,c")
question_2("An interpreter is a computer program that directly executes instructions written in a programming language, without requiring them to previously to have been compiled into a machine language program.", "True", "False", "a")
question_4("Select the correct output for the below code:\nprint(\"\")")

print("The Correct answers are " + str(correct_counter) + " of a total of " + str(question_counter) + " questions \nThis gives you a grade of " + str(correct_counter / question_counter * 10))