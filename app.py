import streamlit as st
import base64

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        
        <style>
        
        
        .stApp {{
           background-image: url("data:image/webp;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image (Replace 'background.jpg' with your image file path)
set_background("bg2.webp")

st.markdown("""
            
    <style>
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        /* Main Glassmorphic Effect */
        .glass-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 80%;
            max-width: 600px;
            background: rgba(255, 255, 255, 0.1); /* Light Transparent White */
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px); /* Blur Effect */
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1); /* Soft Shadow */
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
          label {
            color: white !important;
        }
        /* Title Styling */
        .title {
            font-size: 40px;
            font-weight: bold;
            color: white;
            text-align: center;
            animation: fadeIn 2s ease-in-out;
        }

        /* Input and Buttons */
        .stSelectbox, .stNumberInput {
            transition: all 0.3s ease-in-out;
        }
        .stSelectbox:hover, .stNumberInput:hover {
            transform: scale(1.05);
        }
        .stButton button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            transition: all 0.3s ease-in-out;
        }
        .stButton button:hover {
            background-color: #ff1e1e;
            transform: scale(1.1);
        }
    </style>
    """, unsafe_allow_html=True)
st.markdown('<div class="glass-container">', unsafe_allow_html=True)
st.markdown("<div class='title'>🚀🔄 Advanced Unit Converter 🚀</div>", unsafe_allow_html=True)

# Add unit categories and conversion logic here (same as your existing code)


categories = {
    "🌐Area": ["Square Meters", "Square Kilometers", "Square Feet", "Square Miles", "Acres", "Hectares"],
    "📊Data Transfer Rate": ["Bits per Second", "Kilobits per Second", "Megabits per Second", "Gigabits per Second", "Terabits per Second"],
    "💿Digital Storage": ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"],
    "⚡Energy": ["Joules", "Kilojoules", "Calories", "Kilocalories", "Watt-hours", "Kilowatt-hours"],
    "🔄Frequency": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz", "Terahertz"],
    "⛽Fuel Economy": ["Miles per Gallon", "Kilometers per Liter", "Liters per 100 Kilometers"],
    "📏Length": ["Meters", "Kilometers", "Feet", "Miles", "Inches", "Centimeters", "Millimeters", "Yards"],
    "⚖ Mass": ["Grams", "Kilograms", "Pounds", "Ounces", "Tons", "Milligrams"],
    "✈📏Plane Angle": ["Degrees", "Radians", "Gradians"],
    "🌡 Pressure": ["Pascals", "Kilopascals", "Atmospheres", "Bar", "PSI"],
    "🚀Speed": ["Meters per Second", "Kilometers per Hour", "Miles per Hour", "Knots", "Feet per Second"],
    "🔥Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "⌚Time": ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"],
    "📦Volume": ["Liters", "Milliliters", "Cubic Meters", "Gallons", "Cubic Inches", "Cubic Feet"]
}


selected_category = st.selectbox("Select Category", list(categories.keys()))

# Input for value to convert
value = st.number_input("Enter Value", min_value=0.0, value=1.0)

# Dropdowns for selecting 'from' and 'to' units
from_unit = st.selectbox("From Unit", categories[selected_category])
to_unit = st.selectbox("To Unit", categories[selected_category])

# Conversion logic
def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "🌐Area": {
            "Square Meters": 1,
            "Square Kilometers": 1e-6,
            "Square Feet": 10.7639,
            "Square Miles": 3.861e-7,
            "Acres": 0.000247105,
            "Hectares": 0.0001
        },
        "📊Data Transfer Rate": {
            "Bits per Second": 1,
            "Kilobits per Second": 1e-3,
            "Megabits per Second": 1e-6,
            "Gigabits per Second": 1e-9,
            "Terabits per Second": 1e-12
        },
        "💿Digital Storage": {
            "Bytes": 1,
            "Kilobytes": 1e-3,
            "Megabytes": 1e-6,
            "Gigabytes": 1e-9,
            "Terabytes": 1e-12,
            "Petabytes": 1e-15
        },
        "⚡Energy": {
            "Joules": 1,
            "Kilojoules": 1e-3,
            "Calories": 0.239006,
            "Kilocalories": 0.000239006,
            "Watt-hours": 0.000277778,
            "Kilowatt-hours": 2.7778e-7
        },
        "🔄Frequency": {
            "Hertz": 1,
            "Kilohertz": 1e-3,
            "Megahertz": 1e-6,
            "Gigahertz": 1e-9,
            "Terahertz": 1e-12
        },
        "⛽Fuel Economy": {
            "Miles per Gallon": 1,
            "Kilometers per Liter": 0.425144,
            "Liters per 100 Kilometers": 235.215
        },
        "📏Length": {
            "Meters": 1,
            "Kilometers": 1e-3,
            "Feet": 3.28084,
            "Miles": 0.000621371,
            "Inches": 39.3701,
            "Centimeters": 100,
            "Millimeters": 1000,
            "Yards": 1.09361
        },
        "⚖ Mass": {
            "Grams": 1,
            "Kilograms": 1e-3,
            "Pounds": 0.00220462,
            "Ounces": 0.035274,
            "Tons": 1e-6,
            "Milligrams": 1000
        },
        "✈📏Plane Angle": {
            "Degrees": 1,
            "Radians": 0.0174533,
            "Gradians": 1.11111
        },
        "🌡 Pressure": {
            "Pascals": 1,
            "Kilopascals": 1e-3,
            "Atmospheres": 9.86923e-6,
            "Bar": 1e-5,
            "PSI": 0.000145038
        },
        "🚀Speed": {
            "Meters per Second": 1,
            "Kilometers per Hour": 3.6,
            "Miles per Hour": 2.23694,
            "Knots": 1.94384,
            "Feet per Second": 3.28084
        },
        "🔥Temperature": {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        },
        "⌚Time": {
            "Seconds": 1,
            "Minutes": 1/60,
            "Hours": 1/3600,
            "Days": 1/86400,
            "Weeks": 1/604800,
            "Months": 1/2.628e+6,
            "Years": 1/3.154e+7
        },
        "📦Volume": {
            "Liters": 1,
            "Milliliters": 1000,
            "Cubic Meters": 1e-3,
            "Gallons": 0.264172,
            "Cubic Inches": 61.0237,
            "Cubic Feet": 0.0353147
        }
    }
    if category == "🔥Temperature":
        converted_value = conversion_factors[category][to_unit](value) if callable(conversion_factors[category][to_unit]) else value
    else:
        converted_value = value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
    return round(converted_value, 4)

converted_value = convert_units(value, from_unit, to_unit, selected_category)
st.warning(f"Converted Value: {converted_value} {to_unit}")  # Red box