#!/usr/bin/env python3

import psycopg2
from connector import slack_notify_new_order

dsn = "mocked"
conn = psycopg2.connect(dsn)

with conn.cursor() as cur:
    cur.execute("set schema = test_failure")
    cur.execute("DECLARE c CURSOR FOR SUBSCRIBE correctness_user_organization_view")
    while True:
        cur.execute("FETCH ALL c")
        for row in cur:
            print(row)

# slack_notify_new_order(1, 'RahulJyala', 100)