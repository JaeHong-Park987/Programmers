-- 코드를 입력하세요
# 중복을 제거해야할 때는 GROUP BY 대신 DISTINCT 사용해보자!!!
SELECT
    CRCC.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS CRCC
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CRCRH
ON CRCC.CAR_ID = CRCRH.CAR_ID
WHERE CRCC.CAR_TYPE = '세단'
AND MONTH(START_DATE) = 10
GROUP BY CRCC.CAR_ID
ORDER BY CRCC.CAR_ID DESC;