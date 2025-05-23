﻿
# Title
Weather Observation Station 18

# Problem
Consider $$P_1(a, b)$$ and $$P_2(c, d)$$ to be two points on a 2D plane.
* a happens to equal the minimum value in Northern Latitude(LAT_N in STATION).
* b happens to equal the minimum value in Western Longitude(LONG_W in STATION).
* c happens to equal the maximum value in Nothern Latitude(LAT_N in STATION).
* d happens to equal the maximum value in Western Longitude(LONG_W in STATION).
Query the Manhatten Distance between points P1 and P2 and round it to a scale of 4 decimal places.

**Input Format**
The **STATION** table is described as follows:
|Field|Type|
|---|---|
|ID|NUMBER|
|CITY|VARCHAR2(21)|
|STATE|VARCHAR2(2)|
|LAT_N|NUMBER|
|LONG_W|NUMBER|

where LAT_N is the northern latitude and LONG_W is the western longitude. 
