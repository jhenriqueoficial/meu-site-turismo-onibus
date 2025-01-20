from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated data for destinations and reservations
destinations = [
    {"id": 1, "name": "Rio de Janeiro", "price": 100},
    {"id": 2, "name": "São Paulo", "price": 80},
    {"id": 3, "name": "Salvador", "price": 120}
]

reservations = []

@app.route('/')
def index():
    return render_template('index.html', destinations=destinations)

@app.route('/reserve/<int:destination_id>', methods=['GET', 'POST'])
def reserve(destination_id):
    destination = next((d for d in destinations if d["id"] == destination_id), None)
    if request.method == 'POST':
        name = request.form['name']
        reservations.append({"name": name, "destination": destination})
        return redirect(url_for('index'))
    return render_template('reserve.html', destination=destination)

if __name__ == '__main__':
    app.run(debug=True)