# Cowitter News App

With exponentially increasing daily cases of novel-coronavirus, new developments in various fields are also made almost at the same pace.  
This app is your one stop destination for your all covid-19 related news (sentiment segregated).  

## Model:-
- **Model Architecture:-**  
    - A Multi-output Functional API Model (Keras with Tensorflow as backend)  
    - Dense Layers(4) with activation: Relu  
    - LSTM Unidirectional (2)
    - Embedding Layer  
    - Loss Function(s): Binary Crossentropy  
    - Metrics : Accuracy  
    - Optimizer : Adam (default)  

- **Model Save:-**  
   - Keras Saved Model format (Model/Final_Model)  
   - Json file format (Model/final_model.json)  

- **Model Deployment:-**  
    - Model is deployed using REST-API using Flask mini-framework. (main_app.py)  
    - Preparing Input for prediction on server. (processing.py)    
    - Dummy request make for testing. (request.py)
    
_ **Directory Map:**
    - Master Model File -- main.ipynb  

## Requirements:-  
- Tensorflow  
- Keras  
- Pandas  
- Numpy  
- NLTK  
- scikit-learn  
- Flask  
- Git (optional)  
- Conda (optional)  
- Local sever  

**NOTE: Anyone is more than welcome to contribute/bug-fix/update syntax etc.**    
*This space may be updated soon*


#### Work of : [@that_danish](https://github.com/thatdanish)
