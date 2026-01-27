CREATE TABLE IF NOT EXISTS loan_approval_prediction_raw(
	loan_id TEXT,
    gender TEXT,
    married TEXT,
    dependents NUMERIC,
    education TEXT,
    self_employed TEXT,
    applicant_income NUMERIC,
    coapplicant_income NUMERIC,
    loan_amount NUMERIC,
    loan_amount_term NUMERIC,
    credit_history INTEGER,
    property_area TEXT,
    loan_status TEXT
);

COPY loan_approval_prediction_raw
FROM '/home/miagarciaru/Documents/portafolio_data_analytics/loan_approval_prediction_using_ML/data/raw/LoanApprovalPrediction.csv' 
DELIMITER ',' 
CSV HEADER;

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