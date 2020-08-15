from flask import Flask,jsonify,request
from processing import call_model,preprocess_data
import numpy as np
import pandas as pd
import silence_tensorflow.auto

app = Flask(__name__)
@app.route('/predict',methods=['POST'])
def predict():
    
    if request.method == 'POST':
        data = {'success':False}
        raw_in = request.get_json()
        df = pd.DataFrame([raw_in['text']],columns=['text'])
        pred_df = df['text'][0]

        final_input = preprocess_data(pred_df)
        out_covid,out_senti = model.predict(final_input)
        out_covid = np.argmax(out_covid)
        out_senti = np.argmax(out_senti)
        out_covid = str(out_covid)
        out_senti = str(out_senti)
        final_output = [out_covid,out_senti]

        data['Prediction'] = final_output
        data['success'] = True
    return jsonify(data)


if __name__ == '__main__':
    print("***********Loading Model********")
    model = call_model()
    app.run(debug=True,port=5000)