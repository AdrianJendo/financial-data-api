CREATE TABLE reports
(
    report_id   SERIAL UNIQUE,
    symbol      VARCHAR(5),
    start_date  date,
    end_date    date,
    filing_date date,

    PRIMARY KEY (symbol, end_date)
);

INSERT INTO reports(symbol, start_date, end_date)
VALUES ('GOOGL',
        '2017-10-29',
        '2018-10-26');

DROP TABLE reports CASCADE;

CREATE TABLE balance_sheet
(
    report_id                int REFERENCES reports (report_id) on delete cascade,
    cash                     int,
    marketable_securities    int,
    accounts_receivable      int,
    inventories              int,

    property_plant_equipment int,
    goodwill                 int,
    intangibles              int,
    total_assets             int,
    current_assets           int,
    short_term_debt          int,
    long_term_debt           int,
    accounts_payable         int,
    accrued_expenses         int,
    deferred_revenue         int,
    current_liabilities      int,
    total_liabilities        int,
    equity                   int,
    retained_earnings        int,


    PRIMARY KEY (report_id)
);

INSERT INTO balance_sheet (report_id, cash, marketable_securities, accounts_receivable, inventories)
VALUES (2, 100, 200, 300, 400);

CREATE TABLE cash_flow
(
    report_id                          int REFERENCES reports (report_id) on delete cascade,
    depr_and_amort                     int,
    stock_based_comp                   int,
    cash_from_operating_activities     int,
    cash_from_investing_activities     int,
    cash_from_financing_activities     int,
    inventories                        int,
    accounts_receivable                int,
    accounts_payable                   int,
    deferred_revenue                   int,
    capex                              int,
    purchases_of_marketable_securities int,
    sales_of_marketable_securities     int,
    cost_of_acquisition                int,
    issuance_of_debt                   int,
    payments_of_debt                   int,
    dividends                          int,
    shares_repurchased                 int,
    stock_issued                       int,
    net_increase_of_cash               int,
    cash_at_beginning                  int,
    cash_at_end                        int,
    PRIMARY KEY (report_id)
);

INSERT INTO cash_flow (report_id, depr_and_amort, stock_based_comp, cash_from_operating_activities,
                       cash_from_investing_activities, cash_from_financing_activities)
VALUES (1, 100, 200, 300, 400, 500);



CREATE TABLE income_statement
(
    report_id     int REFERENCES reports (report_id) on delete cascade,
    revenue       int,
    cost_of_sales int,
    -- gross_profit               int,
    -- r_and_d                    int,
    -- g_and_a                    int,
    -- interest_expense           int,
    -- operating_income           int,
    -- operating_expenses         int,
    -- income_before_taxes        int,
    -- taxes_paid                 int,
    -- net_income                 int,
    -- basic_shares_outstanding   int,
    -- diluted_shares_outstanding int,

    PRIMARY KEY (report_id)
);

INSERT INTO income_statement (report_id, revenue, cost_of_sales)
VALUES (1, 100000000, 200);

SELECT *
FROM reports
WHERE symbol = 'AAPL'
ORDER BY end_date DESC;

SELECT *
FROM reports
         INNER JOIN income_statement
                    ON reports.report_id = income_statement.report_id
         INNER JOIN cash_flow ON reports.report_id = cash_flow.report_id
         INNER JOIN balance_sheet ON reports.report_id = balance_sheet.report_id
WHERE reports.start_date > '2012-01-01';

DROP TABLE income_statement