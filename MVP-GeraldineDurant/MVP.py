from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Exemple de sites à surveiller
    sites = ["http://google.com", "http://example.org","http://toto.hsdj"]
    status = {}

    for site in sites:
        try:
            response = requests.get(site)
            status[site] = "En ligne" if response.status_code == 200 else "Hors ligne"
        except requests.ConnectionError:
            status[site] = "Hors ligne"

    return render_template('dashboard.html', status=status)

if __name__ == '__main__':
    app.run(debug=True)