import streamlit as st

def length_converter(value, from_unit, to_unit):
    units_to_meters = {
        'meters': 1,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'kilometers': 1000,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34
    }

    if from_unit not in units_to_meters:
        st.write(f"Unsuported Unit: {from_unit}" )
    value_in_meters = value * units_to_meters[from_unit]

    if to_unit not in units_to_meters:
        st.write(f"Unsuported Unit: {to_unit}")
    converted_value = value_in_meters / units_to_meters[to_unit]
    return converted_value

def time_converter(value, from_unit, to_unit):
    conversions = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'months': 2629800,  # Approximate: 1 month = 30.44 days
        'years': 31557600,  # Approximate: 1 year = 365.25 days
    }

    if from_unit not in conversions:
        st.write(f"Unsupported Unit: {from_unit}")
    elif to_unit not in conversions:
        st.write(f"Unsupported Unit: {to_unit}")

    unit_to_seconds = value * conversions[from_unit]
    converted_value = unit_to_seconds / conversions[to_unit]

    return converted_value

st.title("Unit Converter⚖️")

st.sidebar.title("Unit Type⚖️")


def volume_converter(value, input_unit, output_unit):
    conversions = {
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

    if input_unit not in conversions:
        st.write(f"Unsupported Unit: {input_unit}")
    unit_to_liters = value * conversions[input_unit]

    if output_unit not in conversions:
        st.write(f"Unsupported Unit: {output_unit}")
    converted_value = unit_to_liters / conversions[output_unit]
    return converted_value


unit_type = st.sidebar.selectbox("Select Unit Type", ["Length📏", "Temperature🌡️", "Time⌚", "Volume🧪"])

if unit_type == "Length📏":
    input_unit = st.selectbox("From:", ["Meters", "Centimeters", "Kilometers", "Millimeters", "Feet", "Inches", "Yards", "Miles"])
    output_unit = st.selectbox("To:", ["Meters", "Centimeters", "Kilometers", "Millimeters", "Feet", "Inches", "Yards", "Miles"])
    value = st.number_input("Enter The Value:")

    try:
        if st.button("Convert Unit 🔃"):
            result = length_converter(value, input_unit.lower(), output_unit.lower())
            result_message = f"{value} {input_unit} is equal to {result:.2f} {output_unit}"
            st.success(result_message)
    except:
        st.warning("Unit Converter Failed")

elif unit_type == "Temperature🌡️":
    input_unit = st.selectbox("From:", ["Celsius", "Kelvin", "Fahrenheit"])
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
        except:
            st.warning("Unit Converter Failed")
elif unit_type == "Time⌚":
    input_unit = st.selectbox("From:", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])
    output_unit = st.selectbox("To:", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])
    value = st.number_input("Enter the value")
    if st.button("Convert Unit 🔃"):
        try:
            result = time_converter(value, input_unit.lower(), output_unit.lower())
            result_message = f"{value:.2f} {input_unit} is equal to {result:.2f} {output_unit}"
            st.success(result_message)
        except:
            st.warning("Unit Converter Failed")
elif unit_type == "Volume🧪":
    input_unit = st.selectbox("From:", ["Liters", "Milliliters", "Cubic_Meter", "Cubic_Centimeters", "Cubic_Inches", "Cubic_Feet", "Gallons", "Quarts", "Pint", "Cups", "Fluid_Ounces", "Tablespoons", "Teaspoons"])
    output_unit = st.selectbox("To:", ["Liters", "Milliliters", "Cubic_Meter", "Cubic_Centimeters", "Cubic_Inches", "Cubic_Feet", "Gallons", "Quarts", "Pint", "Cups", "Fluid_Ounces", "Tablespoons", "Teaspoons"])
    
    value = st.number_input("Enter the value")
    if st.button("Convert Unit 🔃"):
        try:
            result = volume_converter(value, input_unit.lower(), output_unit.lower())
            result_message = f"{value:.2f} {input_unit} is equal to {result:.2f} {output_unit}"
            st.success(result_message)
        except:
            st.warning("Unit Converter Failed")

    
      



