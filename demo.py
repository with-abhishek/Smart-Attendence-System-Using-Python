import pymysql
conn = pymysql.connect(host="localhost", user="root", password="3121", database="facerecognizer")
mycursor = conn.cursor()
mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    "iejcd",
                    "eijfc",
                    "ncecole",
                    "ermfoc",
                    "efnco",
                    "ceomco",
                    "cevvbr"
                ))
conn.commit()
conn.close()

CREATE TABLE student (
  Dep varchar(50) DEFAULT NULL,
  Course varchar(50) DEFAULT NULL,
  Year varchar(50) DEFAULT NULL,
  Semester varchar(50) DEFAULT NULL,
  StudentId varchar(45) NOT NULL,
  Name varchar(50) DEFAULT NULL,
  Division varchar(50) DEFAULT NULL,
  Roll varchar(50) DEFAULT NULL,
  Gender varchar(50) DEFAULT NULL,
  DOB varchar(50) DEFAULT NULL,
  Email varchar(50) DEFAULT NULL,
  Phone varchar(20) DEFAULT NULL,
  Address varchar(50) DEFAULT NULL,
  Teacher varchar(50) DEFAULT NULL,
  PhotoSamle varchar(50) DEFAULT NULL,
  PRIMARY KEY (`StudentId`)
);