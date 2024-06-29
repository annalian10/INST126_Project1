#1.1 Write a program to get user input on students, courses, assignments, 
# and grades and put these data into lists

#students table functions
st_template = ["last_name", "first_name", "student_id", "email", "accomodation", "notes"]
instudent = []
for item in st_template:
    instudent.append(input(item+" :"))
    