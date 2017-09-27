# manage.py 
# third party import
from flask import Flask


#local import
from views import main


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app


def main_point():
    app = create_app()
    app.run(debug=True)


if __name__ == '__main__':
    main_point()