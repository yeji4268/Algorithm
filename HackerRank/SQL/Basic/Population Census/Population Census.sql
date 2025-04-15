SELECT SUM(A.population)
FROM city A, country B
WHERE A.countrycode = B.code
  AND B.continent = 'Asia'; 