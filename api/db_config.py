from app import app
from flaskext.mysql import MySQL
import os
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] =  os.environ.get('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] =  os.environ.get('MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] =  os.environ.get('MYSQL_DATABASE_HOST')  or 'localhost'
app.config['MYSQL_DATABASE_PORT'] =  int(os.environ.get('MYSQL_DATABASE_PORT')) or 3306
print(app.config)
print("DB User:", os.environ.get('MYSQL_DATABASE_USER'))
print("DB Password:", os.environ.get('MYSQL_DATABASE_PASSWORD'))
print("DB Host:", os.environ.get('MYSQL_DATABASE_HOST'))
print("DB Port:", os.environ.get('MYSQL_DATABASE_PORT'))
print("DB:", os.environ.get('MYSQL_DATABASE_DB'))
mysql.init_app(app)
