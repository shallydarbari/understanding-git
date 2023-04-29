from flask import Flask
app=Flask(__name__)
@app.route("/base")
def home():
	return "Hello from Home"
if(__name__=="__main__"):
	app.run()