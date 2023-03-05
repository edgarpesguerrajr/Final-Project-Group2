# Transcript Generation System

#### Description: A menu-driven program with a command line interface (CLI) that prints and generates transcripts of a student into text files.

#### Submitted as Lab Final Project in the Polytechnic University of the Philippines - Sta. Mesa - A.Y. 2022-2023 in the course CMPE 30052 - Data Structures and Algorithm

---

> Student Transcript Generation System

![Menu Feature](/img/menu-feature.PNG)

---

### Table of Contents

- [Description]()
    - [Technologies]()
- [How to Use]()
    - [Installation]()
    - [Configuration]()
- [Features]()
    - [Start Feature]()
    - [Menu Feature]()
    - [Details Feature]()
    - [Statistics Feature]()
    - [Major Transcript Feature]()
    - [Minor Transcript Feature]()
    - [Full Transcript Feature]()
    - [Previous Requests Feature]()
    - [New Student Feature]()
    - [Terminate Feature]()
- [Credits and References]()
- [Authors Info]()

---

## Description

A menu-driven program with a command line interface (CLI) that prints and generates transcripts of a student into text files. Registered students are listed in a CSV file with the filename 'studentDetails.csv'. Each student has another CSV file with a filename of their student ID (e.g., 2021-05794-MN-0.csv) where their grades are listed. The program reads and filters information in the CSV files based on the student information given by the user. Each request creates a text file where the information requested is saved. Each request is recorded in history via the 'previous requests feature' with a date and time in which the request was made.

#### Technologies

- Python 3.10

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

#### Configuration

- **To edit the students enrolled/registered:**
    - Open studentDetails.csv in the 'program' directory.
    - Feel free to edit the values however, the following format must be followed.
        - Level must only be U or G. (undergraduate or graduate)
        - Degree must only be BS, M, or D, but digits after it is allowed. (bachelor, master, or degree)
        - Degrees of undergraduates (U) must be bachelor (BS).
        - Degrees of graduates (G) can either be master, or doctorate (M or D).
        - Terms must be an integer.

- **To edit the grades of students:**
    - In the 'program' directory, rename \<student ID>.csv to the new student ID registered in studentDetails.csv. (Make sure the filename of the CSV is exactly the student ID registered in studentDetails.csv)
    - Open the \<student ID>.csv.
    - Feel free to edit the values however, the following format must be followed.
        - Level must only be U or G. (undergraduate or graduate)
        - Degree must only be BS, M, or D, but digits after it is allowed. (bachelor, master, or degree)
        - courseType can only be Major or Minor.
        - term, creditHours, and Grade must be an integer.

- **Make sure that all student information in studentDetails.csv matches the information in their own CSV. (\<student ID>.csv)**.

---

## Features

- #### Start Feature

Acts as a log in system of the program. Prompts user for student level (U, G, or B). Automatically assign bachelor (BS) as the degree if undergraduate (U). If graduate (G), prompts for student degree (M, D, B0). Finally, prompts for student ID. The program checks user inputs validity. If input is, invalid the program prompts again until a valid input is given. As a last validity check, the program ensures that the given student information exists in studentDetails.csv. If the student indeed exists in, then redirects to main menu (menu feature).

![Start Feature](/img/start-feature.PNG)

- #### Menu Feature

Acts as the main menu of the program. Users will only reach the main menu after successfully logging in via start feature. Shows all available option/feature. Prompts user for a feature choice, then redirect to that feature. The program checks for validity. If given feature choice is invalid, then the program informs that it is invalid, and redirect to main menu.

![Menu Feature](/img/menu-feature.PNG)


- #### Details Feature

Shows details about the student that logged in. Details shown includes name, student ID, level(s), number of terms, college(s), and department(s). These data are from studentDetails.csv.

![Details Feature](/img/details-feature.PNG)

- #### Statistics Feature

Shows statistics about the student's record. The statistics information are divided into student levels. If the student logged in as both (B), and the student is indeed registered with both undergraduate (U) and graduate (G), then the statistics shown will be for undergraduate (U) and graduate (G) separately. On the other hand, if the student logged in as only one level or the student is registered with only one level, then the statistics shown will only be for the chosen level.

Statistics information shown includes the overall average for all terms, the average for each term, the maximum grade and in which term(s), and the minimum grade and in which term(s). The data are from the CSV containing the student record/grade with the title name of \<student ID>.csv.


![Statistics Feature](/img/statistics-feature.PNG)

- #### Major Transcript Feature

Shows the transcript of the student based on major courses and the selected level and degree when logging in. The major transcript is divided into terms.

General information are shown at the top. It includes name, student ID, college(s), department(s), number of major courses, number of minor courses, level(s), and number of terms. After the general information, the courses per term are shown. Each courses in a term includes course ID, course name, credit hours, and grade. Each term shows the overall average of all major courses, and the average of all major courses in that term. In cases where the term do not have a major course (only minor course), then it will be be blank with a message saying that there is no registered major course in that term.

![Major Transcript Feature](/img/major-transcript-feature.PNG)

- #### Minor Transcript Feature

It works exactly the same as major transcript, only difference is that it only considers minor courses. It shows the transcript of the student based on minor courses and the selected level and degree when logging in. The minor transcript is divided into terms.

General information are shown at the top. It includes name, student ID, college(s), department(s), number of major courses, number of minor courses, level(s), and number of terms. After the general information, the courses per term are shown. Each courses in a term includes course ID, course name, credit hours, and grade. Each term shows the overall average of all minor courses, and the average of all minor courses in that term. In cases where the term do not have a minor course (only major course), then it will be be blank with a message saying that there is no registered minor course in that term.

![Minor Transcript Feature](/img/minor-transcript-feature.PNG)

- #### Full Transcript Feature

It works exactly the same as major, and minor transcript, only difference is that it only considers both major and minor courses (in other words, all courses). It shows the transcript of the student based on the selected level and degree when logging in. The full transcript is divided into terms.

General information are shown at the top. It includes name, student ID, college(s), department(s), number of major courses, number of minor courses, level(s), and number of terms. After the general information, the courses per term are shown. Each courses in a term includes course ID, course name, credit hours, and grade. Each term shows the overall average of all courses, and the average of all courses in that term. In cases where the term do not have a any course, then it will be be blank with a message saying that there is no registered course in that term.

![Full Transcript Feature](/img/full-transcript-feature.PNG)

- #### Previous Requests Feature

![Previous Requests Feature](/img/previous-requests-feature.PNG)

- #### New Student Feature

![New Student Feature](/img/new-student-feature.PNG)

- #### Terminate Feature

![Terminate Feature](/img/terminate-feature.PNG)

---

## Credits and References

---

## Authors Info
- Github - [Siegfred Lorelle Mina](https://github.com/SiegfredLorelle)
- Github - [Edgar Esguerra Jr.](https://github.com/edgarpesguerrajr)
- Github - [Shin Lim](https://github.com/ShinayLim) & [Shin Lim](https://github.com/shinlim12)
- Github - [Kenji Ilao](https://github.com/KenjiIlao)


<!-- TODO: Add go back to top -->
<!-- TODO: Features -->
<!-- TODO: Credit the pdf -->
<!-- TODO: TOC link to parts -->
<!-- TODO: TEST -->



