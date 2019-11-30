from app import create_app


#create app instance
app = create_app('development')


if __name__ == '__main__':
    app.run()