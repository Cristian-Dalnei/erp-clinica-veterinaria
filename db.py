def conectar():
    import psycopg
    conn = psycopg.connect(user="postgres", password="SUA-SENHA-AQUI", host="localhost", dbname="pet_shop")
    return conn

