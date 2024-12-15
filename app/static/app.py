from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disqualified')
def disqualified():
    return "You have been disqualified from the exam."

@app.route('/submitted')
def submitted():
    return "Your quiz has been submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
