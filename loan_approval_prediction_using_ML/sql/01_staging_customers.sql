-- Create staging_customers table
CREATE TABLE staging_customers AS(
	SELECT DISTINCT
		ROW_NUMBER() OVER() AS customer_id,
		loan_id,
		gender,
	    married,
	    education,
	    dependents
	FROM loan_approval_prediction_raw AS raw_data
	ORDER BY customer_id ASC
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
