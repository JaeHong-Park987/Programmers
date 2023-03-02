-- 코드를 입력하세요
SELECT 
    B.n AS HOUR, 
    IFNULL(A.COUNT, 0) AS COUNT
FROM(
    SELECT 
        HOUR(DATETIME) AS HOUR,
        COUNT(*) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR
    ) A
    RIGHT JOIN(
    WITH RECURSIVE cte AS(
    SELECT 0 AS n
    UNION ALL
    SELECT n + 1 FROM cte WHERE n < 23
    )
    SELECT n FROM cte
    ) B on A.HOUR = B.n
    ORDER BY HOUR ASC;

