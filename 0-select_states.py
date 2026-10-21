#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # 1. الاتصال بقاعدة البيانات باستخدام المدخلات الثلاثة المُمررة من التيرمينال
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # 2. إنشاء مؤشر (Cursor) لتنفيذ أوامر واستعلامات SQL
    cursor = db.cursor()

    # 3. تنفيذ استعلام جلب الولايات مرتبة تصاعدياً حسب الـ id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # 4. جلب جميع الصفوف الناتجة وطباعتها سطراً بسطر
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # 5. إغلاق المؤشر والاتصال بقاعدة البيانات لإنهاء الموارد بأمان
    cursor.close()
    db.close()
