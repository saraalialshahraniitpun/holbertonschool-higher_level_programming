#!/usr/bin/python3
"""
Module that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, safe from SQL injection.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    
    # تمرير المتغير كـ tuple لتجنب الـ SQL Injection تماماً
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC;"
    cur.execute(query, (sys.argv[4],))
    
    for row in cur.fetchall():
        print(row)
        
    cur.close()
    db.close()
