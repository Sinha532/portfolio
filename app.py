from flask import Flask, render_template, request, jsonify, send_from_directory


# Initialize Flask app
app = Flask(__name__)

# Route for serving the static page
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
