import pickle

from flask import Flask, jsonify, request

from convert_predict_service import predict_single

app = Flask('convert-predict')

with open('modelos/convert-model.pck', 'rb') as f:
    dv, model = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    churn, prediction = predict_single(customer, dv, model)

    result = {
        'Converted': bool(churn),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
