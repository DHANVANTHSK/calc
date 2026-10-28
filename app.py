from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json() or {}
    operation = data.get('operation')
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    else:
        return jsonify({"error": "Unsupported operation in Push 1"}), 400
        
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
