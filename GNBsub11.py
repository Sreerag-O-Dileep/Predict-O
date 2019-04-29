import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest, chi2
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
df = pd.read_csv("data\sub1_data.csv", sep=",")
from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()
fselect=df.iloc[:,:]
for column in fselect:
    df[column]=le.fit_transform(df[column])
y = df.pop("class")
X = df
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=17)
clf = Pipeline([
    ('reduce_dim', SelectKBest(chi2, k=4)),
    ('train', GaussianNB())
])
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("GNB Model Accuracy")
print(metrics.accuracy_score(y_test, y_pred))

def gnbsub11(values):
    result = clf.predict(values)
    if result == 0|result == 1:
        return 'excellent'
    else:
        return 'poor'

