class BaseConfig(object):  
    DEBUG = True
    #FOR LOCAL
    MYSQL_DATABASE_USER = "root"
    MYSQL_DATABASE_PASSWORD = ""
    MYSQL_DATABASE_DB = "myproject"
    MYSQL_DATABASE_HOST = "localhost"
    # used for encryption and session management
    JWT_SECRET_KEY = 'mysecretkey'


    
    #FOR EC2
    # MYSQL_DATABASE_USER = "admin"
    # MYSQL_DATABASE_PASSWORD = "pwd123"
    # MYSQL_DATABASE_DB = "Pihitak"
    # MYSQL_DATABASE_HOST = "localhost"
    # # used for encryption and session management
    # JWT_SECRET_KEY = 'mysecretkey'