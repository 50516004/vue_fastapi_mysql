from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 許可するオリジン
    allow_credentials=True,  # Cookieなどの認証情報を許可
    allow_methods=["*"],  # 許可するHTTPメソッド
    allow_headers=["*"],  # 許可するHTTPヘッダー
)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/db")
def test_db():
    conn = mysql.connector.connect(
        host="db", user="root", password="root", database="mydb"
    )
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    return {"tables": tables}


@app.get("/users")
def read_users():
    conn = mysql.connector.connect(
        host="db", user="root", password="root", database="mydb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    return users

@app.get("/users/{user_id}")
def read_user_by_id(user_id: int):
    conn = mysql.connector.connect(
        host="db", user="root", password="root", database="mydb"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE id = {user_id}")
    user = cursor.fetchall()
    return user
