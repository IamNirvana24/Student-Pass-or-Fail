import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split



data = pd.read_csv(r"C:\Machine Learning\Projects\Machine Learning Models\Logistic & Linear Regression\Student Pass or Fail\student_pass_fail_dataset.csv")
print(data.head)

X = data[['Study Hours', 'Attendance (%)', 'Assignments Submitted', 'Internal Marks']]
y = data['Pass/Fail']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Actual", list(y_test[0:7]))
print("Predicted", list(y_pred[0:7]))

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Achievements")
plt.ylabel("Predicted Achievements")
plt.title("Student Passed or Fail")
plt.show()
