from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

display = "" 
products = []
unidades = [random.randint(1,10) for i in range(41)]

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html', display=display, products=products, unidades=unidades)


@app.route('/upload', methods=["POST", "GET"])
def upload():
    global display, products, unidades
    if request.method == "POST":
        value = request.form["button"]
        if value == "Sel":
            if request.method == "POST":
                if display == "0" or display=="" or int(display)>40:
                    error2 = "Número fuera de rango"
                    display = ""
                    return render_template('index.html', error2=error2, products=products, unidades=unidades)
                name = "drink"+display
                if products.count(name) >=unidades[int(display)]: 
                    error = "No hay más unidades"
                    display = ""
                    return render_template('index.html', error=error, products=products, unidades=unidades)
                products.append(name)
                drink_value = request.form[name]
                return render_template('index.html', drink_value=drink_value, products=products, unidades=unidades)
        elif value == "fproduct":
            nam = 'drink'+display
            diferencia = unidades[int(display)] - products.count(nam)
            display = ""
            mensaje1 = "Tomaste un producto"
            mensaje2 = "Quedan "+ str(diferencia)+" unidades"
            print(unidades)    
            return render_template('index.html', products=products, unidades=unidades, mensaje1=mensaje1, mensaje2=mensaje2)    
        elif value == "C":
            display = ""
        elif value == "R":
            display = display[:-1]
        else:
            display += value
        
        return render_template('index.html', display=display, products=products, unidades=unidades)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)