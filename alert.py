#!/usr/bin/env python3

import psycopg2
import os
import sys
from connector import Connectors

conn = None

try:
    conn = psycopg2.connect(os.environ.get('MZ_CONNECTION'))
    client = Connectors()

    with conn.cursor() as cur:
        cur.execute("set schema = test_failure")
        cur.execute("BEGIN")
        # cur.execute("DECLARE correctness CURSOR FOR SUBSCRIBE correctness_user_organization_view")
        cur.execute("DECLARE completness CURSOR FOR SUBSCRIBE completness_user_organization_view")
        while True:
            cur.execute("FETCH ALL completness")
            for row in cur:
                print("completness: ", row)
                # Alerting take place from now
                client.slack_notify("completness", row[2])
                client.prom_counter(row[1])

except Exception as e:
    print("Error:", e)

finally:
    if conn is not None:
        conn.close()
        sys.exit(0)
