CREATE TABLE reports
(
    report_id  SERIAL UNIQUE,
    symbol     VARCHAR(5),
    start_date date,
    end_date   date,
    report_date date,

    PRIMARY KEY (symbol, end_date)
);

INSERT INTO reports(symbol, start_date, end_date)
VALUES ('CRM',
        '2017-10-29',
        '2018-10-26');

DROP TABLE reports CASCADE ;

CREATE TABLE balance_sheet
(
    report_id             int REFERENCES reports (report_id) on delete cascade,
    cash                  int,
    marketable_securities int,
    accounts_receivable   int,
    inventories           int,
    PRIMARY KEY (report_id)
);

INSERT INTO balance_sheet (report_id, cash, marketable_securities, accounts_receivable, inventories)
VALUES (2, 100, 200, 300, 400);

CREATE TABLE cash_flow
(
    report_id                      int REFERENCES reports (report_id) on delete cascade,
    depr_and_amort                 int,
    stock_based_comp               int,
    cash_from_operating_activities int,
    cash_from_investing_activities int,
    cash_from_financing_activities int,
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
    gross_profit  int,
    PRIMARY KEY (report_id)
);

INSERT INTO income_statement (report_id, revenue, cost_of_sales, gross_profit)
VALUES (3, 100000000, 200, 300);

SELECT *
FROM reports
WHERE symbol = 'AAPL'
ORDER BY end_date DESC;