-- 코드를 입력하세요
SELECT
    AI.NAME,
    AI.DATETIME
FROM ANIMAL_INS AS AI
LEFT JOIN ANIMAL_OUTS AS AO
ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AO.DATETIME IS NULL
ORDER BY AI.DATETIME ASC
LIMIT 3; # 가장 오래 보호소에 있었던 동물 3마리만 조회 