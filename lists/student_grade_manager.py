students = ["Sara", "Lina", "Ahmad", "Omar"]
grades = [85, 72, 91, 64]

while True:

    question = int(input(
        "\nHello there!\n"
        "What are we gonna do today with this data?\n"
        "1. Show all students and grades\n"
        "2. Show average grade\n"
        "3. Show highest grade\n"
        "4. Show lowest grade\n"
        "5. Search for a student\n"
        "6. Add a new student\n"
        "7. Exit\n"
        "Choose: "
    ))

    if question == 1:
        # Show all students and grades
        for i in range(len(students)):
            print(f"{students[i]}, {grades[i]}")

    elif question == 2:
        # Calculate average
        total = 0

        for grade in grades:
            total += grade

        print(f"Average is {total / len(grades)}")

    elif question == 3:
        # Find highest grade
        highest = grades[0]

        for grade in grades:
            if grade > highest:
                highest = grade

        print(f"Highest grade is {highest}")

    elif question == 4:
        # Find lowest grade
        lowest = grades[0]

        for grade in grades:
            if grade < lowest:
                lowest = grade

        print(f"Lowest grade is {lowest}")

    elif question == 5:
        # Search for a student
        student = input("Who are you looking for? ")

        if student in students:
            position = students.index(student)
            print(f"{student}'s grade is {grades[position]}")
        else:
            print("Not Found")

    elif question == 6:
        # Add a new student
        new_student = input("Write the name of the student you want to add: ")
        students.append(new_student)

        new_grade = int(input("Write their grade: "))
        grades.append(new_grade)

        print(f"{new_student} was added with a grade of {new_grade}.")

    elif question == 7:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a number from 1 to 7.")
