# Bengaluru House Price Prediction

A machine learning project that predicts house prices in Bengaluru based on property-related features such as location, size, total square footage, number of bathrooms, and balconies.

## Project Status

**Completed**

## Features

* Predicts house prices based on property details
* Handles categorical location data
* Uses property size and area-related features
* Includes data preprocessing and model training
* Provides price predictions for new property inputs

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

### Machine Learning

* Random Forest Regression
* Label Encoding

## Dataset

The project uses the **Bengaluru House Data** dataset.

### Main Features

* `location` — Location of the property
* `size` — Number of bedrooms/BHK
* `total_sqft` — Total area of the property
* `bath` — Number of bathrooms
* `balcony` — Number of balconies
* `price` — Property price

## Machine Learning Workflow

1. Load the Bengaluru house price dataset.
2. Explore and understand the dataset.
3. Clean missing and inconsistent data.
4. Convert categorical location data into numerical values.
5. Select relevant features for prediction.
6. Split the dataset into training and testing sets.
7. Train a Random Forest Regression model.
8. Evaluate the model.
9. Use the trained model to predict house prices for new properties.

## Project Structure

```text
Bengaluru-House-Price-Prediction/
│
├── Bengaluru_House_Data.csv
├── house_price_prediction.py
├── requirements.txt
├── README.md
│
└── model/
    └── house_price_model.pkl
```

## Example Prediction

The model can take property details such as:

```text
Location: Whitefield
Size: 2 BHK
Total Sqft: 1200
Bathrooms: 2
Balcony: 1
```

and generate an estimated house price based on the trained machine learning model.

## Future Improvements

* Improve prediction accuracy through feature engineering
* Compare multiple regression algorithms
* Add a web interface for easier predictions
* Add interactive data visualizations
* Deploy the prediction model as a web application
* Add more property-related features

## Project Goal

The goal of this project is to apply machine learning techniques to a real-world housing dataset and build a model capable of estimating property prices in Bengaluru.

## Author

**Krishna Nandan**

BCA (AI & Data Science) | Aspiring Data Analyst
