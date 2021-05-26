import joblib
exp = float(input('Enter your year of experience: '))
model = joblib.load('marks.pk1')
print()
print('Your years of experience: ', num)
output = model.predict([[num]])
print('Your Salaray   : ', output)
