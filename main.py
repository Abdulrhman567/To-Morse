from flask import Flask, render_template, redirect, url_for, request, flash
from morse_code import codes
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route("/", methods=['GET', 'POST'])
def home():
    full_morse_code = ""
    if request.method == 'POST':
        text_data = request.form.get('usertext')
        morse_code = [' '.join(codes[char]) if char in codes else 'flash' for char in text_data.lower()]
        if 'flash' in morse_code:
            flash("Can't translate these characters, Please try again!", category="error")
            return redirect(url_for("home"))
        else:
            full_morse_code = ''.join(morse_code)
    return render_template('index.html', full_code=full_morse_code)


if __name__ == "__main__":
    app.run(debug=True)
