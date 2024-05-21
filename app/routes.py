# routes.py
from flask import Blueprint, request, jsonify
from .model import load_model
import pandas as pd

main = Blueprint('main', __name__)
model = load_model()

@main.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if isinstance(data, dict):
            df = pd.DataFrame([data])
        else:
            df = pd.DataFrame(data)

        # Ensure all expected columns are present in the DataFrame
        expected_columns = [
            'lon', 'lat', 'property_type', 'valuation_group', 'neighbourhood',
            'property_age_2015', 'basement_finished', 'has_garage', 'has_fireplace',
            'fully_complete', 'building_count', 'walkout_basement', 'air_conditioning', 
            'net_area', 'site_coverage', 'lot_size', 'tot_gross_area_description', 
            'Assessed_value_2015'
        ]
        for col in expected_columns:
            if col not in df.columns:
                df[col] = 0

        # Convert columns to appropriate types
        df['lon'] = pd.to_numeric(df['lon'], errors='coerce')
        df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
        df['property_age_2015'] = pd.to_numeric(df['property_age_2015'], errors='coerce')
        df['net_area'] = pd.to_numeric(df['net_area'], errors='coerce')
        df['site_coverage'] = pd.to_numeric(df['site_coverage'], errors='coerce')
        df['lot_size'] = pd.to_numeric(df['lot_size'], errors='coerce')
        df['tot_gross_area_description'] = pd.to_numeric(df['tot_gross_area_description'], errors='coerce')
        df['Assessed_value_2015'] = pd.to_numeric(df['Assessed_value_2015'], errors='coerce')

        # Convert categorical columns to string
        categorical_features = ['property_type', 'valuation_group', 'neighbourhood', 
                                'basement_finished', 'has_garage', 'has_fireplace', 
                                'fully_complete', 'building_count', 'walkout_basement', 
                                'air_conditioning']
        df[categorical_features] = df[categorical_features].astype(str)

        # Fill NaN values
        df = df.fillna(0)

        prediction = model.predict(df)
        
        inflation_adjustment_factor = 1.2547  
        adjusted_prediction = prediction * inflation_adjustment_factor
        adjusted_prediction = [f"{x:,.3f}" for x in adjusted_prediction]  # Format prediction
        return jsonify({'prediction': adjusted_prediction})
    except Exception as e:
        return jsonify({'error': str(e)})
