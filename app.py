from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

app = Flask(__name__)


data = pd.read_csv("data.csv")
data.dropna(inplace=True)
data_encoded = pd.get_dummies(data, columns=["Gender", "Education Level", "Job Title"], drop_first=True)
X = data_encoded.drop("Salary", axis=1)
y = data_encoded["Salary"]

model = LinearRegression()
model.fit(X, y)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
 
    age = int(request.form["age"])
    gender = request.form["gender"]
    education = request.form["education"]
    job = request.form["job"]
    exp = int(request.form["experience"])

    
    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Education Level": education,
        "Job Title": job,
        "Years of Experience": exp
    }])

    
    combined = pd.concat([data.drop("Salary", axis=1), input_data], ignore_index=True)
    combined_encoded = pd.get_dummies(combined, columns=["Gender", "Education Level", "Job Title"], drop_first=True)
    combined_encoded = combined_encoded.reindex(columns=X.columns, fill_value=0)

    
    pred = model.predict(combined_encoded.tail(1))[0]

    
    y_train_pred = model.predict(X)
    r2 = r2_score(y, y_train_pred)

    return render_template("index.html", prediction=round(pred, 2), hu=round(r2, 4))
if __name__ == "__main__":
    app.run(debug=True)
