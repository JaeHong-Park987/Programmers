-- 코드를 입력하세요
# 46분 25초
SELECT
    HISTORY_ID,
    CASE
        WHEN DURATION = 0 THEN DAILY_FEE * DATE
        ELSE ROUND((DAILY_FEE * (100-DISCOUNT_RATE)/100) * DATE,0)
    END FEE
FROM(
SELECT
    C1.CAR_ID,
    C1.CAR_TYPE,
    C1.DAILY_FEE,
    C2.HISTORY_ID,
    DATEDIFF(END_DATE,START_DATE)+1 AS DATE,
    CASE
        WHEN DATEDIFF(END_DATE,START_DATE) + 1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(END_DATE,START_DATE) + 1 >= 30 THEN '30일 이상'
        WHEN DATEDIFF(END_DATE,START_DATE) + 1 >= 7 THEN '7일 이상'
        ELSE 0
    END AS DURATION
FROM CAR_RENTAL_COMPANY_CAR AS C1
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS C2
ON C1.CAR_ID = C2.CAR_ID) AS C3
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C4
ON C3.CAR_TYPE = C4.CAR_TYPE AND C3.DURATION = C4.DURATION_TYPE
WHERE C3.CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC