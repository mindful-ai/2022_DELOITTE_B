from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from joblib import dump
import os.path

def genmodel(id='iris'): 
    if(id == 'iris'):
        iris = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.1, random_state=42)
        lr = LogisticRegression(max_iter=100, solver='liblinear', n_jobs=1)
        lr.fit(X_train, y_train)
        return lr
    return None

if __name__ == "__main__":
    lr = genmodel()
    dump(lr, os.path.join('models', 'irismodel.joblib'))