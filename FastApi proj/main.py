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
            id INTEGER primary key AUTOINCREMENT,
            nome TEXT,
            numero INTEGER
        );
        
        Create Table alunos(
            id INTEGER primary key AUTOINCREMENT,
            nome TEXT,
            numero INTEGER,
            email TEXT,
            turma_id INTEGER,
            CONSTRAINT fk_aluno_turma
            FOREIGN KEY (turma_id)
            REFERENCES turmas(id)
        );
        
        Create Table professores(
            id INTEGER primary key AUTOINCREMENT,
            nome TEXT,
            numero INTEGER,
            email TEXT,
            turma_id INTEGER,
            CONSTRAINT fk_professor_turma
            FOREIGN KEY (turma_id)
            REFERENCES turmas(id)
        );
        """)

        conn.close()
        return "success"
    except Exception as error:
        return str(error)

@app.get("/addteste")
async def addteste():
    conn = sqlite3.connect("pi_dbDemo.sqlite")

    conn.execute("""INSERT INTO turmas(nome, numero) VALUES ('PI0921', 10);""")

    conn.execute("""INSERT INTO alunos(nome, numero, email, turma_id) VALUES ('Sofia Lopes', 25, 'sofia.lopes@edu.atec.pt', 1);""")

    conn.execute("""INSERT INTO professores(nome, numero, email, turma_id) VALUES ('Mario Luis', 52, 'mario.luis@edu.atec.pt', 1);""")

    conn.commit()

    conn.close()

@app.get("/checkall")
async def checkall():
    conn = sqlite3.connect("pi_dbDemo.sqlite")

    allTables = []
    cur = conn.cursor()

    for table in ["turmas", "alunos", "professores"]:
        cur.execute(f"SELECT * from {table};")
        allTables.append(cur.fetchall())

    conn.close()

    return {"allTables" : allTables}

@app.get("/check/turmas")
async def checkturmas():
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute("Select * from turmas")
    conn.commit()
    curry = cur.fetchall()
    conn.close()
    return curry

@app.get("/check/turmas/{id}")
async def checkturma(id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute(f"Select * from turmas where id ={id}")
    conn.commit()
    curry = cur.fetchall()
    conn.close()
    return curry

@app.get("/addturma")
async def addturma(nome: str, num: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")

    sql = f"""INSERT INTO turmas(nome, numero) VALUES ('{nome}', {num});"""

    conn.execute(sql)

    conn.commit()

    conn.close()

    print(sql)

@app.get("/changeturma")
async def changeturma(id: int, nome: str = None, num: int = None):

    if nome == None and num == None:
        return "null"

    conn = sqlite3.connect("pi_dbDemo.sqlite")

    sql = ""

    if nome != None:
        sql = f"""UPDATE turmas set nome = '{nome}' where id = {id};"""

    if num != None:
        sql = f"""UPDATE turmas set numero = {num} where id = {id};"""

    conn.execute(sql)

    conn.commit()

    conn.close()

    print(sql)

@app.get("/remove/turmas/{id}")
async def delturma(id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")

    conn.execute(f"delete from turmas where id = {id};")

    conn.commit()

    conn.close()

@app.get("/check/alunos")
async def checkalunos():
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute("Select * from alunos")
    conn.commit()
    curry = cur.fetchall()
    conn.close()
    return curry

@app.get("/check/alunos/{id}")
async def checkalunos(id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute(f"Select * from alunos where id ={id}")
    conn.commit()
    curry = cur.fetchall()
    conn.close()
    return curry

@app.get("/addaluno")
async def addaluno(nome: str, num: int, email: str, turma_id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")

    conn.execute(f"""INSERT INTO alunos(nome, numero, email, turma_id) VALUES ('{nome}', {num}, '{email}', {turma_id});""")

    conn.commit()

    conn.close()

@app.get("/changealuno")
async def changealuno(id: int, nome: str = None, num: int = None, email: str = None, turma_id: int = None):

    if nome == None and num == None and email == None and turma_id == None:
        return "null"

    conn = sqlite3.connect("pi_dbDemo.sqlite")

    if nome != None:
        conn.execute(f"""UPDATE alunos set nome = '{nome}' where id = {id};""")

    if num != None:
        conn.execute(f"""UPDATE alunos set numero = {num} where id = {id};""")

    if email != None:
        conn.execute(f"""UPDATE alunos set email = '{email}' where id = {id};""")

    if turma_id != None:
        conn.execute(f"""UPDATE alunos set turma_id = {turma_id} where id = {id};""")

    conn.commit()

    conn.close()

@app.get("/remove/aluno/{id}")
async def delaluno(id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")

    conn.execute(f"delete from alunos where id = {id};")

    conn.commit()

    conn.close()

@app.get("/check/professores")
async def checkprofessores():
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute("Select * from professores")
    conn.commit()
    curry = cur.fetchall()
    conn.close()
    return curry

@app.get("/check/professores/{id}")
async def checkprofs(id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")
    cur = conn.cursor()
    cur.execute(f"Select * from professores where id ={id}")
    conn.commit()
    curry = cur.fetchall()
    conn.close()
    return curry

@app.get("/addprofessor")
async def addprofessor(nome: str, num: int, email: str, turma_id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")

    conn.execute(f"""INSERT INTO professores(nome, numero, email, turma_id) VALUES ('{nome}', {num}, '{email}', {turma_id});""")

    conn.commit()

    conn.close()

@app.get("/changeprofessor")
async def changeprofessor(id: int, nome: str = None, num: int = None, email: str = None, turma_id: int = None):

    if nome == None and num == None and email == None and turma_id == None:
        return "null"

    conn = sqlite3.connect("pi_dbDemo.sqlite")

    if nome != None:
        conn.execute(f"""UPDATE professores set nome = '{nome}' where id = {id};""")

    if num != None:
        conn.execute(f"""UPDATE professores set numero = {num} where id = {id};""")

    if email != None:
        conn.execute(f"""UPDATE professores set email = '{email}' where id = {id};""")

    if turma_id != None:
        conn.execute(f"""UPDATE professores set turma_id = {turma_id} where id = {id};""")

    conn.commit()

    conn.close()

@app.get("/remove/professor/{id}")
async def delprof(id: int):
    conn = sqlite3.connect("pi_dbDemo.sqlite")

    conn.execute(f"delete from professores where id = {id};")

    conn.commit()

    conn.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts/{id}")
async def rootTeste(id: int):
    p = postList[id]
    return {"id": f"{id}", "title": f"{p.title}", "body": f"{p.body}","userId":f"{p.userId}" }

@app.get("/posts")
async def rootTeste(id: int = -1):
    pId = 1
    if id == -1:
        posts = []
        for post in postList:
            posts.append({"id": f"{pId}", "title": f"{post.title}", "body": f"{post.body}", "userId": f"{post.userId}"})
            pId += 1
        return posts

    p = postList[id]
    return {"id": f"{id}", "title": f"{p.title}", "body": f"{p.body}","userId":f"{p.userId}" }
