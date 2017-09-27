# manage.py

#third party import
import os
from flask_script import Manager, Shell


#local import
from initial import create_app


# Initialization
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()