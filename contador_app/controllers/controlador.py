from contador_app import app
from flask import render_template, redirect, session

@app.route('/')          
def contador():
    if 'numero'in session:
        session['numero'] += 1
    else:
        session['numero'] = 0
    return render_template('index.html')

@app.route('/contador')
def sumar_visitas():
    session['numero'] += 1
    return redirect('/')

@app.route('/eliminar')
def eliminar_visitas():
    session.clear()
    return redirect('/')
