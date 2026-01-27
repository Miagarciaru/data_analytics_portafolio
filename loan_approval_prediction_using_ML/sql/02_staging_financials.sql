-- Create staging_financials table
CREATE TABLE staging_financials AS(
	SELECT
		c.customer_id,
		rd.applicant_income+rd.coapplicant_income AS total_income,
		rd.credit_history
	FROM loan_approval_prediction_raw as rd
	JOIN staging_customers AS c
	ON rd.loan_id = c.loan_id
)

-- Load tables
-- SELECT * FROM loan_approval_prediction_raw
-- SELECT * FROM staging_customers
-- SELECT * FROM staging_financials
-- SELECT * FROM staging_loans

-- Drop tables
-- DROP TABLE loan_approval_prediction_raw;
-- DROP TABLE staging_customers;
-- DROP TABLE staging_financials;
-- DROP TABLE staging_loans;
