-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS,
(CASE
    WHEN FREEZER_YN IS NULL THEN 'N'
    ELSE FREEZER_YN
 END) AS 'FREEZER_YN'
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID;

# IFNULL함수 활용 해보기!!
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') AS 'FREEZER_YN'
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID;
# IF 함수 활용해보기!!