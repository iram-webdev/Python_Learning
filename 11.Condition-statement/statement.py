# write a program for if-statement

Age=18
if Age >=18:
    print("you are eligible for vote...")


# write a program for if-else statement

Age=17
if Age>=18:
    print("you are eligible for vote...")
else:
    print("you are not eligible for vote...")

# write a program for if-elif-else statement

marks=90
if marks>=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>= 50:
    print("Grade C")

    
# write a program for nasted-if-elif-else

student_pass= True
persentage=75
entrance_score=65

if student_pass:
    if persentage>=60:
        if entrance_score>=80:
            print("Admission confiormed.")

        elif entrance_score>=50:
            print("Admission on waiting list.")
        else:
            print("Admission rejected")
    else:
        print("persentage is too low")
else:
    print("u are failed student")
