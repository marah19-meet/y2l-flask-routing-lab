from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	clothes=["blue jeans","black jeans","white skirt","black skirt"]
	return render_template("home2.html",clothes=clothes)

@app.route("/shop")
def shop_page():
	return render_template("shop.html")



if __name__ == '__main__':
   app.run(debug = True)
