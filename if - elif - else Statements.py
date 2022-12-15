
# Part 1


def main():

    message = say_you_say_me('Daniel', 'Tom')

    print("")

    message = goto_bed(7.5)
    print(message)
    message = goto_bed(3.5)
    print(message)
    print("")
    get_student_grades()

    

def say_you_say_me(you, me):
    """Displays a simple message regarding the names you and me."""
    length_you = len(you)
    length_me = len(me)
    total_length = length_you + length_me
    print("You:",you)
    print("Me:",me)
    print("Length of our names combined is:", total_length)

    if (length_you < length_me):
        print(you, "has the shorter name by", length_me - length_you, "character(s).")
    elif (length_me < length_you):
        print(me, "has the shorter name by", length_you - length_me, "character(s).")
    else: 
        print("Both names are the same length.")


# Part 2

def goto_bed(hours_slept):
    """Displays a message regarding the number of hours needed to sleep.""" 
    hours_slept = float(hours_slept)
    if (hours_slept <= 5.5):
        return ("You need to go to bed before 10p.")

    else: (hours_slept >= 5.5)
    return ("You can stay up past midnight.")


# Part 3

def determine_letter_grade(score):
    """Determines the letter grade of a student using multi-branch if statements"""
    
    grade = "Not assigned"
    
    if (score >= 90):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    else:
        grade = "F"
    
    return(grade)


def get_student_grades():
    """Displays the score and letter grade of a student"""
    num_grades = input("Enter number of student grades to enter: ")
    print("")
    num_grades = int(num_grades)
    for i in range (0,num_grades):
        print("Enter student "+str(i+1)+"'s score: ",end="")
        score = int(input())
        print("Student "+str(i+1)+"'s letter grade is: "+determine_letter_grade(score))
        print("")


    

main()
