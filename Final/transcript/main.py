"""
This work is done by Group 2
Edgar Esguerra Jr. - 2021-05780-MN-0 - 25%
Kenji Ilao - 2021-05784-MN-0 - 25%
Shin Lim - 2021-05789-MN-0 - 25%
Siegfred Lorelle Mina - 2021-05794-MN-0 - 25% 
"""


# TODO: ADD COMMENTS
# TODO: USE DICT READER WHEN READING INDIVIDUAL STUDENT'S CSV
# TODO: USE SWITCH CASE IN MENU MANAGER

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
        self.student_level = ' '
        self.student_type = ' '
        self.student_id = ' '
        self.data = []
        self.history = []
        self.student = {}

        # Call the startFeature method to assign data and student level, type, and id
        self.startFeature()


    def startFeature(self):
        """ Load student data from student details CSV file then prompt user for their student level, type, and id """
        # Read student details CSV file, save each row as a dictionary then append that dictionary to data
        with open('studentDetails.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data.append(row)

        # Prompt user to select student level and type/degree
        self.getStudentLevel()
        # Prompt user to enter student ID
        self.getStudentID()

        # Pause the program and clear the screen
        buffer()
        clearScreen()
        # Redirect to menu screen
        self.menuFeature()


    def getStudentLevel(self):
        """ Prompt user to select student level and then ask for type/degree if they have one """
        # Asks for their student level
        print("Select Student Level:\nUndergraduate (U)\nGraduate (G)\nBoth (B)")
        self.student_level = input("\nChoice: ").upper()
        # Check if the given student level is valid
        if self.student_level == "G" or self.student_level == "B":
            self.getDegreeLevel()
        elif self.student_level != "U":
            print("\nPlease use: U/G/B\n")
            self.getStudentLevel()

    def getDegreeLevel(self):
        """ Prompt user to enter degree level """
        # Ask for their degree/type
        print("\nSelect your level type:\nMaster (M)\nDoctorate (D)\nBoth (B0)")
        self.student_type = input("\nChoice: ").upper()
        # Check if the given degree/type is valid
        if self.student_type != "M" and self.student_type != "D" and self.student_type != "B0":
            print("\nPlease use: M/D/B0\n")
            self.getDegreeLevel()

    def getStudentID(self):
        """ Prompt user to enter student ID and check if it exists in the data list """
        # Prompt for the new student id
        self.student_id = input("\nEnter your Student ID: ")
        # Check if the given student id is registered
        for i in self.data:
            if i['stdID'] == self.student_id:
                self.student = i
                return
        self.getStudentID()


    def menuFeature(self):
        """ Show all available options in menu. Asks for a choice, then redirect to that feature """
        print('Student Transcript Generation System\n====================================================\n1. Student Details\n2. Statistics\n3. Transcript based on major courses\n4. Transcript based on minor courses\n5. Full transcript\n6. Previous transcript requests\n7. Select another student\n8. Terminate system\n====================================================')
        # Asks the user what to do, then redirects it to that feature
        self.menuManager()


    # Display Details and save it in a text file
    def detailsFeature(self, student):
        print(f"Name: {student['Name']}\nstdID: {student['stdID']}\nLevel(s): {student['Level']}\nNumber of Terms: {student['Terms']}\nCollege(s): {student['College']}\nDepartment(s): {student['Department']}")
        file = open(f'stdID{student["stdID"]}.txt', 'w')
        with file as f:
            f.write(f"Name: {student['Name']}\nstdID: {student['stdID']}\nLevel(s): {student['Level']}\nNumber of Terms: {student['Terms']}\nCollege(s): {student['College']}\nDepartment(s): {student['Department']}")


    def statisticsFeature(self, student_level, student_id):
        data = []

        # TODO: USE DICT READER
        file = open(f"{self.student_id}.csv")
        reader = csv.reader(file)
        tempheader = next(reader)

        for row in reader:
            temp = {
                "level": row[0],
                "degree": row[1],
                "term": int(row[2]),
                "courseName": row[3],
                "courseID": row[4],
                "courseType": row[5],
                "creditHours": row[6],
                "grade": int(row[7]),
            }

            data.append(temp)

        sum = 0
        minor_sum = 0
        major_sum = 0

        average = 0
        major_average = 0
        minor_average = 0

        count = 0
        major_count = 0
        minor_count = 0

        for i in data:
            sum += i['grade']
            count += 1

            if i['courseType'] == "Major":
                major_sum += i['grade']
                major_count += 1
            elif i['courseType'] == 'Minor':
                minor_sum += i['grade']
                minor_count += 1
        
        average = int(sum / count)
        major_average = int(major_sum / major_count)
        minor_average = int(minor_sum / minor_count)

        nums = [i['grade'] for i in data]

        max_grade = max(nums)
        min_grade = min(nums)

        print(student_level)
        if student_level == 'U':
            text_term = ''
            print(f'===================================\nUndergraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}')

            for i in data:
                print(f"\tTerm {i['term']}: {i['grade']}\n")
                text_term += f"\tTerm {i['term']}: {i['grade']}\n"
            
            print(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")

            file = open(f"std{student_id}statistics.txt", 'w')
            file.write(f'===================================\nUndergraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}\n')
            file.write(text_term)
            file.write(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")
        elif student_level == 'G':
            text_term = ''
            print(f'===================================\nGraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}')

            for i in data:
                print(f"\tTerm {i['term']}: {i['grade']}\n")
                text_term += f"\tTerm {i['term']}: {i['grade']}\n"
            
            print(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")

            file = open(f"std{student_id}statistics.txt", 'w')
            file.write(f'===================================\nGraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}\n')
            file.write(text_term)
            file.write(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y")
        elif student_level == 'B':
            u_term = ''
            print(f'===================================\nUndergraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}')

            for i in data:
                print(f"\tTerm {i['term']}: {i['grade']}\n")
                u_term += f"\tTerm {i['term']}: {i['grade']}\n"
            
            print(f"Maximum grade(s) and in which term(s): {max_grade}\nMinimum grade(s) and in which term(s): {min_grade}\nDo you have any repeated course(s)?: Y\n")

            g_term = ''
            print(f'===================================\nGraduate Level\n===================================\nOverall average (major and minor) for all terms: {average}\nAverage (major and minor) of each term: {major_average} & {minor_average}')

            for i in data:
                print(f"\tTerm {i['term']}: {i['grade']}\n")
                g_term += f"\tTerm {i['term']}: {i['grade']}\n"
            
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
        data = []

        file = open(f"{student_id}.csv")
        reader = csv.reader(file)
        tempheader = next(reader)

        major = 0
        minor = 0

        for row in reader:
            temp = {
                "level": row[0],
                "degree": row[1],
                "term": int(row[2]),
                "courseName": row[3],
                "courseID": row[4],
                "courseType": row[5],
                "creditHours": row[6],
                "grade": int(row[7]),
            }

            if temp['courseType'] == 'Major':
                major += 1
            elif temp['courseType'] == 'Minor':
                minor += 1

            data.append(temp)


        major_ave = 0
        major_sum = 0
        major_count = 0

        for i in data:
            if i['courseType'] == 'Major':
                major_sum += i['grade']
                major_count += 1
        
        major_ave = int(major_sum / major_count)
            

        all_terms = [i['term'] for i in data]
        maxterm = max(all_terms)

        file = open(f"std{student_id}MajorTranscript.txt", 'w')

        print(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}")

        file.write(f"Name: {student['Name']}\nstdID: {student['stdID']}\nCollege: {student['College']}\nDepartment: {student['Department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['Level']}\nNumber of Terms: {maxterm}\n")

        for i in range(1, maxterm):

            perterm_sum = 0
            perterm_count = 0

            print(f"===================================\nTerm {i}\n===================================\n")
            print ("{:<8} {:<12} {:<7} {:<10}".format('Course ID','Course Name','Credit Hours','Grade'))

            file.write(f"===================================\nTerm {i}\n===================================\n")
            file.write("{:<8} {:<12} {:<7} {:<10}\n".format('Course ID','Course Name','Credit Hours','Grade'))


            for j in data:
                if j['term'] == i and j['courseType'] == 'Major':
                    perterm_sum += j['grade']
                    perterm_count += 1
                    print ("{:<9} {:<12} {:<12} {:<10}".format(j['courseID'], j['courseName'], j['creditHours'], j['grade']))
                    file.write("{:<9} {:<12} {:<12} {:<10}\n".format(j['courseID'], j['courseName'], j['creditHours'], j['grade']))


            print(f"\n\nMajor Average = {major_ave}\nOverall Average = {int(perterm_sum / perterm_count)}")
            file.write(f"\n\nMajor Average = {major_ave}\nOverall Average = {int(perterm_sum / perterm_count)}\n")
        file.close()

        today = date.today()
        now = datetime.now()
        

        new_h = {
            "req": "Major",
            "date": str(today.strftime("%d/%m/%Y")),
            "time": f"{now.strftime('%H:%M')}"
        }

        self.history.append(new_h)


    def minorTranscriptFeature(self, student_level, student_id, student):
        data = []

        file = open(f"{student_id}.csv")
        reader = csv.reader(file)
        tempheader = next(reader)

        major = 0
        minor = 0

        for row in reader:
            temp = {
                "level": row[0],
                "degree": row[1],
                "term": int(row[2]),
                "courseName": row[3],
                "courseID": row[4],
                "courseType": row[5],
                "creditHours": row[6],
                "grade": int(row[7]),
            }

            if temp['courseType'] == 'Major':
                major += 1
            elif temp['courseType'] == 'Minor':
                minor += 1

            data.append(temp)
        
        minor_ave = 0
        minor_sum = 0
        minor_count = 0

        for i in data:
            if i['courseType'] == 'Major':
                minor_sum += i['grade']
                minor_count += 1
        
        minor_ave = int(minor_sum / minor_count)

        all_terms = [i['term'] for i in data]
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
            for j in data:
                if j['term'] == i and j['courseType'] == 'Minor':
                    perterm_sum += j['grade']
                    perterm_count += 1
                    print ("{:<9} {:<12} {:<12} {:<10}".format(j['courseID'], j['courseName'], j['creditHours'], j['grade']))
                    file.write("{:<9} {:<12} {:<12} {:<10}\n".format(j['courseID'], j['courseName'], j['creditHours'], j['grade']))
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
        data = []

        file = open(f"{student_id}.csv")
        reader = csv.reader(file)
        tempheader = next(reader)

        major = 0
        minor = 0

        for row in reader:
            temp = {
                "level": row[0],
                "degree": row[1],
                "term": int(row[2]),
                "courseName": row[3],
                "courseID": row[4],
                "courseType": row[5],
                "creditHours": row[6],
                "grade": int(row[7]),
            }

            if temp['courseType'] == 'Major':
                major += 1
            elif temp['courseType'] == 'Minor':
                minor += 1

            data.append(temp)
        
        full_ave = 0
        full_sum = 0
        full_count = 0

        for i in data:
            if i['courseType'] == 'Major':
                full_sum += i['grade']
                full_count += 1
        
        full_ave = int(full_sum / full_count)

        all_terms = [i['term'] for i in data]
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
            for j in data:
                if j['term'] == i:
                    perterm_sum += j['grade']
                    perterm_count += 1
                    print ("{:<9} {:<12} {:<12} {:<10}".format(j['courseID'], j['courseName'], j['creditHours'], j['grade']))
                    file.write("{:<9} {:<12} {:<12} {:<10}\n".format(j['courseID'], j['courseName'], j['creditHours'], j['grade']))
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
        # Prompt user to select the new student's level and type/degree
        self.getStudentLevel()
        # Prompt user to enter the new student ID
        self.getStudentID()


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
