class BaseConfig(object):  
    DEBUG = True
    MYSQL_DATABASE_USER = "root"
    MYSQL_DATABASE_PASSWORD = "malika"
    MYSQL_DATABASE_DB = "ItemListDb"
    MYSQL_DATABASE_HOST = "localhost"
    # used for encryption and session management
    SECRET_KEY = 'mysecretkey'