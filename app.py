from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecret"  # 세션 암호화 키

# 선수 리스트 (임시)
players = ["선수A", "선수B", "선수C", "선수D", "선수E",
           "선수F", "선수G", "선수H", "선수I", "선수J",
           "선수K", "선수L", "선수M", "선수N", "선수O"]

def init_db():
    conn = sqlite3.connect("draft.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            user TEXT,
            rank INTEGER,
            player TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"].strip()
        if not name:
            return render_template("login.html", error="이름을 입력하세요.")
        session["user"] = name
        return redirect("/predict")
    return render_template("login.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "user" not in session:
        return redirect("/")
    if request.method == "POST":
        selected_players = [request.form[f"rank{i}"] for i in range(1, 11)]
        conn = sqlite3.connect("draft.db")
        c = conn.cursor()
        c.execute("DELETE FROM predictions WHERE user=?", (session["user"],))
        for i, p in enumerate(selected_players, 1):
            c.execute("INSERT INTO predictions VALUES (?, ?, ?)",
                      (session["user"], i, p))
        conn.commit()
        conn.close()
        return redirect("/results")
    return render_template("predict.html", players=players, user=session["user"])

@app.route("/results")
def results():
    conn = sqlite3.connect("draft.db")
    c = conn.cursor()
    c.execute("SELECT * FROM predictions ORDER BY user, rank")
    data = c.fetchall()
    conn.close()
    return render_template("results.html", data=data)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
