from flask import Flask, render_template, request, flash
from morse_code import codes
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route("/", methods=['GET', 'POST'])
def home():
    full_morse_code = ""
    if request.method == 'POST':
        text_data = request.form.get('usertext').lower()
        for char in text_data:
            if char in codes:
                full_morse_code += codes[char] + ' '
            else:
                flash(message='Error in input, Can not translate these characters, Try again.', category='error')
                break
    return render_template('index.html', full_code=full_morse_code)


debug = os.getenv('Debug') == 'True'
if __name__ == "__main__":
    app.run(debug=debug)
