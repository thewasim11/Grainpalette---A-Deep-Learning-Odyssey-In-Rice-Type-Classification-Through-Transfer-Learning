from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load your trained model
model = load_model("rice_model.h5")

# Route for the main page (index.html)
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

    # Save uploaded image to static folder
    img_path = os.path.join("static", file.filename)
    file.save(img_path)

    # Preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Predict using the model
    prediction = model.predict(img_array)

    # Get class names from your training folder
    class_names = sorted(os.listdir("C:/Users/pnmuk/GrainPalette/data/train"))
    predicted_class = class_names[np.argmax(prediction)]

    return render_template("index.html", prediction=predicted_class, image_path=img_path)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
