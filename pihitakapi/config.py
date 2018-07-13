class BaseConfig(object):  
    DEBUG = True
    MYSQL_DATABASE_USER = "admin"
    MYSQL_DATABASE_PASSWORD = "pwd123"
    MYSQL_DATABASE_DB = "Pihitak"
    MYSQL_DATABASE_HOST = "localhost"
    # used for encryption and session management
    JWT_SECRET_KEY = 'mysecretkey'
    
    