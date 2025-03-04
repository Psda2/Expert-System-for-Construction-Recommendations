class InferenceEngine:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def infer(self, inputs):
        for rule in self.knowledge_base.get_rules():
            if all(rule[key] == value or rule[key] == f">{value}" for key, value in inputs.items() if key in rule):
                return {
                    "Concrete Grade": rule["Concrete Grade"],
                    "Steel Diameter (mm)": rule["Steel Diameter (mm)"],
                    "Beam Size (mm)": rule["Beam Size (mm)"],
                }
        return None
