# Transcript Generation System

#### Description: A menu-driven program with a command line interface (CLI) that prints and generates transcripts of a student into text files.

#### Submitted as Lab Final Project in the Polytechnic University of the Philippines - Sta. Mesa - A.Y. 2022-2023 in the course CMPE 30052 - Data Structures and Algorithm

---

<!-- PICTURE HERE -->

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
    - In the 'program' directory, rename \<studentID>.csv to the new student ID registered in studentDetails.csv. (Make sure the filename of the CSV is exactly the student ID registered in studentDetails.csv)
    - Open the \<studentID>.csv.
    - Feel free to edit the values however, the following format must be followed.
        - Level must only be U or G. (undergraduate or graduate)
        - Degree must only be BS, M, or D, but digits after it is allowed. (bachelor, master, or degree)
        - courseType can only be Major or Minor.
        - term, creditHours, and Grade must be an integer.
- **Make sure that all student information in studentDetails.csv matches the information in their own CSV. (\<studentID>.csv)**.

---

## Features

#### Start Feature
Prompts user for student level (U, G, or B). Automatically assign bachelor (BS) as the degree if undergraduate (U). If graduate, prompts for student degree (M, D, B0). Finally, prompts for student ID. The program checks user inputs validity. If input is, invalid the program prompts again until a valid input is given. As a last validity check, the program ensures that the given student information exists in studentDetails.csv.

![Start Feature](/img/start-feature.PNG)

#### Menu Feature

![Menu Feature](/img/menu-feature.PNG)


#### Details Feature

![Details Feature](/img/details-feature.PNG)

#### Statistics Feature

![Statistics Feature](/img/statistics-feature.PNG)

#### Major Transcript Feature

![Major Transcript Feature](/img/major-transcript-feature.PNG)

#### Minor Transcript Feature

![Minor Transcript Feature](/img/minor-transcript-feature.PNG)

#### Full Transcript Feature

![Full Transcript Feature](/img/full-transcript-feature.PNG)

#### Previous Requests Feature

![Previous Requests Feature](/img/previous-requests-feature.PNG)

#### New Student Feature

![New Student Feature](/img/new-student-feature.PNG)

#### Terminate Feature

![Terminate Feature](/img/terminate-feature.PNG)

---

## Credits and References

---

## Authors Info
- Github - [Siegfred Lorelle Mina](https://github.com/SiegfredLorelle)
- Github - [Edgar Esguerra Jr.](https://github.com/edgarpesguerrajr)
- Github - [Shin Lim](https://github.com/ShinayLim) & [Shin Lim](https://github.com/shinlim12)
- Github - [Kenji Ilao](https://github.com/KenjiIlao)




