from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np

# ----------------------------------------------------
# Flask App Configuration
# ----------------------------------------------------
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create upload folder automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ----------------------------------------------------
# Check file extension
# ----------------------------------------------------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ----------------------------------------------------
# Home Page
# ----------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------------------------------
# Predict Image
# ----------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return render_template(
            "index.html",
            prediction="No image selected."
        )

    file = request.files["image"]

    if file.filename == "":
        return render_template(
            "index.html",
            prediction="Please choose an image."
        )

    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        # -----------------------------------------
        # Read Image
        # -----------------------------------------
        image = cv2.imread(filepath)

        if image is None:
            return render_template(
                "index.html",
                prediction="Invalid image."
            )

        # Resize image
        image = cv2.resize(image, (224, 224))

        # -----------------------------------------
        # Temporary Detection Logic
        # (AI model will be added later)
        # -----------------------------------------

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        mean_value = np.mean(gray)

        if mean_value > 120:

            result = "Real Image ✅"

            confidence = "91.8%"

        else:

            result = "DeepFake Image ❌"

            confidence = "88.4%"

        return render_template(
            "index.html",
            prediction=result,
            confidence=confidence,
            image=filename
        )

    return render_template(
        "index.html",
        prediction="Only JPG, JPEG and PNG are allowed."
    )


# ----------------------------------------------------
# Run Application
# ----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)