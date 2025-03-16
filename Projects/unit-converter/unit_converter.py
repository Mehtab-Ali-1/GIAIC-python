import streamlit as st

def convert_units(unit_from, unit_to, value):
    conversions = {
        "meter_kilometer": 0.001,   # 1 meter = 0.001 kilometer
        "meter_centimeter": 100,    # 1 meter = 100 centimeters
        "meter_millimeter": 1000,   # 1 meter = 1000 millimeters
        "kilometer_meter": 1000,    # 1 kilometer = 1000 meters
        "kilometer_centimeter": 100000, # 1 kilometer = 100000 centimeters
        "kilometer_millimeter": 1000000, # 1 kilometer = 1000000 millimeters        
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        conversion = conversions[key]
        return value *conversion
    else:
        return "Conversion not found"

st.title("Unit Converter")

value = st.number_input("Enter the value to convert")

unit_from = st.selectbox("Select the unit to convert from", ["meter", "kilometer", "centimeter", "millimeter"])
unit_to = st.selectbox("Select the unit to convert to", ["meter", "kilometer", "centimeter", "millimeter"])

if st.button("Convert"):
    result = convert_units(unit_from, unit_to, value)
    st.success(f"The converted value is {result}")

