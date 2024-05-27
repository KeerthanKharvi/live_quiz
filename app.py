"""from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True) """


from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store quizzes
quizzes = {}

# Endpoint to create a new quiz
@app.route('/quiz', methods=['POST'])
def create_quiz():
    quiz_data = request.json
    quiz_id = len(quizzes) + 1
    quizzes[quiz_id] = quiz_data
    return jsonify({"message": "Quiz created", "quiz_id": quiz_id}), 201

# Endpoint to fetch a quiz by ID
@app.route('/quiz/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    quiz = quizzes.get(quiz_id)
    if quiz is None:
        return jsonify({"message": "Quiz not found"}), 404
    return jsonify({"quiz_id": quiz_id, "quiz": quiz})

# Endpoint to fetch all quizzes
@app.route('/quizzes', methods=['GET'])
def get_all_quizzes():
    return jsonify(quizzes)

if __name__ == '__main__':
    app.run(debug=True)
