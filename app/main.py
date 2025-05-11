from flask import Flask, request, render_template
from extract_processor import formatContentToGoogleSheets


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = ''
    if request.method == "POST":
        month = int(request.form.get("month"))
        person = request.form.get("person")
        content = request.form.get("content")
        result = formatContentToGoogleSheets(content, month, person)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
