from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Prathibha - 2022BCD0036</h1><p>This is a microservices-based app.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)  
