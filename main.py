from fastapi import FastAPI
from Posts import postList
import sqlite3

app = FastAPI()

@app.get("/setup")
async def setup_database():
    try:
        conn = sqlite3.connect("pi_dbDemo.sqlite")

        conn.executescript("""
        Create Table turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            numero INTEGER 
        );
        Create Table alunos(
            id INTEGER primary key AUTOINCREMENT,
            nome TEXT,
            numero INTEGER,
            email TEXT,
            id_turm INTEGER,
            CONSTRAINT fk_at
            Foreign Key (id_turm)
            REFERENCES turmas(id)
            
        );
        Create Table professores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            numero INTEGER,
            email TEXT,
            turma INTEGER,
            id_turm INTEGER,
            CONSTRAINT fk_pt
            Foreign Key (id_turm)
            REFERENCES turmas(id)
        )
        """)

        conn.close()
    except:
        pass

@app.get("/addvalues")
async def gerir():
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    for i in ["turmas","professores","alunos"]:
