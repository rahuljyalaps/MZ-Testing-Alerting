#!/usr/bin/env python3

import psycopg2
import sys

dsn = "user=rahul-jyala@pluralsight.com password=mzp_d06ecc4a7f5b48dcb2a87cd00bc9c391100009c9fb634d98a230b1e66775cc10 host=a3eldpgfddavjheax03kfzz9m.us-east-1.aws.materialize.cloud port=6875 dbname=arkenstone sslmode=require options=-csearch_path%3Dpublic,rahul"
conn = psycopg2.connect(dsn)

with conn.cursor() as cur:
    cur.execute("set schema = test_failure")
    cur.execute("DECLARE c CURSOR FOR SUBSCRIBE correctness_user_organization_view")
    while True:
        cur.execute("FETCH ALL c")
        for row in cur:
            print(row)
