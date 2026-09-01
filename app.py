from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    print("\n====================================")
    print("       ScanMAT Flask Server")
    print("====================================")
    print("Open on this computer:")
    print("http://127.0.0.1:5000")
    print("\nFor your phone, use your computer's")
    print("local IP address, for example:")
    print("http://192.168.1.10:5000")
    print("====================================\n")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )