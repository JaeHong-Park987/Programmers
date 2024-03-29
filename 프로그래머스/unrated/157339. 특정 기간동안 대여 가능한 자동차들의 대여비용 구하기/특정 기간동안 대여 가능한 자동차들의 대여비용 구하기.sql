-- 코드를 입력하세요
SELECT
    CAR_ID,
    CAR_TYPE,
    FEE
FROM(
SELECT
    DISTINCT(C1.CAR_ID),
    C1.CAR_TYPE,
    ROUND(DAILY_FEE * 30 * (100-DISCOUNT_RATE) * 0.01,0) AS FEE,
    DISCOUNT_RATE
FROM CAR_RENTAL_COMPANY_CAR AS C1
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS C3
ON C1.CAR_TYPE = C3.CAR_TYPE AND DURATION_TYPE = '30일 이상'
WHERE C1.CAR_TYPE = 'SUV' OR C1.CAR_TYPE = '세단'
) AS C
WHERE C.FEE BETWEEN 500000 AND 2000000
AND CAR_ID NOT IN(SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE DATE_FORMAT(END_DATE,'%Y-%m-%d') > '2022-11-01')
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC