import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# === Load the trained model ===
model = load_model("model.h5")

# === Class names ===
class_names = [
    "damaged_infrastructure_earthquake",
    "damaged_infrastructure_infrastructure",
    "fire_disaster_urban_fire",
    "fire_disaster_wild_fire",
    "human_damage",
    "land_damage_drought",
    "land_damage_land_slide",
    "non_damage_human",
    "non_damage_buildings_street",
    "non_damage_wildfire_forest",
    "non_damage_sea",
    "water_damage",
]

# === Streamlit UI ===
st.set_page_config(page_title="Disaster Classification", page_icon="🌎")
st.title("🌎 Disaster Image Classification")
st.write("Upload an image to classify it into a disaster category.")

# === File uploader ===
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Preprocess image
    img = img.resize((225, 225))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Rescale

    # Predict
    with st.spinner("Classifying..."):
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions)]
        confidence = np.max(predictions) * 100

    # Display result
    st.success(f"**Predicted Class:** {predicted_class}")
    st.info(f"Confidence: {confidence:.2f}%")
