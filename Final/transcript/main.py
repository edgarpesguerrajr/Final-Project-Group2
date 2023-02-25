# This work is done by Group 2
# Edgar Esguerra Jr. - 2021-05780-MN-0 - 25%
# Kenji Ilao - 2021-05784-MN-0 - 25%
# Shin Lim - 2021-05789-MN-0 - 25%
# Siegfred Lorelle Mina - 2021-05794-MN-0 - 25%

import csv
import sys
from os import system
from datetime import date, datetime


class App:
    def __init__(self):
        self.student_level = ' '
        self.student_type = ' '
        self.student_id = ' '
        self.data = []
        self.history = []
        self.student = {}

        self.startFeature()


    def startFeature(self):
        system("cls")

        tempheader = []

        file = open('studentDetails.csv')
        reader = csv.reader(file)
        tempheader = next(reader)

        for row in reader:
            temp = {
                "serial": row[0],
                "stdID": row[1],
                "name": row[2],
                "college": row[3],
                "department": row[4],
                "level": row[5],
                "degree": row[6],
                "major": row[7],
                "minor": row[8],
                "terms": row[9]
            }
            self.data.append(temp)

        # TODO: ONLY ASK FOR DEGREE/TYPE WHEN GRADUATE OR BOTH
        # TODO: ACCEPTING INVALID INPUT (STUDENT LEVEL AND STUDENT TYPE)
        self.student_level = input("Select Student Level:\nUndergraduate (U)\nGraduate (G)\nBoth (B)\nChoice: ").upper()
        self.student_type = input("\nSelect your level type:\nMaster (M)\nDoctorate (D)\nBoth (B0)\nChoice: ").upper()

        fix = True
        while fix:
            self.student_id = input("Enter your Student ID: ")
            for i in self.data:
                if i['stdID'] == self.student_id:
                    self.student = i
                    fix = False

        system('pause')
        system('cls')

        self.menuFeature()
        
    # General Menu
    def menuFeature(self):
        print('Student Transcript Generation System\n====================================================\n1. Student Details\n2. Statistics\n3. Transcript based on major courses\n4. Transcript based on minor courses\n5. Full transcript\n6. Previous transcript requests\n7. Select another student\n8. Terminate system\n====================================================')

        #ASKS FOR CHOICE
        self.menu_manager()




    # Display Details and save it in a text file
    def detailsFeature(self, student):
        print(f"Name: {student['name']}\nstdID: {student['stdID']}\nLevel(s): {student['level']}\nNumber of Terms: {student['terms']}\nCollege(s): {student['college']}\nDepartment(s): {student['department']}")
        file = open(f'stdID{student["stdID"]}.txt', 'w')
        with file as f:
            f.write(f"Name: {student['name']}\nstdID: {student['stdID']}\nLevel(s): {student['level']}\nNumber of Terms: {student['terms']}\nCollege(s): {student['college']}\nDepartment(s): {student['department']}")

    def statisticsFeature(self, student_level, student_id):
        data = []

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

        print(f"Name: {student['name']}\nstdID: {student['stdID']}\nCollege: {student['college']}\nDepartment: {student['department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['level']}\nNumber of Terms: {maxterm}")

        file.write(f"Name: {student['name']}\nstdID: {student['stdID']}\nCollege: {student['college']}\nDepartment: {student['department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['level']}\nNumber of Terms: {maxterm}\n")

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

        print(f"Name: {student['name']}\nstdID: {student['stdID']}\nCollege: {student['college']}\nDepartment: {student['department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['level']}\nNumber of Terms: {maxterm}")

        file.write(f"Name: {student['name']}\nstdID: {student['stdID']}\nCollege: {student['college']}\nDepartment: {student['department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['level']}\nNumber of Terms: {maxterm}\n")

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

        print(f"Name: {student['name']}\nstdID: {student['stdID']}\nCollege: {student['college']}\nDepartment: {student['department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['level']}\nNumber of Terms: {maxterm}")

        file.write(f"Name: {student['name']}\nstdID: {student['stdID']}\nCollege: {student['college']}\nDepartment: {student['department']}\nMajor: {major}\nMinor: {minor}\nLevel: {student['level']}\nNumber of Terms: {maxterm}\n")

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

        tempheader = []

        file = open('studentDetails.csv')
        reader = csv.reader(file)
        tempheader = next(reader)

        for row in reader:
            temp = {
                "serial": row[0],
                "stdID": row[1],
                "name": row[2],
                "college": row[3],
                "department": row[4],
                "level": row[5],
                "degree": row[6],
                "major": row[7],
                "minor": row[8],
                "terms": row[9]
            }
            self.data.append(temp)


        self.student_level = input("Select Student Level:\nUndergraduate (U)\nGraduate (G)\nBoth (B)\nChoice: ").upper()
        self.student_type = input("\nSelect your level type:\nMaster (M)\nDoctorate (D)\nBoth (B0)\nChoice: ").upper()

        fix = True
        while fix:
            self.student_id = input("Enter your Student ID: ")
            for i in self.data:
                if i['stdID'] == self.student_id:
                    self.student = i
                    fix = False

    def terminateFeature(self):
        sys.exit("Goodbye!")

    def menu_manager(self):
        choice = input("Enter your Feature: ")
        system('cls')

        if choice == '1':
            system('cls')
            self.detailsFeature(self.student)
            system('pause')
        elif choice == '2':
            system('cls')
            self.statisticsFeature(self.student_level, self.student_id)
            system('pause')
        elif choice == '3':
            system('cls')
            self.majorTranscriptFeature(self.student_level, self.student_id, self.student)
            system('pause')
        elif choice == '4':
            system('cls')
            self.minorTranscriptFeature(self.student_level, self.student_id, self.student)
            system('pause')
        elif choice == '5':
            system('cls')
            self.fullTranscriptFeature(self.student_level, self.student_id, self.student)
            system('pause')
        elif choice == '6':
            system('cls')
            self.previousRequestsFeature(self.history, self.student_id)
            system('pause')
        elif choice == '7':
            system('cls')
            self.newStudentFeature()
            system('pause')
        elif choice == '8':
            system('cls')
            self.terminateFeature()
            system('pause')
        else:
            system('cls')
            print("Invalid Input!")
            system('pause')
        system('cls')
        self.menuFeature()

# TODO: REPLACE SYSTEM PAUSE WITH INPUT FUNCTION
def buffer():
    ...
# TODO: USE DIFFERENT OS COMMANDS DEPENDING ON OS
def clear_screen():
    ...

if __name__ == "__main__":
    App()

