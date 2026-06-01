import psycopg2 #type: ignore
from flask import Flask, render_template #type: ignore
import webbrowser
from threading import Timer

app = Flask(__name__)
conn = psycopg2.connect("postgresql://cvms_achn_user:cgefSxswr84dVSX81UPxxylIdTO5sddk@dpg-d8er7murnols73ajqe2g-a.virginia-postgres.render.com/cvms_achn")

@app.route("/")
def home():
    name = "Alice"
    items = ["apple", "banana", "cherry"]
    return render_template("CVMS.html", name=name, items=items)

def open_browser():
    webbrowser.open("http://localhost:5000")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))