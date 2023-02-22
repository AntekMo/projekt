from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd



app = Flask(__name__)

@app.route("/dataframe", methods=["POST"])
def return_dataframe():
    df = pd.DataFrame({"frm1": [1, 2, 3], "frm2": [4, 5, 6]})
    return jsonify(prediction = df.to_json())


if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')