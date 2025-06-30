from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import uuid
import json

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = load_model("rice_classifier_v2.h5")

# Load class names from JSON
with open("class_names.json", "r") as f:
    index_to_class = json.load(f)

# Route for main page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Route for prediction
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]
    if file.filename == "":
        return "No file selected"

    # Save uploaded image with a unique filename
    unique_filename = str(uuid.uuid4()) + "_" + file.filename
    img_path = os.path.join("static", unique_filename)
    file.save(img_path)

    # Preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Make prediction
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class = index_to_class[str(predicted_class_index)]

    return render_template("index.html", prediction=predicted_class, image_path=img_path)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
