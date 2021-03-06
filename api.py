# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import pickle
import traceback
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("default", category=DeprecationWarning)

# Your API definition
app = Flask(__name__)


@app.route('/predict', methods=['POST','GET'])
def predict():

    if lr:
        try:
            json_ = request.get_json()
            print(type(json_))
            print(json_)
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return 'No model here to use'


if __name__ == '__main__':
    # try:
    #     port = int(sys.argv[1]) # This is for a command-line input
    # except:
    #     port = 12345 # If you don't provide any port the port will be set to 12345
    fileobject=open("model.pkl","rb")
    lr = pickle.load(fileobject) # Load "model.pkl"
    print('Model loaded')

    fileobject = open("model_columns.pkl", "rb")
    model_columns = pickle.load(fileobject)
    print('Model columns loaded')

    app.run(debug=True)
