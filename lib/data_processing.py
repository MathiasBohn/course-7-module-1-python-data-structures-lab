# This module contains functions to process student data.

def format_student_data(student):
  
    student_id = student[0]
    student_name = student[1]
    student_major = student[2]

    # Use an f-string to format the information clearly
    return f"ID: {student_id} | Name: {student_name} | Major: {student_major}"


def display_students(student_list):

    # Loop through every student in the list
    for student in student_list:
        # Call format_student_data to get formatted string
        formatted_student = format_student_data(student)

        # Print formatted string
        print(formatted_student)