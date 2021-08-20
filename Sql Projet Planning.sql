SELECT P1.start_date, P2.end_date
FROM Projects P1 JOIN Projects P2
    ON DATEDIFF(P2.end_date, P1.start_date) = 
            (SELECT COUNT(*)
             FROM Projects
             WHERE start_date >= P1.start_date
                 AND end_date <= P2.end_date
            )
        AND P1.start_date - 1 NOT IN (SELECT start_date FROM Projects)
        AND P2.end_date + 1 NOT IN (SELECT end_date FROM Projects)
ORDER BY DATEDIFF(P2.end_date, P1.start_date), P1.start_date