import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="비밀번호",
    database="pyDB" 
)

mc = mydb.cursor()

sql = "INSERT INTO members (name, city) VALUES (%s, %s)"
val = [('이곤','부산'),
       ('정태을','서울'),
       ('조영','부산'),
       ('김신재','서울'),
       ('구서령','부산')
      ]

mc.executemany(sql, val)

mydb.commit()

print(mc.rowcount, "개의 레코드가 입력되었습니다.")

