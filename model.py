import pandas as pd
import joblib
data = pd.read_csv('salary.csv')
x = data['YearsExperience'].values.reshape(-1,1)
y = data['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
joblib.dump(model, 'marks.pk1')
