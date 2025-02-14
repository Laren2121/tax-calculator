from flask import Flask
from api.tax_routes import tax_blueprint

def create_app(config_filename=None): 

    app = Flask(__name__)

    if config_filename: 
        app.config.from_pyfile(config_filename)
    else: 
        app.config.from_object('config.DefaultConfig')

    app.register_blueprint(tax_blueprint)

    return app

if __name__ == "__main__": 
    app = create_app()
    app.run(debug=True, port=5002)



#http://localhost:5002/api/calculate-tax?salary=50000&tax_year=2022
