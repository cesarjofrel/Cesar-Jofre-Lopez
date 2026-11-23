from flask import Flask, render_template, request

app = Flask(__name__)


# Ruta del Menú Principal
@app.route('/')
def index():
    return render_template('index.html')


# Ruta Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None

    if request.method == 'POST':
        # Capturamos los datos que el usuario escribió en el HTML
        n1 = float(request.form['nota1'])
        n2 = float(request.form['nota2'])
        n3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calculamos el promedio
        promedio = (n1 + n2 + n3) / 3

        # Verificamos las condiciones del documento (>= 40 y >= 75)
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)


# Ruta Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_largo = None
    cantidad = None

    if request.method == 'POST':
        # Guardamos los 3 nombres en una lista
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]

        # max() busca el mayor. key=len significa que busque el de mayor longitud (caracteres)
        nombre_largo = max(nombres, key=len)
        cantidad = len(nombre_largo)

    return render_template('ejercicio2.html', nombre_largo=nombre_largo, cantidad=cantidad)


# Esto hace que el servidor se ejecute
if __name__ == '__main__':
    app.run(debug=True)