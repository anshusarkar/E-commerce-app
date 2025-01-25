from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    products = [
        {"name": "Cadbury _ choco_bakes", "price": "₹5.00", "image": "Cadbury_choco_bakes.jpg"},
        {"name": "DEEP_tea", "price": "₹30.00", "image": "DEEP_tea.jpg"},
        {"name": "Soya_sauce", "price": "₹45.00", "image": "Soya_sauce.jpg"},
        {"name": "Tomato_Ketchup", "price": "₹45.00", "image": "Tomato_Ketchup.jpg"}
    ]
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)