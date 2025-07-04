from flask import Flask, render_template
from app.routes import bp

app = Flask(__name__, template_folder='templates')
app.register_blueprint(bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
