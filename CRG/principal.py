
from flask import Flask,render_template,request
from flaskext.mysql import MySQL
aplicacion=Flask(__name__)
mysql=MySQL()
aplicacion.config['MYSQL_DATABASE_HOST']= 'localhost'
aplicacion.config['MYSQL_DATABASE_PORT']=3306
aplicacion.config['MYSQL_DATABASE_USER']= 'root'
aplicacion.config['MYSQL_DATABASE_PASSWORD']= ''
aplicacion.config['MYSQL_DATABASE_DB']= 'cristian'

mysql.init_app(aplicacion)

@aplicacion.route('/')
def index():
    return render_template('/login.html')
@aplicacion.route("/ir")
def ir():
    return render_template("/agregar.html")

@aplicacion.route("/buscar", methods=['POST'])
def buscar():
    encontrar=request.form['nombre']
    sql=f"call busqueda('{encontrar}');"
    con=mysql.connect()
    cur=con.cursor()
    cur.execute(sql)
    resultado=cur.fetchone()
    con.commit
    print(resultado)
    return render_template("login.html",datos=resultado)

@aplicacion.route("/crear" ,methods=['POST'])
def crear():
    nombre=request.form['nombre']
    edad=request.form['edad']
    profecion=request.form['profecion']
    sql=f"call insertar ('{nombre}','{edad}','{profecion}');"
    con=mysql.connect()
    cur=con.cursor()
    cur.execute(sql)
    con.commit()
    print(sql)
    return render_template("agregar.html")




if __name__=='__main__':
    aplicacion.run(host="0.0.0.0",debug=True,port="8081" )






