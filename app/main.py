from flask import Flask, request, render_template, url_for

app = Flask(__name__) 

secret = "323327"

@app.route("/", methods=["GET", "POST"])
def startPage():
    if request.method == "POST":
        enteredSecret = request.form.get("password")
        if enteredSecret == secret:
            return render_template("index.html", show_content=True)
        else:
            return render_template("startpage.html", error=True)
    else:
        show_content = request.args.get("show_content", False)
        return render_template("startpage.html", error=False, show_content=show_content)

if __name__ == "__main__":
    app.run(debug=True)