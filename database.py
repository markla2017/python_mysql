import mysql.connector

config = {
    'user': 'root',
    'password': 'my-secret-pw',
    'host': '192.168.56.105',   
    'database': 'acme' 
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
