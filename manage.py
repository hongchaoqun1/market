import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


from app import create_app, db 
from app.models import UserInfo, Merchant


app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, UserInfo=UserInfo, Merchant=Merchant)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()