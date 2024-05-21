
import { useState } from 'react';

export default function Predict() {
  const initialState = {
    lon: '',
    lat: '',
    property_type: '',
    valuation_group: '',
    neighbourhood: '',
    property_age_2015: '',
    basement_finished: '',
    has_garage: '',
    has_fireplace: '',
    fully_complete: '',
    building_count: '',
    walkout_basement: '',
    air_conditioning: '',
    net_area: '',
    site_coverage: '',
    lot_size: '',
    tot_gross_area_description: '',
    Assessed_value_2015: ''
  };

  const [formData, setFormData] = useState(initialState);
  const [prediction, setPrediction] = useState(null);
  const [errors, setErrors] = useState({});
  const [apiError, setApiError] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const validate = () => {
    const newErrors = {};
    const numericFields = [
      'lon', 'lat', 'property_age_2015', 'net_area', 'site_coverage', 
      'lot_size', 'tot_gross_area_description', 'Assessed_value_2015'
    ];
    
    Object.keys(formData).forEach(key => {
      if (!formData[key]) {
        newErrors[key] = 'This field is required';
      } else if (numericFields.includes(key) && isNaN(formData[key])) {
        newErrors[key] = 'This field must be a number';
      }
    });
    return newErrors;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationErrors = validate();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }
    setErrors({});
    setApiError(null);
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify([formData])
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      const formattedPrediction = parseFloat(data.prediction[0]).toFixed(3).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
      setPrediction(formattedPrediction);
    } catch (error) {
      setApiError(`Error: ${error.message}`);
      console.error('Error fetching prediction:', error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 py-6">
      <h1 className="text-3xl font-bold mb-6">House Price Prediction</h1>
      <form className="bg-white p-6 rounded shadow-md w-full max-w-lg" onSubmit={handleSubmit}>
        <div className="grid grid-cols-2 gap-4">
          {Object.keys(initialState).map((key) => (
            <div key={key}>
              <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor={key}>
                {key.replace(/_/g, ' ')}
              </label>
              <input
                className={`shadow appearance-none border ${errors[key] ? 'border-red-500' : 'border-gray-300'} rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline`}
                id={key}
                name={key}
                type="text"
                value={formData[key]}
                onChange={handleChange}
              />
              {errors[key] && <p className="text-red-500 text-xs italic">{errors[key]}</p>}
            </div>
          ))}
        </div>
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mt-4"
          type="submit"
        >
          Predict
        </button>
      </form>
      {prediction && <p className="text-xl mt-6">Predicted Price: ${prediction}</p>}
      {apiError && <p className="text-red-500 text-xl mt-6">{apiError}</p>}
    </div>
  );
}
