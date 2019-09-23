from flask_script import Manager,Server
from app import create_app,db
from app.models import User,Comment,Writer,Blog
from flask_migrate import Migrate,MigrateCommand

app=create_app()
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('runserver',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Comment=Comment,Writer=Writer,Blog=Blog)

if __name__ =='__main__':
    manager.run()
