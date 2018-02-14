from flask import Flask, render_template_string, request
# ssh <username>@ssh.pythonanywhere.com
app = Flask(__name__)
html = """
    <div class="form">
    <form action="{{url_for('sent')}}" method="POST">
        <input type="text" title="your email address will be safe with us." placeholder="enter a line" name="line" required>
        <br>
        <button class="go-button" type="submit"> Submint </button>
    </form>
    </div>
"""
@app.route("/")
def index():
    return render_template_string(html)

@app.route("/sent", methods=["GET","POST"])
def sent():
    line = None
    if request.method == "POST":
        line = request.form["line"]
        with open("user_input_flask.txt", "a+") as target:
            target.write(line+"\n")
        return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)