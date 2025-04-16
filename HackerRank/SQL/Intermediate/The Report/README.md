
# Title
The Report

# Problem
You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks.
|Column|Type|
|---|---|
|ID|Integer|
|Name|String|
|Marks|Integer|

Grades contains the following data:
_Ketty_  gives  _Eve_  a task to generate a report containing three columns:  _Name_,  _Grade_  and  _Mark_.  _Ketty_  doesn't want the NAMES of those students who received a grade lower than  _8_. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

Write a query to help Eve.
**Note**

Print "NULL" as the name if the grade is less than 8.

**Explanation**

Consider the following table with the grades assigned to the students:
So, the following students got  _8_,  _9_  or  _10_  grades:

-   _Maria (grade 10)_
-   _Jane (grade 9)_
-   _Julia (grade 9)_
-   _Scarlet (grade 8)_
