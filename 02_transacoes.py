import sqlite3

# para colocar na pasta certa
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")


cursor = conexao.cursor()

cursor.row_factory = sqlite3.Row


try:
    cursor.execute('INSERT INTO cliente (nome, email) VALUES (?,?)', ('Teste2', "teste@gmail,com"))
    cursor.execute('INSERT INTO cliente (id, nome, email) VALUES (?,?)', (2, 'Teste2', "teste@gmail,com")) #vai dar erro
    conexao.commit()
except Exception as exc:
    print(f"Erro {exc}")
    conexao.rollback()