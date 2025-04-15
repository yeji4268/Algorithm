SELECT A.name
FROM city A, country B
WHERE A.countrycode = B.code 
  AND B.continent = 'Africa';