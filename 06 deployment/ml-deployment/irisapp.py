from flask import Flask, render_template, request
from joblib import load
import os.path

app = Flask(__name__)

# ----------------------------------------------------------------------------

model = load(os.path.join('models', 'irismodel.joblib'))

# ----------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('iris.html')

@app.route('/process', methods=['GET', 'POST'])
def process():

    X_test = []
    temp = [item[1] for item in request.form.items()]
    X_test.append([float(item) for item in temp[:-1]])

    prediction = model.predict(X_test)

    '''
    if(prediction[0] == 0):
        flower_type = "SETOSA"
    elif (prediction[0] == 1):
        flower_type = "VERSICOLOR"
    else:
        flower_type = "VIRGINICA"

    return render_template('result.html', flower_type=flower_type)
    '''

    return render_template('result.html', flower_type=prediction[0])

    

if __name__ == '__main__':
    app.run(debug=True)