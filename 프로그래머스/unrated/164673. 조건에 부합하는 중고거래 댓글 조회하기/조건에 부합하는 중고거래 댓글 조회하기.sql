-- 코드를 입력하세요
SELECT
    UGB.TITLE,
    UGB.BOARD_ID,
    UGR.REPLY_ID,
    UGR.WRITER_ID,
    UGR.CONTENTS,
    DATE_FORMAT(UGR.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS UGB JOIN USED_GOODS_REPLY AS UGR ON UGB.BOARD_ID = UGR.BOARD_ID
WHERE UGB.CREATED_DATE LIKE '2022-10%'
ORDER BY UGR.CREATED_DATE ASC, UGB.TITLE ASC;