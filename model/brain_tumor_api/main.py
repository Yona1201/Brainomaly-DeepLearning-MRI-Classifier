from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

# Allow access from any origin (optional, adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = tf.keras.models.load_model("brain_tumor_model.h5")

# Define labels based on your dataset order
labels = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    image = image.resize((150, 150))  # Match model input size
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)
    class_id = int(np.argmax(predictions))
    confidence = float(np.max(predictions))

    return {
        "class_id": class_id,
        "label": labels[class_id],
        "confidence": confidence
    }
