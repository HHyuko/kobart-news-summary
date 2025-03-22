from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    keyword = request.form.get("keyword", "")
    return f"<h2>요약 결과</h2><p>키워드: {keyword}</p>"

if __name__ == "__main__":
    app.run(debug=True)