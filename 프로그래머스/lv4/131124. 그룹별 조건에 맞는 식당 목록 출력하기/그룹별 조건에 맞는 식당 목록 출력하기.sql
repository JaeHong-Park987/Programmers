-- 코드를 입력하세요
SELECT
    P.MEMBER_NAME,
    R.REVIEW_TEXT,
    DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS P
JOIN REST_REVIEW AS R
ON P.MEMBER_ID = R.MEMBER_ID
WHERE P.MEMBER_ID IN (SELECT
                        MEMBER_ID
                     FROM REST_REVIEW
                     GROUP BY MEMBER_ID
                     HAVING COUNT(*) = (SELECT MAX(COUNTED)
                                        FROM (SELECT COUNT(*) AS COUNTED
                                              FROM REST_REVIEW
                                              GROUP BY MEMBER_ID) AS COUNT))
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT                                              

# SELECT
#     MEMBER_ID
# FROM REST_REVIEW
# GROUP BY MEMBER_ID
# HAVING COUNT(*) = (SELECT MAX(COUNTED)
#                    FROM (SELECT COUNT(*) AS COUNTED
#                          FROM REST_REVIEW
#                          GROUP BY MEMBER_ID) AS COUNT)