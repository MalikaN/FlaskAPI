if __name__ == '__main__':  
    from pihitakapi.application import create_app
    app = create_app()
    app.run(host='127.0.0.1',port=5000)