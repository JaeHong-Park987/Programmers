-- 코드를 입력하세요
SELECT
    YEAR(OS.SALES_DATE) AS YEAR,
    MONTH(OS.SALES_DATE) AS MONTH,
    UI.GENDER,
    COUNT(DISTINCT(UI.USER_ID)) AS USERS
FROM USER_INFO AS UI
JOIN ONLINE_SALE AS OS
ON UI.USER_ID = OS.USER_ID
WHERE UI.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR,MONTH,GENDER;
