def preprocess_input(input_data):
    """Preprocess input data to ensure correct data types and structure."""
    try:
        input_data["loadBearingCapacity"] = int(input_data["loadBearingCapacity"])
        input_data["moistureContent"] = int(input_data["moistureContent"])
        input_data["floors"] = int(input_data["floors"])
        input_data["area"] = int(input_data["area"])

        if isinstance(input_data["windSpeed"], str) and "-" in input_data["windSpeed"]:
            wind_speed_range = input_data["windSpeed"].split("-")
            input_data["windSpeed"] = (int(wind_speed_range[0].strip()), int(wind_speed_range[1].strip()))

        return input_data
    except Exception as e:
        raise ValueError(f"Error during preprocessing: {e}")
