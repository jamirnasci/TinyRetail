from flask import Flask
from flask_cors import CORS
from controller.product_controller import product_bp
from controller.sales_controller import sales_bp
from controller.user_controller import user_bp
app = Flask(__name__)
CORS(app)

app.register_blueprint(product_bp, '/products')
app.register_blueprint(sales_bp, '/sales')
app.register_blueprint(user_bp, '/users')

if __name__ == '__main__':
    app.run(debug=True)