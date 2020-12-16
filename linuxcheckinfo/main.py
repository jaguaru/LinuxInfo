import routes
from app import app

HOST = '127.0.0.7'
PORT = 5007

if __name__ == '__main__':
   app.run(host=HOST, port=PORT)