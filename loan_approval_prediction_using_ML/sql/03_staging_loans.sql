-- Create staging_loans table
CREATE TABLE staging_loans AS(
	SELECT
	    c.customer_id,
	    rd.loan_id,
		rd.loan_amount,
	    rd.loan_amount_term,
	    rd.loan_status
	FROM loan_approval_prediction_raw AS rd
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