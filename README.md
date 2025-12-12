# 🌋 Disaster Classification using CNN

This project uses a Convolutional Neural Network (CNN) to classify different types of disasters from images: such as fires, earthquakes, floods, and non-damage scenes.

## 🧠 Project Overview 

The CNN model is trained on a custom dataset organized into multiple disaster categories.
It automatically classifies input images into one of several disaster types.

## 📂 Dataset Structure

```mathematica
Dataset/
│── damaged_infrastructure/
│   ├── earthquake/
│   └── infrastructure/
│── fire_disaster/
│   ├── urban_fire/
│   └── wild_fire/
│── human_damage/
│── land_damage/
│   ├── drought/
│   └── land_slide/
│── non_damage/
│   ├── human/
│   ├── buildings_street/
│   ├── wildfire_forest/
│   └── sea/
└── water_damage/
```

The dataset is split into `train/`, `validation/`, and `test/` sets before training. You can get this dataset from [Kaggle](https://www.kaggle.com/datasets/varpit94/disaster-images-dataset)

## ⚙️ Requirements

Install dependencies:

```bash
pip install tensorflow pillow matplotlib seaborn streamlit
```

## 🚀 Training

Run the training script:

```bash
# Run all the cells in the train.ipynb notebook
```

The trained model will be saved as `model.h5`.

## 🖼️ Streamlit App

Launch the web interface to classify disaster images:

```bash
streamlit run app.py
```

Upload an image - the app predicts the disaster category.

## 🧹 Notes

If you face training errors, use the included cleanup script to remove corrupted images:

```bash
python clean_up.py
```
