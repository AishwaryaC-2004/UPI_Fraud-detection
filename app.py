from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

model = joblib.load("fraud_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["file"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(filepath)

    data = pd.read_csv(filepath)

    prediction = model.predict(data)

    data["Prediction"] = prediction

    output_path = os.path.join(OUTPUT_FOLDER, "prediction.csv")

    data.to_csv(output_path,index=False)

    fraud = (prediction==1).sum()

    genuine = (prediction==0).sum()

    return render_template(
        "result.html",
        fraud=fraud,
        genuine=genuine,
        total=len(data)
    )

if __name__=="__main__":
    app.run(debug=True)