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
        morse_list = [codes[char] + ' ' if char in codes else 'flash' for char in text_data]
        if 'flash' in morse_list:
            flash(message='Error in input, Can not translate these characters, Try again.', category='error')
        else:
            full_morse_code = ''.join(morse_list)
    return render_template('index.html', full_code=full_morse_code)


debug = os.getenv('Debug') == 'True'
if __name__ == "__main__":
    app.run(debug=debug)
