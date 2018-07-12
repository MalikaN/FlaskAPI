class BaseConfig(object):  
    DEBUG = True
    MYSQL_DATABASE_USER = "root"
    MYSQL_DATABASE_PASSWORD = ""
    MYSQL_DATABASE_DB = "Pihitak"
    MYSQL_DATABASE_HOST = "localhost"
    # used for encryption and session management
    JWT_SECRET_KEY = 'mysecretkey'
    
    