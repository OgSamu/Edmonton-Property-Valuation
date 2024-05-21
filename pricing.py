import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
import joblib
house_data = pd.read_csv(r"C:\Users\ogosa\OneDrive\Desktop\LiveHousePricingSystem\Edmonton_house_price_data.csv")


# Function to convert columns to numeric, coercing errors to NaN
def to_numeric(series):
    return pd.to_numeric(series, errors='coerce')

# List of numeric columns
numeric_columns = ['property_age_2015', 'net_area', 'site_coverage', 
                   'lot_size', 'tot_gross_area_description', 'Assessed_value_2015', 'Assessed_value_2016']

# Apply to_numeric to all the columns that should be numeric
house_data[numeric_columns] = house_data[numeric_columns].apply(to_numeric)

# Handle missing values based on the improved strategy
house_data["property_age_2015"].fillna(house_data["property_age_2015"].median(), inplace=True)
house_data["fully_complete"].fillna("missing", inplace=True)
house_data["property_type"].fillna("missing", inplace=True)
house_data["walkout_basement"].fillna("missing", inplace=True)
house_data["net_area"].fillna(house_data["net_area"].median(), inplace=True)
house_data["site_coverage"].fillna(house_data["site_coverage"].median(), inplace=True)
house_data["tot_gross_area_description"].fillna(house_data["tot_gross_area_description"].median(), inplace=True)
house_data["lot_size"].fillna(house_data["lot_size"].median(), inplace=True)  # Change strategy to median for consistency

# Check if the missing values have been handled
missing_values = house_data.isnull().sum()
print(missing_values[missing_values > 0])

# Verify data types
print(house_data.dtypes)

house_data.isna().sum()


#split into x / y 
x = house_data.drop("Assessed_value_2016", axis = 1)
y = house_data["Assessed_value_2016"]

#split into train and test set 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score, cross_val_predict


# Define features and target
X = house_data[['lon', 'lat', 'property_type', 'valuation_group', 'neighbourhood', 
                'property_age_2015', 'basement_finished', 'has_garage', 'has_fireplace',
                'fully_complete', 'building_count', 'walkout_basement', 'air_conditioning', 
                'net_area', 'site_coverage', 'lot_size', 'tot_gross_area_description', 
                'Assessed_value_2015']]
y = house_data['Assessed_value_2016']

# Combine X and y for consistent outlier removal
combined = pd.concat([X, y], axis=1)

# Function to remove outliers using the IQR method
def remove_outliers(df, numeric_cols):
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df

# Combine X and y for consistent outlier removal
combined = pd.concat([X, y], axis=1)

# Function to remove outliers using the IQR method
def remove_outliers(df, numeric_cols):
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df

# Remove outliers from the combined dataset
combined = remove_outliers(combined, numeric_columns)

numeric_columns = ['property_age_2015', 'net_area', 'site_coverage', 
                   'lot_size', 'tot_gross_area_description', 'Assessed_value_2015']
# Separate features and target after removing outliers
X = combined.drop(columns=['Assessed_value_2016'])
y = combined['Assessed_value_2016']

# Convert all categorical features to string using .loc to avoid SettingWithCopyWarning
categorical_features = ['property_type', 'valuation_group', 'neighbourhood', 
                        'basement_finished', 'has_garage', 'has_fireplace', 
                        'fully_complete', 'building_count', 'walkout_basement', 'air_conditioning']
X.loc[:, categorical_features] = X[categorical_features].astype(str)

# Preprocessing pipeline for numeric and categorical features
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_columns),
        ('cat', categorical_transformer, categorical_features)])

# Define the model pipeline with preprocessing and model training
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', Ridge())
])

# Train the model
model_pipeline.fit(X, y)

# Save the model
joblib.dump(model_pipeline, 'house_price_model.pkl')

