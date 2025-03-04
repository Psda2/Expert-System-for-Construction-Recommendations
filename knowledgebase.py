class KnowledgeBase:
    def __init__(self):
        self.rules = [
            {
                "Soil Type": "Clay",
                "Load-Bearing Capacity (kPa)": 50,
                "Moisture Content (%)": 20,
                "Floors": 2,
                "Area (sq. m)": 150,
                "Wind Speed (km/h)": 30,
                "Environment": "Normal",
                "Concrete Grade": "M20",
                "Steel Diameter (mm)": "12 (Main), 8 (Secondary)",
                "Beam Size (mm)": "230 x 300",
            },
            {
                "Soil Type": "Sand",
                "Load-Bearing Capacity (kPa)": 150,
                "Moisture Content (%)": 10,
                "Floors": 5,
                "Area (sq. m)": 500,
                "Wind Speed (km/h)": 50,
                "Environment": "Coastal",
                "Concrete Grade": "M25",
                "Steel Diameter (mm)": "16 (Main), 10 (Secondary)",
                "Beam Size (mm)": "230 x 450",
            },
            {
                "Soil Type": "Rock",
                "Load-Bearing Capacity (kPa)": ">2000",
                "Moisture Content (%)": 5,
                "Floors": 10,
                "Area (sq. m)": 1000,
                "Wind Speed (km/h)": 60,
                "Environment": "Normal",
                "Concrete Grade": "M30",
                "Steel Diameter (mm)": "20 (Main), 12 (Secondary)",
                "Beam Size (mm)": "300 x 600",
            },
            {
                "Soil Type": "Clay",
                "Load-Bearing Capacity (kPa)": 75,
                "Moisture Content (%)": 25,
                "Floors": 3,
                "Area (sq. m)": 300,
                "Wind Speed (km/h)": 40,
                "Environment": "Corrosive",
                "Concrete Grade": "M25",
                "Steel Diameter (mm)": "16 (Main), 10 (Secondary)",
                "Beam Size (mm)": "230 x 450",
            },
            {
                "Soil Type": "Silt",
                "Load-Bearing Capacity (kPa)": 100,
                "Moisture Content (%)": 15,
                "Floors": 4,
                "Area (sq. m)": 400,
                "Wind Speed (km/h)": 35,
                "Environment": "Normal",
                "Concrete Grade": "M20",
                "Steel Diameter (mm)": "14 (Main), 10 (Secondary)",
                "Beam Size (mm)": "230 x 400",
            },
            {
                "Soil Type": "Sand",
                "Load-Bearing Capacity (kPa)": 200,
                "Moisture Content (%)": 8,
                "Floors": 8,
                "Area (sq. m)": 800,
                "Wind Speed (km/h)": 80,
                "Environment": "Coastal",
                "Concrete Grade": "M30",
                "Steel Diameter (mm)": "20 (Main), 16 (Secondary)",
                "Beam Size (mm)": "300 x 600",
            },
            {
                "Soil Type": "Gravel",
                "Load-Bearing Capacity (kPa)": 300,
                "Moisture Content (%)": 5,
                "Floors": 6,
                "Area (sq. m)": 600,
                "Wind Speed (km/h)": 45,
                "Environment": "Normal",
                "Concrete Grade": "M25",
                "Steel Diameter (mm)": "18 (Main), 12 (Secondary)",
                "Beam Size (mm)": "250 x 500",
            },
        ]

    def get_rules(self):
        return self.rules
