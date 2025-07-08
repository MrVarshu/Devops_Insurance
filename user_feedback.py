import numpy as np

class AdviceEngine:
    def __init__(self, driving_data):
        self.driving_data = driving_data

    def suggest_tips(self):
        tips = []

        if not self.driving_data:
            return ["Insufficient driving data to analyze."]

        avg_speed = np.mean([d['speed'] for d in self.driving_data])
        avg_brake = np.mean([d['braking'] for d in self.driving_data])

        if avg_speed > 80:
            tips.append("Try maintaining a lower average speed for safer driving.")
        if avg_brake < -3:
            tips.append("Avoid sudden braking to prevent accidents.")
        if any(entry['time_of_day'] >= 22 or entry['time_of_day'] <= 5 for entry in self.driving_data):
            tips.append("Night driving requires extra caution. Be alert.")

        if not tips:
            tips.append("Your driving looks good overall. Keep it up!")

        return tips
