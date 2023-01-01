import psycopg2
import sys

con = None

try:

    hostname='dpg-ce1cmd6n6mpu84vrj1og-a.oregon-postgres.render.com'
    port_id='5432'
    username='db_world_happiness_report_user'
    pwd='pHPv4o2ZQ0W8hQSWSbYl0lVE1kSVz39m'
    database='db_world_happiness_report'

    con = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    cur = con.cursor()
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()