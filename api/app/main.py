from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/db")
def test_db():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="example",
        database="mydb"
    )
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    return {"tables": tables}
