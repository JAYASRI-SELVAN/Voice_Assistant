from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_query', methods=['POST'])
def process_query():
    user_query = request.form['user_query']
    assistant_response = f"You said: {user_query}"
    return render_template('index.html', user_query=user_query, assistant_response=assistant_response)

if __name__ == '__main__':
    app.run(debug=True)
