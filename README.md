# Transcript Generation System

#### Description: A menu-driven program with a command line interface (CLI) that prints and generates transcripts of a student into text files.

#### Submitted as Lab Final Project in the Polytechnic University of the Philippines - Sta. Mesa - A.Y. 2022-2023 in the course CMPE 30052 - Data Structures and Algorithm

---

> Student Transcript Generation System

![Menu Feature](/img/menu-feature.PNG)

---

### Table of Contents

- [Description](#description)
    - [Technologies](#technologies)
- [How to Use](#how-to-use)
    - [Installation](#installation)
    - [Configuration](#configuration)
- [Features](#features)
    - [Start Feature](#start-feature)
    - [Menu Feature](#menu-feature)
    - [Details Feature](#details-feature)
    - [Statistics Feature](#statistics-feature)
    - [Major Transcript Feature](#major-transcript-feature)
    - [Minor Transcript Feature](#minor-transcript-feature)
    - [Full Transcript Feature](#full-transcript-feature)
    - [Previous Requests Feature](#previous-requests-feature)
    - [New Student Feature](#new-student-feature)
    - [Terminate Feature](#terminate-feature)
- [Credits and References](#credits-and-references)
- [Authors Info](#authors-info)

---

## Description

A menu-driven program with a command line interface (CLI) that prints and generates transcripts of a student into text files. Registered students are listed in a CSV file with the filename 'studentDetails.csv'. Each student has another CSV file with a filename of their student ID (e.g., 2021-05794-MN-0.csv) where their grades are listed. The program reads and filters information in the CSV files based on the student information given by the user. Each request creates a text file where the information requested is saved. Each request is recorded in history via the 'previous requests feature' with a date and time in which the request was made.

#### Technologies

- Python 3.10

[Back to the Top](#transcript-generation-system)

---

## How to Use

#### Installation

- Fork [this repository](https://github.com/edgarpesguerrajr/transcript-generation-system). [(Not sure how?)](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
- Install [python](https://www.python.org/downloads/).
- Try running the command below on the 'program' directory (where main.py is saved.)
    - For Windows and Mac:
        ```
        python main.py
        ```
    - For Linux:
        ```
        # 'python3' might be different if on a newer version of python
        python3 main.py
        ```
- If an error occurs, try following the steps again.

[Back to the Top](#transcript-generation-system)

#### Configuration

- **To edit the students enrolled/registered:**
    - Open studentDetails.csv in the 'program' directory.
    - Feel free to edit the values. However, the following format must be followed.
        - Level must only be U or G. (undergraduate or graduate)
        - Degree must only be BS, M, or D, but digits after it is allowed. (bachelor, master, or degree)
        - Degrees of undergraduates (U) must be bachelor (BS).
        - Degrees of graduates (G) can either be master, or doctorate (M or D).
        - Terms must be an integer.

- **To edit the grades of students:**
    - In the 'program' directory, rename \<student ID>.csv to the new student ID registered in studentDetails.csv. (Make sure the filename of the CSV is exactly the student ID registered in studentDetails.csv)
    - Open the \<student ID>.csv.
    - Feel free to edit the values. However, the following format must be followed.
        - Level must only be U or G. (undergraduate or graduate)
        - Degree must only be BS, M, or D, but digits after it is allowed. (bachelor, master, or degree)
        - courseType can only be Major or Minor.
        - term, creditHours, and Grade must be an integer.

- **Make sure that all student in the studentDetails.csv has their own CSV (\<student ID>.csv), and that the information in both CSV files match.**

[Back to the Top](#transcript-generation-system)

---

## Features

Note that all of the features/requests, except for change student, and terminate will generate a text file containing the data requested. In instances where the text file is already generated, then the text file will be rewritten.

- #### Start Feature

Acts as a login system. Prompts the user for student level (U, G, or B). If undergraduate (U), bachelor (BS) is automatically assigned as a degree. If graduate (G), prompts for student degree (M, D, B0). Finally, prompts for student ID. The program checks the validity of the user input. If the input is, invalid the program prompts again until a valid input is given. As a last validity check, the program ensures that the given student information exists in studentDetails.csv. If the student indeed exists, then redirect to the main menu (menu feature).

![Start Feature](/img/start-feature.PNG)

[Back to the Top](#transcript-generation-system)

- #### Menu Feature

Acts as the main menu of the program. Users will only reach the main menu after successfully logging in via the start feature. Shows all available option/feature. Prompts the user for a feature choice, then redirect to that feature. The program checks for validity. If the given feature choice is invalid, then the program informs that it is invalid, and redirects to the main menu.


![Menu Feature](/img/menu-feature.PNG)

[Back to the Top](#transcript-generation-system)

- #### Details Feature

Shows details about the student that logged in. Details shown include name, student ID, level(s), number of terms, college(s), and department(s). These data are from studentDetails.csv.

![Details Feature](/img/details-feature.PNG)

[Back to the Top](#transcript-generation-system)

- #### Statistics Feature

Shows statistics about the student's record. The statistics information is divided into student levels. If the student logged in as both (B), and the student is indeed registered with both undergraduate (U) and graduate (G), then the statistics shown will be for undergraduate (U) and graduate (G) separately. On the other hand, if the student logged in as only one level or the student is registered with only one level, then the statistics shown will only be for the chosen level.

Statistics information shown includes the overall average for all terms, the average for each term, the maximum grade and in which term(s), and the minimum grade and in which term(s). The data are from the CSV containing the student record/grade with the title name of \<student ID>.csv.


![Statistics Feature](/img/statistics-feature.PNG)

[Back to the Top](#transcript-generation-system)

- #### Major Transcript Feature

Shows the transcript of the student based on major courses and the selected level and degree when logging in. The major transcript is divided into terms.

General information is shown at the top. It includes name, student ID, college(s), department(s), number of major courses, number of minor courses, level(s), and number of terms. After the general information, the courses per term are shown. Each course in a term includes course ID, course name, credit hours, and grade. Each term shows the overall average of all major courses and the average of all major courses in that term. In cases where the term does not have a major course (only minor courses), then it will be blank with a message saying that there is no registered major course in that term. The data are from the CSV containing the student record/grade with the title name of <student ID>.csv.

![Major Transcript Feature](/img/major-transcript-feature.PNG)

[Back to the Top](#transcript-generation-system)

- #### Minor Transcript Feature

It works exactly the same as the major transcript, the only difference is that it only considers minor courses. It shows the transcript of the student based on minor courses and the selected level and degree when logging in. The minor transcript is divided into terms.

General information is shown at the top. It includes name, student ID, college(s), department(s), number of major courses, number of minor courses, level(s), and number of terms. After the general information, the courses per term are shown. Each course in a term includes course ID, course name, credit hours, and grade. Each term shows the overall average of all minor courses and the average of all minor courses in that term. In cases where the term does not have a minor course (only major courses), then it will be blank with a message saying that there is no registered minor course in that term. The data are from the CSV containing the student record/grade with the title name of <student ID>.csv.

![Minor Transcript Feature](/img/minor-transcript-feature.PNG)

[Back to the Top](#transcript-generation-system)

- #### Full Transcript Feature

It works exactly the same as major, and minor transcript, the only difference is that it only considers both major and minor courses (in other words, all courses). It shows the transcript of the student based on the selected level and degree when logging in. The full transcript is divided into terms.

General information is shown at the top. It includes name, student ID, college(s), department(s), number of major courses, number of minor courses, level(s), and number of terms. After the general information, the courses per term are shown. Each course in a term includes course ID, course name, credit hours, and grade. Each term shows the overall average of all courses and the average of all courses in that term. In cases where the term does not have any course, then it will be blank with a message saying that there is no registered course in that term. The data are from the CSV containing the student record/grade with the title name of <student ID>.csv.

![Full Transcript Feature](/img/full-transcript-feature.PNG)

[Back to the Top](#transcript-generation-system)

- #### Previous Requests Feature

Shows all requests made by the user/student accompanied by a date and time in which the request was made. Requests that are recorded are details, statistics, major transcript, minor transcript, and full transcript. All of the requests mentioned will be recorded here. The previous requests of the student are saved across sessions because it is saved via a text file.

![Previous Requests Feature](/img/previous-requests-feature.PNG)

[Back to the Top](#transcript-generation-system)

- #### New Student Feature

Acts as the log-out system. Clear all information recorded from the previous students (requested information is still saved via text files) to give space for the new student. With space for the new student, prompt for student information of the new student. Student information prompted are student level degree, and student ID (works exactly as the login system in the start feature). The validity of inputs is checked. If the inputs are indeed valid then the login is successful so redirect to the main menu.

![New Student Feature](/img/new-student-feature.PNG)

[Back to the Top](#transcript-generation-system)

- #### Terminate Feature

Acts as the close/exit of the program. Before terminating the program, the number of requests across all students in that particular session is shown. The request includes details, statistics, major transcript, minor transcript, full transcript, and previous requests.

![Terminate Feature](/img/terminate-feature.PNG)

[Back to the Top](#transcript-generation-system)

---

## Credits and References

- All specifications and functionality of each feature are based on the PDF with the filename 'CMPE 30052 Lab Project Transcript Generation System.pdf'
- Data on the CSV files are fabricated and are not based on real people's information and/or grades.

[Back to the Top](#transcript-generation-system)

---

## Authors Info
- Github - [Siegfred Lorelle Mina](https://github.com/SiegfredLorelle)
- Github - [Edgar Esguerra Jr.](https://github.com/edgarpesguerrajr)
- Github - [Shin Lim](https://github.com/ShinayLim) & [Shin Lim](https://github.com/shinlim12)
- Github - [Kenji Ilao](https://github.com/KenjiIlao)

[Back to the Top](#transcript-generation-system)