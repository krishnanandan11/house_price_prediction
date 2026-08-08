import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("Bengaluru_House_Data.csv")

# Keep important columns
df = df[['location', 'size', 'total_sqft', 'bath', 'balcony', 'price']]

# Remove missing values
df.dropna(inplace=True)

print(df['location'].unique())

# Convert size like "2 BHK" → 2
df['size'] = df['size'].str.extract(r'(\d+)').astype(int)

# Function to convert sqft
def convert_sqft(x):
    if '-' in str(x):
        nums = x.split('-')
        return (float(nums[0]) + float(nums[1])) / 2
    try:
        return float(x)
    except:
        return None

# Apply cleaning
df['total_sqft'] = df['total_sqft'].apply(convert_sqft)

# Remove bad rows
df.dropna(inplace=True)

# Encode location
location_encoder = LabelEncoder()
df['location'] = location_encoder.fit_transform(df['location'])

# Features
X = df[['location', 'size', 'total_sqft', 'bath', 'balcony']]

# Target
y = df['price']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
pickle.dump((model, location_encoder), open("model.pkl", "wb"))

print("Model trained successfully")