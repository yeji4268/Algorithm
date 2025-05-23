﻿
# Title
The Blunder

# Problem

Samantha was tasked with calculating the average monthly salaries for all employees in the  **EMPLOYEES**  table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: $$actual - miscalculated$$ average monthly salaries), and round it up to the next integer.

**Input Format**
The **EMPLOYEES** table is described as follows:<br>
|Column|Type|
|---|---|
|ID|Integer|
|Name|String|
|Salary|Integer|

**Note**: Salary is per month.

**Constraints**
$$1000 < Salary < 10^5$$

**Sampel Input**
|ID|Name|Salary|
|---|---|---|
|1|Kristeen|1420|
|2|Ashley|2006|
|3|Julia|2210|
|4|Maria|3000|

**Sample Output**
``
2061
``
