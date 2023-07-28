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
            id_turm INTEGER,
            CONSTRAINT fk_pt
            Foreign Key (id_turm)
            REFERENCES turmas(id)
        )
        """)

        conn.close()
    except:
        pass

@app.get("/addaluno")
async def addaluno(nome: str, numero: int, email: str, id_turm: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    conn.execute(f"Insert into alunos (nome,numero, email, id_turm) values ('{nome}',{numero},'{email}',{id_turm})")
    conn.commit()
    conn.close()


@app.get("/addturma")
async def addturma(nome: str, numero: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    conn.execute(f"Insert into turmas (nome,numero) values ('{nome}',{numero})")
    conn.commit()
    conn.close()


@app.get("/addprofessores")
async def addprof(nome: str, numero: int, email: str, id_turm: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    conn.execute(f"Insert into professores (nome,numero, email, id_turm) values ('{nome}',{numero},'{email}',{id_turm})")
    conn.commit()
    conn.close()


@app.get("/check/turmas")
async def checkturmas():
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute("Select * from turmas")
    conn.commit()
    return cur.fetchall()


@app.get("/check/alunos")
async def checkalunos():
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute("Select * from alunos")
    conn.commit()
    return cur.fetchall()


@app.get("/check/professores")
async def checkprofessor():
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute("Select * from professores")
    conn.commit()
    return cur.fetchall()


@app.get(f"/check/alunos/{id}")
async def checkalunos(id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute(f"Select * from alunos where id ={id}")
    conn.commit()
    curry = cur.fetchall()
    conn.close()
    return curry


@app.get(f"/check/professores/{id}")
async def checkprofs(id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute(f"Select * from professores where id ={id}")
    conn.commit()
    curry = cur.fetchall()
    conn.close()
    return curry

@app.get(f"/check/turma/{id}")
async def checkturma(id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute(f"Select * from turmas where id ={id}")
    conn.commit()
    curry = cur.fetchall()
    conn.close()
    return curry


