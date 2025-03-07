import json
from difflib import SequenceMatcher


class RuleEngine:
    """
    A comprehensive inference engine for evaluating construction rules, providing suggestions,
    and handling dynamic rule extensions.
    """

    def __init__(self, rule_file):
        """
        Initializes the RuleEngine with a JSON-based rule file.

        Args:
            rule_file (str): Path to the JSON file containing rules.
        """
        self.rule_file = rule_file
        self.rules = self.load_rules()

    def load_rules(self):
        """
        Load rules from the rule file.

        Returns:
            list: List of rules loaded from the JSON file.
        """
        with open(self.rule_file, "r") as f:
            return json.load(f)

    def save_rules(self):
        """
        Save the current rules back to the rule file.
        """
        with open(self.rule_file, "w") as f:
            json.dump(self.rules, f, indent=4)

    def validate_rule(self, new_rule):
        """
        Validate a new rule before adding it to the knowledge base.

        Args:
            new_rule (dict): The rule to validate.

        Returns:
            bool: True if the rule is valid, False otherwise.
        """
        if "if" not in new_rule or "then" not in new_rule:
            return False  # Rule must contain 'if' and 'then' keys
        if not isinstance(new_rule["if"], dict) or not isinstance(new_rule["then"], dict):
            return False  # 'if' must be a dictionary and 'then' must be a dictionary
        return True

    def add_rule(self, new_rule):
        """
        Add a new rule to the knowledge base after validation.

        Args:
            new_rule (dict): The rule to add.

        Returns:
            str: Success or error message.
        """
        if not self.validate_rule(new_rule):
            return "Invalid rule format. Rule must contain 'if' (dict) and 'then' (dict)."

        self.rules.append(new_rule)
        self.save_rules()
        return "Rule successfully added to the knowledge base."

    def exact_match(self, criteria):
        """
        Find an exact match for the given criteria in the rules.

        Args:
            criteria (dict): The input conditions to evaluate.

        Returns:
            dict: The recommendation if an exact match is found.
        """
        for rule in self.rules:
            if all(criteria.get(key) == value for key, value in rule["if"].items()):
                return rule["then"]
        return None

    def score_rule(self, criteria, rule_conditions):
        """
        Calculate a match score for a rule based on the number of matching conditions.

        Args:
            criteria (dict): The input conditions.
            rule_conditions (dict): The conditions of the rule to evaluate.

        Returns:
            int: The score representing the number of matching conditions.
        """
        return sum(1 for key, value in rule_conditions.items() if criteria.get(key) == value)

    def find_closest_match(self, criteria):
        """
        Suggest the rule with the highest match score when no exact match is found.

        Args:
            criteria (dict): The input conditions to evaluate.

        Returns:
            tuple: (suggested_rule, match_score)
        """
        best_match = None
        highest_score = 0

        for rule in self.rules:
            score = self.score_rule(criteria, rule["if"])
            if score > highest_score:
                highest_score = score
                best_match = rule

        if best_match:
            return best_match["then"], highest_score
        return {"Concrete Grade": "N/A", "Steel Diameter (mm)": "N/A", "Beam Size (mm)": "N/A"}, 0

    def evaluate(self, criteria):
        """
        Evaluate the given criteria against the rules, prioritizing exact matches.

        Args:
            criteria (dict): The input conditions to evaluate.

        Returns:
            dict: The evaluation result, including suggestions if no exact match is found.
        """
        result = {
            "exact_match": None,
            "suggestion": None,
            "match_score": 0
        }

        # Check for exact match
        result["exact_match"] = self.exact_match(criteria)
        if result["exact_match"]:
            return result

        # If no exact match, find the closest match
        suggestion, score = self.find_closest_match(criteria)
        result["suggestion"] = suggestion
        result["match_score"] = score

        return result

    def similarity_ratio(self, str1, str2):
        """
        Calculate the similarity ratio between two strings using SequenceMatcher.

        Args:
            str1 (str): First string.
            str2 (str): Second string.

        Returns:
            float: Similarity ratio (0.0 to 1.0).
        """
        return SequenceMatcher(None, str1, str2).ratio()

    def suggest_improvements(self, criteria):
        """
        Suggest possible improvements to the input criteria by identifying common mismatches.

        Args:
            criteria (dict): The input conditions to evaluate.

        Returns:
            list: List of suggestions to improve the criteria.
        """
        suggestions = []
        for rule in self.rules:
            mismatched_keys = [
                key for key, value in rule["if"].items()
                if key in criteria and criteria[key] != value
            ]
            if mismatched_keys:
                suggestions.append({
                    "rule": rule["then"],
                    "mismatched_keys": mismatched_keys,
                    "correct_values": {key: rule["if"][key] for key in mismatched_keys}
                })
        return suggestions


# Example Usage
if __name__ == "__main__":
    engine = RuleEngine("knowledge_base/construction_rules.json")

    # Example criteria input from user
    user_criteria = {
        "Soil Type": "Clay",
        "Load-Bearing Capacity (kPa)": 75,
        "Moisture Content (%)": 25,
        "Floors": 3,
        "Area (sq. m)": 300,
        "Wind Speed (km/h)": 40,
        "Environment": "Corrosive"
    }

    # Evaluate criteria
    evaluation = engine.evaluate(user_criteria)
    if evaluation["exact_match"]:
        print("Exact Match Found:", evaluation["exact_match"])
    else:
        print("No exact match found.")
        print("Closest Suggestion:", evaluation["suggestion"])
        print("Match Score:", evaluation["match_score"])

    # Add a new rule
    new_rule = {
        "if": {
            "Soil Type": "Gravel",
            "Load-Bearing Capacity (kPa)": 350,
            "Moisture Content (%)": 5,
            "Floors": 7,
            "Area (sq. m)": 700,
            "Wind Speed (km/h)": 50,
            "Environment": "Normal"
        },
        "then": {
            "Concrete Grade": "M30",
            "Steel Diameter (mm)": "20 (Main), 14 (Secondary)",
            "Beam Size (mm)": "300 x 500"
        }
    }
    print(engine.add_rule(new_rule))

    # Suggest improvements to input
    suggestions = engine.suggest_improvements(user_criteria)
    for suggestion in suggestions:
        print("Suggestion:", suggestion)
