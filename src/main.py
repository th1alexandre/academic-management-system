from flask import Flask

from config import FlaskConfig
from library.exceptions import exception_handler
from swagger import initialize_flasgger

from routes.pessoa.route import bp_pessoa


def create_app():
    try:
        app = Flask(__name__)

        initialize_flasgger(app)

        app.config.from_object(FlaskConfig())
        app.register_error_handler(Exception, exception_handler)

        app.register_blueprint(bp_pessoa, url_prefix="/pessoa")

        return app
    except Exception as e:
        raise Exception(f"Error while creating app: {e}")


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
