"""
This work is done by Group 2
Edgar Esguerra Jr. - 2021-05780-MN-0 - 25%
Kenji Ilao - 2021-05784-MN-0 - 25%
Shin Lim - 2021-05789-MN-0 - 25%
Siegfred Lorelle Mina - 2021-05794-MN-0 - 25% 
"""

# TODO: ADD COMMENTS

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
        self.student_level = ""
        self.student_type = ""
        self.student_id = ""
        self.student = {}
        self.student_list = []
        self.student_grades = []
        self.history = []

        # Call the startFeature method to assign data and student level, type, and id
        self.startFeature()


    def startFeature(self):
        """ Load student data from student details CSV file then prompt user for their student level, type, and id """
        # Read student details CSV file, save each row as a dictionary then append that dictionary to data
        with open('studentDetails.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.student_list.append(row)

        # Prompt user to select their student level and type/degree
        self.setStudentLevel()
        # Prompt user to enter their student ID
        self.setStudentID()
        # Read the csv file of the student, then save it to student grades
        self.setStudentGrade()

        # Pause the program and clear the screen
        buffer()
        clearScreen()
        # Redirect to menu screen
        self.menuFeature()


    def setStudentLevel(self):
        """ Prompt user to select student level and then ask for type/degree if they have one """
        # Asks for their student level
        print("\nSelect Student Level:\nUndergraduate (U)\nGraduate (G)\nBoth (B)")
        self.student_level = input("\nChoice: ").upper()
        # Check if the given student level is valid
        if self.student_level == "G" or self.student_level == "B":
            self.setDegreeLevel()
        elif self.student_level != "U":
            print("\nPlease use: U/G/B")
            self.setStudentLevel()

    def setDegreeLevel(self):
        """ Prompt user to enter degree level """
        # Ask for their degree/type
        print("\nSelect your level type:\nMaster (M)\nDoctorate (D)\nBoth (B0)")
        self.student_type = input("\nChoice: ").upper()
        # Check if the given degree/type is valid
        if self.student_type != "M" and self.student_type != "D" and self.student_type != "B0":
            print("\nPlease use: M/D/B0")
            self.setDegreeLevel()

    def setStudentID(self):
        """ Prompt user to enter student ID and check if it exists in the data list """
        # Prompt for the new student id
        self.student_id = input("\nEnter your Student ID: ")
        # Check if the given student id is registered
        for student in self.student_list:
            if student['stdID'] == self.student_id:
                self.student = student
                return
        self.setStudentID()

    def setStudentGrade(self):
        """ Read the csv file of the student, then save it to student grades """
        # Clear the student grade list to give space for the new student's grade
        self.student_grades.clear()
        # Read the record/grade of the student, save each row as dictionary, then append it to student grades
        with open(f'{self.student_id}.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.student_grades.append(row)
        # Convert term and grade into int
        for data in self.student_grades:
            data["Term"] = int(data["Term"])
            data["Grade"] = int(data["Grade"])


    def menuFeature(self):
        """ Show all available options in menu. Asks for a choice, then redirect to that feature """
        print('Student Transcript Generation System\n====================================================\n1. Student Details\n2. Statistics\n3. Transcript based on major courses\n4. Transcript based on minor courses\n5. Full transcript\n6. Previous transcript requests\n7. Select another student\n8. Terminate system\n====================================================')
        # Asks the user what to do, then redirects it to that feature
        self.menuManager()


    def detailsFeature(self, student):
        """ Display Details and save it in a text file """
        print(f"Name: {student['Name']}\nstdID: {student['stdID']}\nLevel(s): {student['Level']}\nNumber of Terms: {student['Terms']}\nCollege(s): {student['College']}\nDepartment(s): {student['Department']}")
        file = open(f'stdID{student["stdID"]}.txt', 'w')
        with file as f:
            f.write(f"Name: {student['Name']}\nstdID: {student['stdID']}\nLevel(s): {student['Level']}\nNumber of Terms: {student['Terms']}\nCollege(s): {student['College']}\nDepartment(s): {student['Department']}")


    def statisticsFeature(self, student_level, student_id):
        sum = 0
        minor_sum = 0
        major_sum = 0

        average = 0
        major_average = 0
        minor_average = 0

        count = 0
        major_count = 0
        minor_count = 0

        for i in self.student_grades:
            sum += i['Grade']
            count += 1

            if i['courseType'] == "Major":
                major_sum += i['Grade']
                major_count += 1
            elif i['courseType'] == 'Minor':
                minor_sum += i['Grade']
                minor_count += 1

        average = int(sum / count)
        major_average = int(major_sum / major_count)
        minor_average = int(minor_sum / minor_count)

        nums = [grade['Grade'] for grade in self.student_grades]

        max_grade = max(nums)
        min_grade = min(nums)

        print(student_level)
        if student_level == 'U':
            text_term = ''
            print(f'===================================\nUndergraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}')

            for i in self.student_grades:
                print(f"\tTerm {i['Term']}: {i['Grade']}\n")
                text_term += f"\tTerm {i['Term']}: {i['Grade']}\n"
            
            print(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")

            file = open(f"std{student_id}statistics.txt", 'w')
            file.write(f'===================================\nUndergraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}\n')
            file.write(text_term)
            file.write(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")
        elif student_level == 'G':
            text_term = ''
            print(f'===================================\nGraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}')

            for i in self.student_grades:
                print(f"\tTerm {i['Term']}: {i['Grade']}\n")
                text_term += f"\tTerm {i['Term']}: {i['Grade']}\n"
            
            print(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")

            file = open(f"std{student_id}statistics.txt", 'w')
            file.write(f'===================================\nGraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}\n')
            file.write(text_term)
            file.write(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")
        elif student_level == 'B':
            u_term = ''
            print(f'===================================\nUndergraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}')

            for i in self.student_grades:
                print(f"\tTerm {i['Term']}: {i['Grade']}\n")
                u_term += f"\tTerm {i['Term']}: {i['Grade']}\n"
            
            print(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y\n")

            g_term = ''
            print(f'===================================\nGraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}')

            for i in self.student_grades:
                print(f"\tTerm {i['Term']}: {i['Grade']}\n")
                g_term += f"\tTerm {i['Term']}: {i['Grade']}\n"
            
            print(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")

            file = open(f"std{student_id}statistics.txt", 'w')
            file.write(f'===================================\nUndergraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}\n')
            file.write(u_term)
            file.write(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")

            file = open(f"std{student_id}statistics.txt", 'w')
            file.write(f'===================================\nGraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}\n')
            file.write(g_term)
            file.write(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")


    def majorTranscriptFeature(self, student_level, student_id, student):
        """ Shows the transcript of the student's major courses """
        # Initialize variables
        major = 0
        minor = 0
        major_ave = 0
        major_sum = 0
        major_count = 0

        # Count the number of major and minor courses, compute the student's overall grade in major courses
        for i in self.student_grades:
            if i['courseType'] == 'Major':
                major_sum += i['Grade']
                major_count += 1
                major += 1
            elif i['courseType'] == 'Minor':
                minor += 1
        # Get the student's average grade in all his/her major courses
        major_ave = int(major_sum / major_count)
        # Get all of the student's terms and find the highest/latest
        all_terms = [i["Term"] for i in self.student_grades]
        maxterm = max(all_terms)

        # Create a txt file with a the student's name and major transcript in its filename, if it exists, then overwrite it
        with open(f"std{student_id}MajorTranscript.txt", 'w') as file:
            # Print and write general information the student before proceeding to the transcript of his/her major courses
            print(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}\n")
            file.write(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}\n")

            # Loop from 1 until the latest term
            for i in range(1, maxterm + 1):
                # Initialize variables
                perterm_sum = 0
                perterm_count = 0
                # Print the header for each term
                print(f"=========================================================================\nTerm {i}\n=========================================================================\n")
                print ("{:<8} {:<40} {:<5} {:<5}".format('Course ID','Course Name','Credit Hours','Grade'))
                # Write the same header in the text file
                file.write(f"=========================================================================\nTerm {i}\n=========================================================================\n")
                file.write("{:<8} {:<40} {:<5} {:<5}\n".format('Course ID','Course Name','Credit Hours','Grade'))
                # Loop through each data in the student's grade/record to find major courses in the current term
                for j in self.student_grades:
                    # If the course is major and is in the current term, then add the grade and increment the counter for term
                    if j["Term"] == i and j['courseType'] == 'Major':
                        perterm_sum += j['Grade']
                        perterm_count += 1
                        # Print and write in the text file the information about the major course
                        print ("{:<9} {:<40} {:<12} {:<6}".format(j['courseID'], j['courseName'], j['creditHours'], j['Grade']))
                        file.write("{:<9} {:40} {:<12} {:<6}\n".format(j['courseID'], j['courseName'], j['creditHours'], j['Grade']))

                # After going through the grade/record, and no major course is found, then just print and write that there was no major course
                if perterm_count == 0:
                    print(f"\nNo registered major course this term.\n")
                    file.write(f"\nNo registered major course this term.\n")
                # If there was a major course, then print and write the average in all major courses and the average in that term
                else:
                    print(f"\n\nMajor Average = {major_ave}\nTerm Average = {int(perterm_sum / perterm_count)}\n")
                    file.write(f"\n\nMajor Average = {major_ave}\nTerm Average = {int(perterm_sum / perterm_count)}\n")

        # Record this request with the current date and time, save it in history list via append
        today = date.today()
        now = datetime.now()
        new_h = {
            "req": "Major",
            "date": str(today.strftime("%d/%m/%Y")),
            "time": f"{now.strftime('%H:%M')}"
        }
        self.history.append(new_h)


    def minorTranscriptFeature(self, student_level, student_id, student):
        """  """
        # BUG: OCCURS WHEN NO MINOR COURSE IN THAT TERM
        major = 0
        minor = 0

        minor_ave = 0
        minor_sum = 0
        minor_count = 0

        for i in self.student_grades:
            if i['courseType'] == 'Major':
                minor_sum += i['Grade']
                minor_count += 1
                major += 1
            elif i['courseType'] == 'Minor':
                minor += 1

        
        minor_ave = int(minor_sum / minor_count)

        all_terms = [i["Term"] for i in self.student_grades]
        maxterm = max(all_terms)

        file = open(f"std{student_id}MinorTranscript.txt", 'w')

        print(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}")

        file.write(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}\n")

        for i in range(1, maxterm):

            perterm_sum = 0
            perterm_count = 0

            print(f"===================================\nTerm {i}\n===================================\n")
            print ("{:<8} {:<12} {:<7} {:<10}".format('Course ID','Course Name','Credit Hours','Grade'))

            file.write(f"===================================\nTerm {i}\n===================================\n")
            file.write("{:<8} {:<12} {:<7} {:<10}\n".format('Course ID','Course Name','Credit Hours','Grade'))
            for j in self.student_grades:
                if j["Term"] == i and j['courseType'] == 'Minor':
                    perterm_sum += j['Grade']
                    perterm_count += 1
                    print ("{:<9} {:<12} {:<12} {:<10}".format(j['courseID'], j['courseName'], j['creditHours'], j['Grade']))
                    file.write("{:<9} {:<12} {:<12} {:<10}\n".format(j['courseID'], j['courseName'], j['creditHours'], j['Grade']))
            print(f"\n\nMinor Average = {minor_ave}\nOverall Average = {int(perterm_sum / perterm_count)}")
            file.write(f"\n\nMinor Average = {minor_ave}\nOverall Average = {int(perterm_sum / perterm_count)}\n")
        file.close()

        today = date.today()
        now = datetime.now()
        

        new_h = {
            "req": "Minor",
            "date": str(today.strftime("%d/%m/%Y")),
            "time": f"{now.strftime('%H:%M')}"
        }

        self.history.append(new_h)

    def fullTranscriptFeature(self, student_level, student_id, student):
        # TODO: FIX SPACING (SIMILAR TO MAJOR TRANSCRIPT

        major = 0
        minor = 0

        full_ave = 0
        full_sum = 0
        full_count = 0

        for i in self.student_grades:
            if i['courseType'] == 'Major':
                full_sum += i["Grade"]
                full_count += 1
                major += 1
            elif i['courseType'] == 'Minor':
                minor += 1

        
        full_ave = int(full_sum / full_count)

        all_terms = [i["Term"] for i in self.student_grades]
        maxterm = max(all_terms)

        file = open(f"std{student_id}FullTranscript.txt", 'w')

        print(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}")

        file.write(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}\n")

        for i in range(1, maxterm):

            perterm_sum = 0
            perterm_count = 0

            print(f"===================================\nTerm {i}\n===================================\n")
            print ("{:<8} {:<12} {:<7} {:<10}".format('Course ID','Course Name','Credit Hours','Grade'))

            file.write(f"===================================\nTerm {i}\n===================================\n")
            file.write("{:<8} {:<12} {:<7} {:<10}\n".format('Course ID','Course Name','Credit Hours','Grade'))
            for j in self.student_grades:
                if j["Term"] == i:
                    perterm_sum += j["Grade"]
                    perterm_count += 1
                    print ("{:<9} {:<12} {:<12} {:<10}".format(j['courseID'], j['courseName'], j['creditHours'], j["Grade"]))
                    file.write("{:<9} {:<12} {:<12} {:<10}\n".format(j['courseID'], j['courseName'], j['creditHours'], j["Grade"]))
            print(f"\n\nFull Average = {full_ave}\nOverall Average = {int(perterm_sum / perterm_count)}")
            file.write(f"\n\nFull Average = {full_ave}\nOverall Average = {int(perterm_sum / perterm_count)}\n")
        file.close()

        today = date.today()
        now = datetime.now()

        new_h = {
            "req": "Full",
            "date": str(today.strftime("%d/%m/%Y")),
            "time": f"{now.strftime('%H:%M')}"
        }

        self.history.append(new_h)


    def previousRequestsFeature(self, history, student_id):
        file = open(f"std{student_id}.txt", 'w')
        print("{:<10} {:<15} {:<7}".format('Request','Date','Time'))
        print("=====================================")
        for i in history:
            print ("{:<11} {:<15} {:<12}".format(i['req'], i['date'], i['time']))
            file.write("{:<11} {:<15} {:<12}\n".format(i['req'], i['date'], i['time']))
        file.close()


    def newStudentFeature(self):
        """ Asks for the new student's info """
        # Prompt user to select the new student's level and type/degree
        self.setStudentLevel()
        # Prompt user to enter the new student ID
        self.setStudentID()
        # Read the csv file of the student, then save it to student grades
        self.setStudentGrade()


    def terminateFeature(self):
        sys.exit("Goodbye!\n")


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