-- Get all Emp_ID's that are in the Employee Table that are not in the Employment Table.

SELECT emp_id
FROM employee e
WHERE NOT EXISTS (
    SELECT
        emp_id
    FROM employment
    WHERE
        e.emp_id = employment.emp_id
);

-- # Get all Emp_ID's that are in both the Employee Table and the Employment Table.
SELECT
    emp_id
FROM employee e
INNER JOIN employment
    ON e.emp_id = employment.emp_id;

-- # Get all unique values of Emp_Profile when Emp_Country is set to India.

SELECT DISTINCT
    emp_profile
FROM employment
WHERE
    emp_country = 'India';
