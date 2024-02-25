# Conexión a la base de datos lab_ing_software
def conectarse_a_bade_de_datos():
    return pymysql.connect(
        host='localhost',
        user='lab',
        password='Developer123!',
        database='lab_ing_software',
        cursorclass=pymysql.cursors.DictCursor
