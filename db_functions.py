import os
from pathlib import Path
from dotenv import load_dotenv
import sqlite3

#loading .env
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

DATABASE = os.getenv('DATABASE')
#SQLite Database
conn = sqlite3.connect(DATABASE)
sql_cursor = conn.cursor()

def listroles():
    sql = "SELECT * FROM roles"
    sql_cursor.execute(sql)
    roles = sql_cursor.fetchall()
    return roles

def listvideos():
    sql = "SELECT * FROM videos"
    sql_cursor.execute(sql)
    videos = sql_cursor.fetchall()
    return videos

def get_video(name):
    sql = "SELECT * FROM videos WHERE name=?"
    sql_cursor.execute(sql, [name])
    videos = sql_cursor.fetchall() 
    return videos

def list_video_names():
    sql = "SELECT * FROM videos"
    sql_cursor.execute(sql)
    videos = sql_cursor.fetchall()
    video_names = []
    names = ''
    for v in videos:
        video_names.append(v[0])
    video_names = list(dict.fromkeys(video_names))
    for name in video_names:
        if not names:
            names = name
        else:
            names = names + ', ' + name       
    return names

def get_role(role):
    role_available = -1
    sql = "SELECT * FROM roles"
    sql_cursor.execute(sql)
    roles = sql_cursor.fetchall()
    for r in roles:
        if role == r[0]:
            role_available = 1   
    return role_available 

#def add_role(role):
    
#def remove_role(role):
    