from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html", error=None, name="")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name", "").strip()
    password = request.form.get("password", "")

    if not name:
        return render_template(
            "register.html",
            error="Username cannot be empty",
            name=name
        )

    if not password:
        return render_template(
            "register.html",
            error="Password cannot be empty",
            name=name
        )

    if len(password) < 6:
        return render_template(
            "register.html",
            error="Password must be at least 6 characters long",
            name=name
        )

    return render_template("successful.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)