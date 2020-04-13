import joblib
model = joblib.load('mySalaryModel.pk1')
print("Welcome To Salary Predictor")
print("Please enter your year of experience", end = ':')
exp = float(input())
predicted = model.predict([[exp]])
print("Expected Salary is:", predicted[0])
