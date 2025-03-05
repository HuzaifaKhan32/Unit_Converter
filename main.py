import streamlit as st
from datetime import datetime
import pandas as pd

PRESSURE_CONVERSIONS = {
        'pascals': 1,
        'kilopascals': 1000,
        'megapascals': 1e6,
        'bar': 1e5,
        'millibar': 100,
        'atmospheres': 101325,
        'torr': 133.322,
        'psi': 6894.76,
        'mmHg': 133.322,
        'inHg': 3386.39,
}

LENGTH_CONVERSIONS = {
        'meters': 1,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'kilometers': 1000,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34
}

TIME_CONVERSIONS = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'months': 2629800,  
        'years': 31557600,  
}

VOLUME_CONVERTIONS = {
        'liters': 1,
        'milliliters': 1000,
        'cubic_meters': 0.001,
        'cubic_centimeters': 1000,
        'cubic_inches': 61.0237,
        'cubic_feet': 0.0353147,
        'gallons': 0.264172,
        'quarts': 1.05669,
        'pints': 2.11338,
        'cups': 4.16667,
        'fluid_ounces': 33.814,
        'tablespoons': 67.628,
        'teaspoons': 202.884,
}

SPEED_CONVERTER = {
        'meter_per_second': 1,
        'kilometer_per_hour': 0.277778,  
        'miles_per_hour': 0.44704,     
        'knots': 0.514444,  # 
        'ft_per_second': 0.3048,     
}

if "history" not in st.session_state:
    st.session_state.history = []

def length_converter(value, from_unit, to_unit):
    

    if from_unit not in LENGTH_CONVERSIONS:
        st.write(f"Unsuported Unit: {from_unit}" )
    value_in_meters = value * LENGTH_CONVERSIONS[from_unit]

    if to_unit not in LENGTH_CONVERSIONS:
        st.write(f"Unsuported Unit: {to_unit}")
    converted_value = value_in_meters / LENGTH_CONVERSIONS[to_unit]
    return converted_value

def time_converter(value, from_unit, to_unit):
    

    if from_unit not in TIME_CONVERSIONS:
        st.write(f"Unsupported Unit: {from_unit}")
    elif to_unit not in TIME_CONVERSIONS:
        st.write(f"Unsupported Unit: {to_unit}")

    unit_to_seconds = value * TIME_CONVERSIONS[from_unit]
    converted_value = unit_to_seconds / TIME_CONVERSIONS[to_unit]

    return converted_value

st.title("Welcome To The Unit Converter⚖️")

st.sidebar.title("Unit Type⚖️")


def volume_converter(value, input_unit, output_unit):
    

    if input_unit not in VOLUME_CONVERTIONS:
        st.write(f"Unsupported Unit: {input_unit}")
    unit_to_liters = value * VOLUME_CONVERTIONS[input_unit]

    if output_unit not in VOLUME_CONVERTIONS:
        st.write(f"Unsupported Unit: {output_unit}")
    converted_value = unit_to_liters / VOLUME_CONVERTIONS[output_unit]
    return converted_value

def pressure_converter(value, input_unit, output_unit):


    if input_unit not in PRESSURE_CONVERSIONS:
        st.write(f"Unsupported Unit: {input_unit}")

    unit_to_pascal = value * PRESSURE_CONVERSIONS[input_unit]

    if output_unit not in PRESSURE_CONVERSIONS:
        st.write(f"Unsupported Unit: {output_unit}")
    converted_value = unit_to_pascal / PRESSURE_CONVERSIONS[output_unit]
    return converted_value


def speed_converter(value, input_unit, output_unit):
    
    if input_unit not in SPEED_CONVERTER:
        st.write(f"Unsupported Unit: {input_unit}")

    unit_to_meter_sec = value * SPEED_CONVERTER[input_unit]

    if output_unit not in SPEED_CONVERTER:
        st.write(f"Unsupported Unit: {output_unit}")
    converted_value = unit_to_meter_sec / SPEED_CONVERTER[output_unit]
    return converted_value

st.sidebar.markdown("Select Unit Type⚖️")
unit_type = st.sidebar.radio("", ["Length📏", "Temperature🌡️", "Time⌚", "Volume🧪", "Pressure 💨", "Speed 🏎"])

if unit_type == "Length📏":
    col1, col2 = st.columns(2)
    with col1:
        input_unit = st.selectbox("From:", list(LENGTH_CONVERSIONS.keys()))
    with col2:
        output_unit = st.selectbox("To:", list(LENGTH_CONVERSIONS.keys()))
    value = st.number_input("Enter The Value:")

    try:
        if st.button("Convert Unit 🔃"):
            result = length_converter(value, input_unit.lower(), output_unit.lower())
            result_message = f"{value} {input_unit} is equal to {result:.2f} {output_unit}"
            st.success(result_message)

            st.session_state.history.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "value": value,
                "from_unit": input_unit,
                "to_unit": output_unit,
                "converted_value": result
            })
    except:
        st.warning("Unit Converter Failed")

elif unit_type == "Temperature🌡️":
    col1, col2 = st.columns(2)

    with col1:
        input_unit = st.selectbox("From:", ["Celsius", "Kelvin", "Fahrenheit"])
    with col2:
        output_unit = st.selectbox("To:", ["Celsius", "Kelvin", "Fahrenheit"])
    value = st.number_input("Enter the value")
    
    if st.button("Convert Unit 🔃"):
        try:    
            if input_unit == output_unit:
                result = value
            elif input_unit == "Celsius":
                if output_unit == "Kelvin":
                    result = value + 273
                elif output_unit == "Fahrenheit":
                    result = (value * 9 / 5) + 32
            elif input_unit == "Kelvin":
                if output_unit == "Celsius":
                    result = value - 273
                elif output_unit == "Fahrenheit":
                    result = (value - 273) * 9/5 + 32
            elif input_unit == "Fahrenheit":
                if output_unit == "Celsius":
                    result = (value - 32) * 5/9 
                elif output_unit == "Kelvin":
                    result = (value - 32) * 5/9 + 273
            result_message = f"{value} {input_unit} is equal to {result:.2f} {output_unit}"
            st.success(result_message)
            st.session_state.history.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "value": value,
                "from_unit": input_unit,
                "to_unit": output_unit,
                "converted_value": result
            })
        except:
            st.warning("Unit Converter Failed")
elif unit_type == "Time⌚":
    col1, col2 = st.columns(2)

    with col1:
        input_unit = st.selectbox("From:", list(TIME_CONVERSIONS.keys()))
    with col2:
        output_unit = st.selectbox("To:", list(TIME_CONVERSIONS.keys()))
    value = st.number_input("Enter the value")
    if st.button("Convert Unit 🔃"):
        try:
            result = time_converter(value, input_unit.lower(), output_unit.lower())
            result_message = f"{value:.2f} {input_unit} is equal to {result:.2f} {output_unit}"
            st.success(result_message)
            st.session_state.history.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "value": value,
                "from_unit": input_unit,
                "to_unit": output_unit,
                "converted_value": result
            })
        except:
            st.warning("Unit Converter Failed")
elif unit_type == "Volume🧪":
    col1, col2 = st.columns(2)
    with col1:        
        input_unit = st.selectbox("From:", list(VOLUME_CONVERTIONS.keys()))
    with col2:
        output_unit = st.selectbox("To:", list(VOLUME_CONVERTIONS.keys()))

    value = st.number_input("Enter the value")
    if st.button("Convert Unit 🔃"):
        try:
            result = volume_converter(value, input_unit.lower(), output_unit.lower())
            result_message = f"{value:.2f} {input_unit} is equal to {result:.2f} {output_unit}"
            st.success(result_message)
            st.session_state.history.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "value": value,
                "from_unit": input_unit,
                "to_unit": output_unit,
                "converted_value": result
            })
        except:
            st.warning("Unit Converter Failed")
elif unit_type == "Pressure 💨":
    col1, col2 = st.columns(2)
    with col1:
        input_unit = st.selectbox("From:", list(PRESSURE_CONVERSIONS.keys()))
    with col2:
        output_unit = st.selectbox("To:", list(PRESSURE_CONVERSIONS.keys()))

    value = st.number_input("Enter the value")
    if st.button("Convert Unit 🔃"):
        try:
            result = pressure_converter(value, input_unit.lower(), output_unit.lower())
            result_message = f"{value:.2f} {input_unit} is equal to {result:.2f} {output_unit}"
            st.success(result_message)
            st.session_state.history.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "value": value,
                "from_unit": input_unit,
                "to_unit": output_unit,
                "converted_value": result
            })
        except:
            st.warning("Unit Converter Failed")
elif unit_type == "Speed 🏎":
    col1, col2 = st.columns(2)
    with col1:        
        input_unit = st.selectbox("From:", list(SPEED_CONVERTER.keys()))
    with col2:
        output_unit = st.selectbox("To:", list(SPEED_CONVERTER.keys()))

    value = st.number_input("Enter the value")
    if st.button("Convert Unit 🔃"):
        try:
            result = speed_converter(value, input_unit.lower(), output_unit.lower())
            result_message = f"{value:.2f} {input_unit} is equal to {result:.2f} {output_unit}"
            st.success(result_message)
            st.session_state.history.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "value": value,
                "from_unit": input_unit,
                "to_unit": output_unit,
                "converted_value": result
            })
        except:
            st.warning("Unit Converter Failed")
else:
    st.write("Sorry, no unit detected")
    
st.markdown("<br>", unsafe_allow_html=True)      
st.subheader("History")
if st.session_state.history:
    history_df = pd.DataFrame(st.session_state.history)
    st.table(history_df)

    csv = history_df.to_csv(index=False)
    st.download_button(
        label="Download History as CSV",
        data=csv,
        file_name="conversion_history.csv",
        mime="text/csv",
    )
    if st.button("Clear History"):
        st.session_state.history = []
else:
    st.write("No conversions yet.")


