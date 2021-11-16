import pymysql
import pymysql.cursors
sys.path.append(r'C:\Users\Sriram\Desktop\SkidosDatabase\SkidosScripts\Authentication')
from MySQL_config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE


def mysql_connect(host, port, user, pswrd, db):
    """function to make MySQl connection using pymysq and credentials"""
    connection = pymysql.connect(host=host,
                                 port=port,
                                 user=user,
                                 password=pswrd,
                                 database=db)
    print(connection)
    return connection

    
mysql_connect( MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
