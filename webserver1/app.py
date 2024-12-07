from flask import Flask, render_template_string
import redis

# Creăm instanța aplicației Flask.
app = Flask(__name__)

# Configurăm conexiunea cu serverul Redis, care rulează pe host-ul 'redis' și portul 6379.
cache = redis.Redis(host='redis', port=6379)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Server 1</title>
    <style>
        /* Stiluri CSS pentru aspect și design */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff; /* Fundal albastru deschis */
            color: #333; /* Text închis */
            text-align: center; /* Text centrat */
            padding: 50px; /* Spațiere */
        }
        h1 {
            color: #3498db; /* Titlu în albastru */
        }
        .visits {
            font-size: 1.5em; /* Mărime text mai mare pentru numărul de vizite */
            margin-top: 20px; /* Spațiu deasupra textului */
            color: #2c3e50; /* Text închis */
        }
    </style>
</head>
<body>
    <!-- Titlu și numărul total de vizite -->
    <h1>Welcome to Web Server 1</h1>
    <p class="visits">Total Visits: {{ visits }}</p>
</body>
</html>
"""

@app.route('/')
def index():
    # Incrementăm contorul de vizite stocat în Redis.
    visits = cache.incr('visits')
    
    # Generăm pagina HTML și inserăm numărul de vizite.
    return render_template_string(HTML_TEMPLATE, visits=visits)

# Aplicația va rula pe toate interfețele de rețea ale gazdei (0.0.0.0) și pe portul 5000.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)