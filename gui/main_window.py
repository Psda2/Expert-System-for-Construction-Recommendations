# gui/main_window.py

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QGroupBox, QFormLayout, QMessageBox, QStatusBar
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from utils.inference_engine import RuleEngine


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Construction Expert System")
        self.setFixedSize(1000, 700)
        self.setWindowIcon(QIcon("gui/resources/icon.png"))

        self.setup_ui()

    def setup_ui(self):
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main Layout
        main_layout = QVBoxLayout()

        # Title
        title_layout = QHBoxLayout()
        self.title_label = QLabel("Construction Expert System")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 28px; font-weight: bold; color: #000;")
        title_layout.addWidget(self.title_label)

        main_layout.addLayout(title_layout)

        # Input Form Group
        form_group = QGroupBox("Enter Construction Parameters")
        form_layout = QFormLayout()

        self.soil_type_input = QLineEdit()
        self.soil_type_input.setPlaceholderText("Enter soil type (e.g., Clay, Sand, Rock)")

        self.load_capacity_input = QLineEdit()
        self.load_capacity_input.setPlaceholderText("Enter load-bearing capacity (kPa)")

        self.moisture_content_input = QLineEdit()
        self.moisture_content_input.setPlaceholderText("Enter moisture content (%)")

        self.floors_input = QLineEdit()
        self.floors_input.setPlaceholderText("Enter number of floors")

        self.area_input = QLineEdit()
        self.area_input.setPlaceholderText("Enter area (sq. m)")

        self.wind_speed_input = QLineEdit()
        self.wind_speed_input.setPlaceholderText("Enter wind speed (km/h)")

        self.environment_input = QLineEdit()
        self.environment_input.setPlaceholderText("Enter environment (e.g., Normal, Coastal, Corrosive)")

        form_layout.addRow(QLabel("Soil Type:"), self.soil_type_input)
        form_layout.addRow(QLabel("Load-Bearing Capacity:"), self.load_capacity_input)
        form_layout.addRow(QLabel("Moisture Content:"), self.moisture_content_input)
        form_layout.addRow(QLabel("Floors:"), self.floors_input)
        form_layout.addRow(QLabel("Area:"), self.area_input)
        form_layout.addRow(QLabel("Wind Speed:"), self.wind_speed_input)
        form_layout.addRow(QLabel("Environment:"), self.environment_input)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # Buttons
        button_layout = QHBoxLayout()
        evaluate_button = QPushButton("Evaluate Design")
        evaluate_button.clicked.connect(self.evaluate_design)

        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset_fields)

        button_layout.addWidget(evaluate_button)
        button_layout.addWidget(reset_button)
        main_layout.addLayout(button_layout)

        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Set Layout
        central_widget.setLayout(main_layout)

    def evaluate_design(self):
        """
        Evaluate construction parameters using the RuleEngine.
        """
        criteria = {
            "soil_type": self.soil_type_input.text(),
            "load_capacity": self.load_capacity_input.text(),
            "moisture_content": self.moisture_content_input.text(),
            "floors": self.floors_input.text(),
            "area": self.area_input.text(),
            "wind_speed": self.wind_speed_input.text(),
            "environment": self.environment_input.text(),
        }

        rule_engine = RuleEngine("knowledge_base/construction_rules.json")
        result = rule_engine.evaluate(criteria)

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Evaluation Result")
        if result["exact_match"]:
            msg_box.setText(f"Recommended Design:\n{result['exact_match']}")
        else:
            msg_box.setText(
                f"No exact match found.\nSuggestion: {result['suggestion']}\nMatch Score: {result['match_score']}"
            )
        msg_box.exec_()

    def reset_fields(self):
        """
        Clear all input fields.
        """
        self.soil_type_input.clear()
        self.load_capacity_input.clear()
        self.moisture_content_input.clear()
        self.floors_input.clear()
        self.area_input.clear()
        self.wind_speed_input.clear()
        self.environment_input.clear()
        self.status_bar.showMessage("Fields Reset", 2000)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
