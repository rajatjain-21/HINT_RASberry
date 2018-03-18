import pandas as pd
from sklearn.externals import joblib
def predictor_disease(dic):
    df=pd.read_csv('fillform/dataset_severe.csv',index_col=0)

    df=df.drop('Source',axis=1)

    col=df.columns

    sym={}
    for i in col:
        sym[i]=0
    for k,v in dic.items():
        sym[k]=v


    df=pd.DataFrame([sym],columns=sym.keys())
    import pickle
    classifier_model = joblib.load('fillform/bagging_model.pkl')
    predicted_labels =classifier_model.predict(df)

    prediction=predicted_labels

    return prediction[0]
