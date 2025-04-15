SELECT B.continent, FLOOR(AVG(A.population))
FROM city A, country B
WHERE A.countrycode = B.code
GROUP BY B.continent; 