from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from auth.auth_routes import auth_bp
from routes.task_routes import task_bp

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY

CORS(app)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(task_bp, url_prefix="/api")

@app.route("/")
def hello():
    return {"message": "Backend Running"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
