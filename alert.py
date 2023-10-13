#!/usr/bin/env python3

import psycopg2
import os
from connector import slack_notify_new_order

conn = psycopg2.connect(os.environ.get('MZ_CONNECTION'))

with conn.cursor() as cur:
    cur.execute("set schema = test_failure")
    cur.execute("DECLARE c CURSOR FOR SUBSCRIBE correctness_user_organization_view")
    while True:
        cur.execute("FETCH ALL c")
        for row in cur:
            print(row)

# slack_notify(1, 'RahulJyala', 100)