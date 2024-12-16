SELECT C.CAR_ID, C.CAR_TYPE, (C.DAILY_FEE * ((100 - D.DISCOUNT_RATE) / 100 )) * 30 AS FEE
FROM (
	SELECT A.CAR_ID, A.CAR_TYPE, A.DAILY_FEE
	FROM CAR_RENTAL_COMPANY_CAR A
	WHERE A.CAR_ID NOT IN (
		SELECT CAR_ID
		FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
		WHERE TO_CHAR(START_DATE, 'YYYYMMDD') <= '20221130' AND TO_CHAR(END_DATE, 'YYYYMMDD') >= '20221101'
	)
	AND A.CAR_TYPE IN ('세단', 'SUV')
) C, CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
WHERE C.CAR_TYPE = D.CAR_TYPE
AND D.DURATION_TYPE LIKE '30%'
AND (C.DAILY_FEE * ((100 - D.DISCOUNT_RATE) / 100)) * 30 BETWEEN 500000 AND 2000000
ORDER BY FEE DESC, C.CAR_TYPE, C.CAR_ID DESC;