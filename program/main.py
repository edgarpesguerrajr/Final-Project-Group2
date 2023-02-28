"""
This work is done by Group 2
Edgar Esguerra Jr. - 2021-05780-MN-0 - 25%
Kenji Ilao - 2021-05784-MN-0 - 25%
Shin Lim - 2021-05789-MN-0 - 25%
Siegfred Lorelle Mina - 2021-05794-MN-0 - 25% 
"""

# TODO: ADD COMMENTS
# TODO: PASS ARGUMENTS WHEN CALLING METHODS IN MENU MANAGER
# TODO: USE INTERPOLATED STRING (F-STRING) INSTEAD OF FORMAT FUNCTION
# TODO: IN STATISTICS, AND TRANSCRIPTS, ONLY SHOW CHOSEN LEVEL AND DEGREE
# TODO: WHEN TERMINATING, TELL HOW MANY REQUEST TOTAL
# TODO: CREATE FUNCTION FOR CLEAR VARIABLES

import csv
import sys
import os
from datetime import date, datetime


def main():
    """ Initialize the App upon starting the program """
    App()


class App:
    def __init__(self):
        """ Initialize all variables, then assign them in start feature """
        self.student_level = set()
        self.student_type = set()
        self.student_id = ""
        self.student = {
            "Name": "",
            "Levels": set(),
            "Colleges": set(),
            "Departments": set(),
            "Num of terms": 0,
        }
        self.student_list = []
        self.student_grades = []
        self.history = []

        # Call the startFeature method to assign data and student level, type, and id
        self.startFeature()


    def startFeature(self):
        """ Load student data from student details CSV file then prompt user for their student level, type, and id """
        # Resets the variables to give way for new student
        self.student_list.clear()
        self.student_level.clear()
        self.student_type.clear()
        self.student["Name"] = ""
        self.student["Levels"].clear()
        self.student["Colleges"].clear()
        self.student["Departments"].clear()
        self.student["Num of terms"] = 0
        # Clear the student grade list to give space for the new student's grade
        self.student_grades.clear()
        
        # Read student details CSV file, save each row as a dictionary then append that dictionary to data
        with open('studentDetails.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.student_list.append(row)

        # Prompt user to select their student level and type/degree
        self.setStudentLevel()
        # Prompt user to enter their student ID
        self.setStudentID()

        # Ensure that the given student level, degree and id exists in the student details
        if not self.isStudentRegistered():
            print("\nA student with the given information doesn't exists. Try Again.")
            buffer()
            clearScreen()
            return self.startFeature()

        # Read the he student details csv of the which contains all students, save only the information relevant to the user
        self.setStudentInfos()
        # Read the csv file of the student's grade/record, then save it to student grades
        self.setStudentGrade()
        # Read the txt file of the student's previous requests, then save it to  history
        self.setHistory()

        # Pause the program and clear the screen
        buffer()
        clearScreen()
        # Redirect to menu screen
        self.menuFeature()


    def setStudentLevel(self):
        """ Prompt user to select student level and then ask for type/degree if they have one """
        LEVELS = {
            "U": "Undergraduate",
            "G": "Graduate",
        }

        # Asks for their student level
        print("\nSelect Student Level:\nUndergraduate (U)\nGraduate (G)\nBoth (B)")

        while True:
            level = input("\nChoice: ").upper()

            if level in LEVELS:
                self.student_level.add(level)
                break
            elif level == "B":
                self.student_level.update(["U", "G"])
                break
            print("\nPlease use: U/G/B")
        
        if "U" in self.student_level:
            self.student_type.add("BS")
        if "G" in self.student_level:
            self.setDegreeLevel()


    def setDegreeLevel(self):
        """ Prompt user to enter degree level """
        DEGREES = {
            "M": "Master",
            "D": "Doctorate",
        }

        # Ask for their degree/type
        print("\nSelect your level type:\nMaster (M)\nDoctorate (D)\nBoth (B0)")
        while True:
            degree = input("\nChoice: ").upper()
            if degree in DEGREES:
                self.student_type.add(degree)
                break
            elif degree == "B0":
                self.student_type.update({"M", "D"})
                break
            print("\nPlease use: M/D/B0")


    def setStudentID(self):
        """ Prompt user to enter student ID and check if it exists in the data list """
        # Prompt for the new student id
        self.student_id = input("\nEnter your Student ID: ")
        # Check if the given student id is registered
        for student in self.student_list:
            if student['stdID'] == self.student_id:
                return
        return self.setStudentID()

    def setStudentInfos(self):
        """ Save student information relevant to the user """
        # Loop through the student list to find information relevant to the user
        for student in self.student_list:
            if student["stdID"] != self.student_id:
                continue
            if student["Level"] not in self.student_level:
                continue
            # Degrees in the student details csv has digits, so strip them to match degree inputted by the user
            degree_without_digits = ''.join(i for i in student["Degree"] if not i.isdigit()).strip()
            if degree_without_digits not in self.student_type:
                continue

            # If student matches the information given by user then save the information in student dictionary
            self.student["Name"] = student["Name"]
            self.student["Levels"].add(student["Level"])
            self.student["Colleges"].add(student["College"])
            self.student["Departments"].add(student["Department"])
            self.student["Num of terms"] += int(student["Terms"])

    def isStudentRegistered(self):
        """ Checks if the student information given is registered in the student details csv """
        for student in self.student_list:
            if student["stdID"] != self.student_id:
                continue
            if student["Level"] not in self.student_level:
                continue
            degrees_without_digits = ''.join(i for i in student["Degree"] if not i.isdigit()).strip()
            if degrees_without_digits not in self.student_type:
                continue
            return True
        return False

    def setStudentGrade(self):
        """ Read the csv file of the student, then save it to student grades """
        # Read the record/grade of the student, save each row as dictionary, then append it to student grades
        with open(f'{self.student_id}.csv', "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                degree_without_digits = ''.join(i for i in row["Degree"] if not i.isdigit()).strip()
                if row["Level"] in self.student_level and degree_without_digits in self.student_type:
                    self.student_grades.append(row)
        # Convert term and grade into int
        for data in self.student_grades:
            data["Term"] = int(data["Term"])
            data["Grade"] = int(data["Grade"])

        # [print(i) for i in self.student_grades]

    def setHistory(self):
        """ Read the csv file of the student's previous request and save it in history """
        # Clear the history list to give space for the new student's history
        self.history.clear()
        filename = f"std{self.student_id}PreviousRequest.txt"
        # If the previous request txt file of the student doesn't exists then do nothing
        if not os.path.exists(filename):
            return
        # Open the previous request txt file of the student
        with open(filename, 'r') as file:
            # Skip the first two line (header)
            reader = file.readlines()[2:]
            # Loop through each line
            for line in reader:
                # Separate data in a line by space
                line = line.split()
                # Via request dictionary, save each data to their appropriate header value
                request = {
                    "req": line[0],
                    "date": line[1],
                    "time": line[2]
                }
                # Append the request in history
                self.history.append(request)
    
    def saveHistory(self):
        """ Save previous requests of the student via txt file """
        # Create a txt file with a the student's name and previous request in its filename, if it exists, then overwrite it
        with open(f"std{self.student_id}PreviousRequest.txt", 'w') as file:
            # Write the header
            file.write("{:^12} {:^15} {:^7}\n".format('Request','Date','Time'))
            file.write("=========================================\n")
            # Loop through history and write each request
            for request in self.history:
                file.write("{:^12} {:^15} {:^7}\n".format(request['req'], request['date'], request['time']))


    def recordRequest(self, request):
        """ Record this request with the current date and time, save it in history list via append """
        today = date.today()
        now = datetime.now()
        new_h = {
            "req": request,
            "date": str(today.strftime("%d/%m/%Y")),
            "time": f"{now.strftime('%H:%M')}"
        }
        self.history.append(new_h)
        self.saveHistory()

    def menuFeature(self):
        """ Show all available options in menu. Asks for a choice, then redirect to that feature """
        print('Student Transcript Generation System\n====================================================\n1. Student Details\n2. Statistics\n3. Transcript based on major courses\n4. Transcript based on minor courses\n5. Full transcript\n6. Previous transcript requests\n7. Select another student\n8. Terminate system\n====================================================')
        # Asks the user what to do, then redirects it to that feature
        self.menuManager()


    def detailsFeature(self, student):
        """ Display Details and save it in a text file """
        text = (
            f"Name: {student['Name']}"
            f"\nstdID: {self.student_id}"
            f"\nLevel(s): {', '.join(student['Levels'])}"
            f"\nNumber of Terms: {student['Num of terms']}"
            f"\nCollege(s): {', '.join(student['Colleges'])}"
            f"\nDepartment(s): {', '.join(student['Departments'])}"
        )


        print(text)
        with open(f'std{self.student_id}Details.txt', 'w') as file: 
            file.write(text)
        
        # Record this request
        self.recordRequest("Details")

    def statisticsFeature(self, student_level, student_id):
        """ Show some statistics about the student's grade/record. Examples are average grade per term, minimum and maximum grades. """

        text= ""
        for level in sorted(self.student["Levels"], reverse=True):
            # Initialize variables
            grades_info = [grade for grade in self.student_grades if grade["Level"] == level]
            grades = [grade["Grade"] for grade in grades_info]
            average = int(sum(grades) / len(grades))
            max_grade = max(grades)
            min_grade = min(grades)
            terms_with_max_grade = {str(grade["Term"]) for grade in grades_info if grade["Grade"] == max_grade}
            terms_with_min_grade = {str(grade["Term"]) for grade in grades_info if grade["Grade"] == min_grade}
            last_term = max([grade["Term"] for grade in grades_info])

            # Change the text header depending on what level (undergraduate for U, graduate for G)
            if level == "U":
                # Save and print the header
                text += (
                    "===================================================================\n"
                    f"Undergraduate Level\n"
                    "===================================================================\n"
                )
            else:
                text += (
                    "===================================================================\n"
                    f"Graduate Level\n"
                    "===================================================================\n"
                )
            # After the header, concatenate the text for the averages
            text += (
                f"Overall average (major and minor) for all terms: {average}\n"
                f"Average (major and minor) of each term:\n"
            )

            # Loop through each terms
            for term in range(1, last_term + 1):
                grades_per_term = []
                # Loop through the student's grade/record, get the average grade per term
                for grade in grades_info:
                    if term == grade["Term"]:
                        grades_per_term.append(grade["Grade"])
                average_per_term = int(sum(grades_per_term) / len(grades_per_term))
                # Concatenate the the average grade per term to text string
                text += f"\tTerm {term}: {average_per_term}\n"

            # Concatenate the minimum and maximum grades to text string
            text += (
                f"\nMaximum grade(s) and in which term(s): {max_grade} in term {', '.join(terms_with_max_grade)}"
                f"\nMinimum grade(s) and in which term(s): {min_grade} in term {', '.join(terms_with_min_grade)}"
                "\nDo you have any repeated course(s)?: Y\n\n"
            )

        # Print and write the text
        print(text, end="")
        with open(f"std{student_id}Statistics.txt", "w") as file:
            file.write(text)

        # Record this request
        self.recordRequest("Statistics")


    def majorTranscriptFeature(self, student_level, student_id, student):
        """ Shows the transcript of the student's major courses """
        # Initialize variables
        major_courses = [grade for grade in self.student_grades if grade["courseType"] == "Major"]
        minor_courses = [grade for grade in self.student_grades if grade["courseType"] == "Minor"]

        name = student['Name']
        student_id = student_id
        num_of_major = str(len(major_courses))
        num_of_minor = str(len(minor_courses))
        colleges = ', '.join(sorted(self.student['Colleges'], reverse=True))
        departments = ', '.join(sorted(self.student['Departments'], reverse=True))
        levels = ', '.join(sorted(self.student['Levels'], reverse=True))
        last_term = max([grade["Term"] for grade in self.student_grades])

        text = (
            f"{'Name: ' + name: <50} student ID: {student_id}\n"
            f"{'College: ' + colleges:<50} Department: {departments}\n"
            f"{'Major: ' + num_of_major:<50} Minor: {num_of_minor}\n"
            f"{'Level: ' + levels:<50} Number of terms: {last_term}\n\n"
        )

        # Compute overall average in all major courses
        major_grades = [grade["Grade"] for grade in major_courses]
        overall_major_average = str(int(sum(major_grades) / len(major_grades)))

        for term in range(1, last_term + 1):
            # Concatenate the header for each term
            text += (
                f"=================================================================================\n"
                f"Term {term}"
                f"\n=================================================================================\n"
            )

            grades_per_term = []
            course_text = ""
            for grade in major_courses:
                if term == grade["Term"]:
                    grades_per_term.append(grade["Grade"])
                    course_text += f"{grade['courseID']:^12} {grade['courseName']:^43} {grade['creditHours']:^12} {grade['Grade']:^8}\n"

            # Solve the average
            # grades_per_term = [grade["Grade"] for grade in major_courses if term == grade["Term"]]
            if len(grades_per_term) <= 0:
                text += "\nNo registered major course this term.\n\n"
                continue
            
            text += f"{'Course ID':^12} {'Course Name':^43} {'Credit Hours':^12} {'Grade':^10}\n"
            text += course_text
            average_grade_per_term = str(int(sum(grades_per_term) / len(grades_per_term)))
            # # Concatenate the the average grade per term to text string
            text += f"\n{'Overall Major Average: ' + overall_major_average:<52} Term Major Average: {average_grade_per_term}\n\n"

        print(text)
        with open(f"std{self.student_id}MajorTranscript.txt", "w") as file:
            file.write(text)

        # Record this request
        self.recordRequest("Major")


    def minorTranscriptFeature(self, student_level, student_id, student):
        """ Shows the transcript of the student's minor courses """
        # Initialize variables
        major_courses = [grade for grade in self.student_grades if grade["courseType"] == "Major"]
        minor_courses = [grade for grade in self.student_grades if grade["courseType"] == "Minor"]

        name = student['Name']
        student_id = student_id
        num_of_major = str(len(major_courses))
        num_of_minor = str(len(minor_courses))
        colleges = ', '.join(sorted(self.student['Colleges'], reverse=True))
        departments = ', '.join(sorted(self.student['Departments'], reverse=True))
        levels = ', '.join(sorted(self.student['Levels'], reverse=True))
        last_term = max([grade["Term"] for grade in self.student_grades])

        text = (
            f"{'Name: ' + name: <50} student ID: {student_id}\n"
            f"{'College: ' + colleges:<50} Department: {departments}\n"
            f"{'Major: ' + num_of_major:<50} Minor: {num_of_minor}\n"
            f"{'Level: ' + levels:<50} Number of terms: {last_term}\n\n"
        )

        # Compute overall average in all major courses
        minor_grades = [grade["Grade"] for grade in minor_courses]
        overall_minor_average = str(int(sum(minor_grades) / len(minor_grades)))

        for term in range(1, last_term + 1):
            # Concatenate the header for each term
            text += (
                f"=================================================================================\n"
                f"Term {term}"
                f"\n=================================================================================\n"
            )

            grades_per_term = []
            course_text = ""
            for grade in minor_courses:
                if term == grade["Term"]:
                    grades_per_term.append(grade["Grade"])
                    course_text += f"{grade['courseID']:^12} {grade['courseName']:^43} {grade['creditHours']:^12} {grade['Grade']:^8}\n"

            # Solve the average
            if len(grades_per_term) <= 0:
                text += "\nNo registered minor course this term.\n\n"
                continue
            
            text += f"{'Course ID':^12} {'Course Name':^43} {'Credit Hours':^12} {'Grade':^10}\n"
            text += course_text
            average_grade_per_term = str(int(sum(grades_per_term) / len(grades_per_term)))
            # # Concatenate the the average grade per term to text string
            text += f"\n{'Overall Minor Average: ' + overall_minor_average:<52} Term Minor Average: {average_grade_per_term}\n\n"

        print(text)
        with open(f"std{self.student_id}MinorTranscript.txt", "w") as file:
            file.write(text)
        
        # Record this request
        self.recordRequest("Minor")


    def fullTranscriptFeature(self, student_level, student_id, student):
        """ Shows the transcript of the student's courses (both major and minor courses) """
        # Initialize variables
        major = 0
        minor = 0
        full_ave = 0
        full_sum = 0
        full_count = 0

        # Count the number of major and minor courses, compute the student's overall grade
        for i in self.student_grades:
            full_sum += i["Grade"]
            full_count += 1
            if i['courseType'] == 'Major':
                major += 1
            elif i['courseType'] == 'Minor':
                minor += 1
        # Get the student's average grade in all his/her courses
        full_ave = int(full_sum / full_count)
        # Get all of the student's terms and find the highest/latest
        all_terms = [i["Term"] for i in self.student_grades]
        maxterm = max(all_terms)

        # Create a txt file with a the student's name and full transcript in its filename, if it exists, then overwrite it
        with open(f"std{student_id}FullTranscript.txt", 'w') as file:
            # Print and write general information the student before proceeding to the transcript of his/her courses
            print(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}")
            file.write(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}\n")

            # Loop from 1 until the latest term
            for i in range(1, maxterm + 1):
                # Initialize variables
                perterm_sum = 0
                perterm_count = 0
                # Print the header for each term
                print(f"=========================================================================\nTerm {i}\n=========================================================================\n")
                print ("{:^8} {:^40} {:^5} {:^5}".format('Course ID','Course Name','Credit Hours','Grade'))
                # Write the same header in the text file
                file.write(f"=========================================================================\nTerm {i}\n=========================================================================\n")
                file.write("{:^8} {:^40} {:^5} {:^5}\n".format('Course ID','Course Name','Credit Hours','Grade'))
                # Loop through each data in the student's grade/record to find courses in the current term
                for j in self.student_grades:
                    # If the course is in the current term, then add the grade and increment the counter for number of courses per term
                    if j["Term"] == i:
                        perterm_sum += j["Grade"]
                        perterm_count += 1
                        # Print and write in the text file the information about the course
                        print ("{:^9} {:^40} {:^12} {:^5}".format(j['courseID'], j['courseName'], j['creditHours'], j["Grade"]))
                        file.write("{:^9} {:^40} {:^12} {:^5}\n".format(j['courseID'], j['courseName'], j['creditHours'], j["Grade"]))
                
                # After going through the grade/record, and no course is found, then just print and write that there was no course
                if perterm_count == 0:
                    print(f"\nNo registered course this term.\n")
                    file.write(f"\nNo registered course this term.\n")
                else:
                    # Print and write the average in all courses and the average of courses in that term
                    print(f"\n\nFull Average = {full_ave}\nTerm Average = {int(perterm_sum / perterm_count)}\n")
                    file.write(f"\n\nFull Average = {full_ave}\nTerm Average = {int(perterm_sum / perterm_count)}\n")

        # Record this request
        self.recordRequest("Full")


    def previousRequestsFeature(self, history, student_id):
        """ Shows the previous requests of the student """
        # Print the header
        print("{:^12} {:^15} {:^7}".format('Request','Date','Time'))
        print("=========================================")
        # Loop through history and print and write each request
        for request in history:
            print ("{:^12} {:^15} {:^7}".format(request['req'], request['date'], request['time']))
        # Save the requests in history in a text file
        self.saveHistory()

    def newStudentFeature(self):
        """ Asks for the new student's info """
        # Prompt user to select the new student's level and type/degree
        self.setStudentLevel()
        # Prompt user to enter the new student ID
        self.setStudentID()

        # Ensure that the given student level, degree and id exists in the student details
        if not self.isStudentRegistered():
            print("\nA student with the given information doesn't exists. Try Again.")
            buffer()
            clearScreen()
            self.startFeature()

        # Read the csv file of the new student, then save it to student grades
        self.setStudentGrade()
        # Read the csv file of the news student's previous request, then save it to history
        self.setHistory()
        


    def terminateFeature(self):
        """ Terminates/exit/close the program """
        print("The program is closing ...\nGoodbye!\n")
        sys.exit()


    def menuManager(self):
        """ Asks user which feature to use, then redirects to that feature """
        # Asks for a feature
        choice = input("Enter your Feature: ")
        clearScreen()
        # Redirect to specific feature based on user choice
        match choice:
            case "1":
                self.detailsFeature(self.student)
            case "2":
                self.statisticsFeature(self.student_level, self.student_id)
            case "3":
                self.majorTranscriptFeature(self.student_level, self.student_id, self.student)
            case "4":
                self.minorTranscriptFeature(self.student_level, self.student_id, self.student)
            case "5":
                self.fullTranscriptFeature(self.student_level, self.student_id, self.student)
            case "6":
                self.previousRequestsFeature(self.history, self.student_id)
            case "7":
                self.newStudentFeature()
            case "8":
                self.terminateFeature()
            case _:
                print("Invalid Input!")
        # After every feature, add a buffer to let user read, then clear screen and go back to menu screen
        buffer()
        clearScreen()
        self.menuFeature()


def buffer():
    """ Acts as buffer to give enough time for user to read the texts """
    input("\nPress enter to proceed ...")

def clearScreen():
    """ Clears the screen regardless of the OS """
    # Posix is OS name for Linux or Mac, 'clear' cmd clears the screen for Linux and Mac
    if os.name == "posix":
        os.system("clear")
    # for Windows (os name is 'nt'), 'cls' command clears the screen
    else:
        os.system("cls")

if __name__ == "__main__":
    main()