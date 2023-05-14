from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'productosdb'
mysql = MySQL(app)

app.secret_key = 'Utec2023'


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('select * from productos')
    data = cur.fetchall()
    return render_template('index.html',productos=data)
    # return 'Hola mundo'

@app.route('/add_producto',methods=['POST'])
def add_product():
    if request.method == 'POST':
        des = request.form['descripcion']
        pre = request.form['precio']
        stc = request.form['stock']
        cat = request.form['categoria']
        mar = request.form['marca']
        mod = request.form['modelo']

#        print('INSERT', id, nom, tel, email)
        print('INSERT', des) 
        cur = mysql.connection.cursor()
        cur.execute('insert into productos(descripcion, precio, stock, categoria, marca, modelo) values(%s,%s,%s,%s,%s,%s)', (des, pre,stc,cat,mar,mod))
        mysql.connection.commit()
        flash('Producto Insertado correctamente')
        return redirect(url_for('index'))

@app.route('/edit/<id>')
def edit_product(id):
    cur = mysql.connection.cursor()
    cur.execute('select * from productos where CODIGO = %s',{id})
    data = cur.fetchall()
    print(data[0])
    return render_template('edit.html', producto=data[0])

@app.route('/delete/<string:id>')
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute('delete from productos where CODIGO = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado correctamente')
    return redirect(url_for('index'))
    

@app.route('/update/<id>',methods=['POST'])
def update_product(id):
    if request.method == 'POST':
        des = request.form['descripcion']
        pre = request.form['precio']
        stc = request.form['stock']
        cat = request.form['categoria']
        mar = request.form['marca']
        mod = request.form['modelo']
        print('UPDATE', des)
        cur = mysql.connection.cursor()
        cur.execute("""
            update productos
            set descripcion = %s,
                precio = %s,
                stock = %s,
                categoria = %s,
                marca = %s,
                modelo = %s
            where CODIGO = %s
        """,  (des, pre,stc,cat,mar,mod, id) )
        mysql.connection.commit()
        flash('Producto actualizado correctamente')
        return redirect(url_for('index'))


@app.route('/saludo')
def saludo():
    return render_template('saludar.html')

@app.route('/adios')
def adios():
    return render_template('adios.html')

if __name__ == '__main__':
    app.run(port=3000,debug=True)