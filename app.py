from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

products = products = {
    "electronics": [
        {"name": "Laptop", "price": 50000, "image": "images/laptop.jpg"},
        {"name": "Smartphone", "price": 20000, "image": "images/phone.jpg"},
        {"name": "Headphones", "price": 3000, "image": "images/headphones.jpg"}
    ],

    "clothes": [
        {"name": "T-Shirt", "price": 800, "image": "images/tshirt.jpg"},
        {"name": "Jeans", "price": 1500, "image": "images/jeans.jpg"},
        {"name": "Jacket", "price": 2500, "image": "images/jacket.jpg"}
    ],

    "kitchen": [
        {"name": "Mixer Grinder", "price": 3500, "image": "images/mixi.jpg"},
        {"name": "Pressure Cooker", "price": 2000, "image": "images/cooker.jpg"},
        {"name": "Gas Stove", "price": 4000, "image": "images/gasstove.jpg"}
    ],

    "bedroom": [
        {"name": "Bed Sheet", "price": 1200, "image": "images/bedsheet.jpg"},
        {"name": "Pillow", "price": 600, "image": "images/pillow.jpg"},
        {"name": "Blanket", "price": 2500, "image": "images/blanket.jpg"}
    ]
}

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        session["cart"] = []
        return redirect("/home")
    return render_template("login.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")
    return render_template("home.html", products=products)

@app.route("/add_to_cart/<item>/<price>")
def add_to_cart(item, price):
    cart = session.get("cart", [])
    cart.append({"item": item, "price": int(price)})
    session["cart"] = cart
    return redirect("/home")

@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    total = sum(item["price"] for item in cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/order")
def order():
    session["cart"] = []
    return render_template("order.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)