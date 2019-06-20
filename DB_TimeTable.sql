CREATE TABLE it4 (
    id serial PRIMARY KEY,
    mon VARCHAR NOT NULL,
    tue VARCHAR NOT NULL,
    wed VARCHAR NOT NULL,
    thu VARCHAR NOT NULL,
    fri VARCHAR NOT NULL,
    sat VARCHAR NOT NULL
);


INSERT INTO it4 (mon, tue, wed, thu, fri, sat)
VALUES
    ('CM', 'AEC', 'OOCP', 'DSAA', 'AEC', 'AEC/DSAA LAB'),
    ('TSCN', 'OOCP', 'OOCP', 'COA', 'COA', 'AEC/DSAA LAB'),
    ('TSCN', 'CM', 'COA', 'AEC', 'AEC/DSAA LAB', 'TSCN'),
    ('DSAA', 'DSAA', 'COA', 'CM', 'AEC/DSAA LAB', 'OOCP'),
    ('AEC', 'OOCP LAB', 'CM', 'TSCN LAB', 'TSCN', 'N/A'),
    ('AEC', 'OOCP LAB', 'TSCN', 'TSCN LAB', 'DSAA', 'N/A'),
    ('OOCP', 'OOCP LAB', 'DSAA', 'TSCN LAB', 'CM', 'N/A');