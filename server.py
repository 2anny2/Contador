from contador_app import app
from contador_app.controllers import controlador
app.secret_key = "supersecreto"

if __name__=="__main__": 
    app.run(debug=True)   