class LearningSystem:
    def __init__(self):
        self.feedback_data = []

    def store_feedback(self, user_feedback, job_role):
        """Store user feedback for learning purposes."""
        self.feedback_data.append({'feedback': user_feedback, 'role': job_role})

    def adjust_system(self):
        """Use feedback to adjust the rules and make better recommendations."""
        # Implement machine learning or rule-based adjustment here.
        for feedback in self.feedback_data:
            if feedback['feedback'] == 'positive':
                print(f"Improving recommendation for {feedback['role']} based on positive feedback.")
            elif feedback['feedback'] == 'negative':
                print(f"Adjusting recommendation for {feedback['role']} based on negative feedback.")
