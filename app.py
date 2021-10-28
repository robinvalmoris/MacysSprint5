import os
from flask import Flask, render_template, g, flash, request, session, url_for,send_file,make_response
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from db import close_db, get_db

app=Flask(__name__)

app.secret_key=os.urandom(24)

@app.route('/', methods=('GET', 'POST'))
@app.route('/login', methods=('GET', 'POST'))
def login():
    #TODO
    try:
        if request.method == 'POST':
            print("Antes de db")
            db = get_db()
            error = None
            username = request.form['username']
            password = request.form['password']
            if not username:
                error = 'Debes ingresar el username'
                flash(error)
                return render_template('login.html')

            if not password:
                error = 'Contraseña requerida'
                flash(error)
                return render_template('login.html')   
            print("Antes de base de datos")
            user = db.execute(
                'SELECT * FROM usuario WHERE username = ?', (username,)).fetchone()
            print(user)
            if user is None:
                error = 'Usuario no encontrado'
                flash(error)
                print("Usuario no encontrado")
            else:
                print("Usuario encontrado", user)                
                print(user)
                contrasena_almacenada=user[4]
                print(contrasena_almacenada)
                print(generate_password_hash(password))
                resultado=check_password_hash(contrasena_almacenada,password)
                print(resultado)
                if (resultado==False):
                    error = 'Consulta realizada: Usuario o contraseña inválidos'
                    print('Consulta realizada: Usuario o contraseña inválidos')
                    return render_template('registro.html')
                else:
                    error = 'Consulta realizada: Usuario valido'
                    print("Usuario y contraseña correctos")
                    session.clear()
                    session["user_id"]=user[0]
                    session["username"]=user[3]
                    session["rol"]=user[1]
                    if (session.get( 'rol' )=='cliente'):
                        return render_template('inicio.html')
                    else:
                        return render_template('administrar.html') 
        return render_template('login.html')
    except:
        return render_template('login.html')


@app.route( '/logout' )
def logout():
    session.clear()
    return redirect(url_for( 'login' ))


@app.route('/registro', methods=('GET', 'POST'))
def registro():
    #TODO
    try:
        if request.method=='POST':
            print("inicia")
            rol=request.form['role']
            nombre=request.form['fullname']
            username=request.form['username']
            password=request.form['password']
            celular=request.form['phonenumber']
            correo=request.form['email']
            ciudad=request.form['city']
            direccion=request.form['address']
            informacion_adicional=request.form['aditional_information']
            error=None
            db = get_db()
            if error is not None:
                return render_template("login.html")
            else:
                db.execute("INSERT INTO usuario (rol, nombre_completo, username, contrasena, celular, correo, direccion, ciudad, informacion_adicional) VALUES (?,?,?,?,?,?,?,?,?)",
                     (rol, nombre, username, generate_password_hash (password), celular, correo, direccion, ciudad, informacion_adicional))
                db.commit()
        return render_template('registro.html')
    except:
        return render_template('registro.html')


@app.route('/inicio', methods=('GET', 'POST'))
def inicio():
    #TODO
    user_id = session.get( 'user_id' )
    if user_id is None:
        return redirect( url_for( 'login' ) )
    else:
        return render_template('inicio.html')

@app.route('/add/producto', methods=('GET', 'POST'))
def addProducto():
    #TODO
    return render_template('addProducto.html')

@app.route('/producto/editar', methods=('GET', 'POST'))
def editarProducto():
    #TODO
    return render_template('editarProducto.html')

@app.route('/producto/eliminar', methods=('GET', 'POST'))
def eliminarProducto():
    #TODO
    return render_template('eliminarProducto.html')

@app.route('/producto/calificar', methods=('GET', 'POST'))
def calificarProducto():
    #TODO
    return render_template('calificarProducto.html')

@app.route('/administrar', methods=('GET', 'POST'))
def administrar():
    #TODO
    return render_template('administrar.html')

@app.route('/lista/deseos', methods=('GET', 'POST'))
def listaDeseos():
    #TODO
    return render_template('listaDeseos.html')

@app.route('/comentarios', methods=('GET', 'POST'))
def comentarios():
    #TODO
    return render_template('comentarios.html')

if __name__=='__main__':
    app.run()
    # app.run(debug=True)