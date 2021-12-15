c.execute("CREATE TABLE IF NOT EXISTS sales ({})".format(' ,'.join(df.columns))

for row in df.iterrows():
    sql = 'INSERT INTO salesdata ({}) VALUES ({})'.format(' ,'.join(df.columns), ','.join([?]*len(df.columns)))
    c.execute(sql, tuple(row[1]))
conn.commit()

################

try:
    # create connection
except Exception as err:
    # print error
else:
    # print(conn.version)
    try:
        cur = conn.cursor()
        sql_insert = """ """
        cur.execute(sql_insert)
    except Exception as err
        print('Error while inserting', err)
    else:
        print('Insert done')
        conn.commit()
finally:
    cur.close()
    conn.close()
