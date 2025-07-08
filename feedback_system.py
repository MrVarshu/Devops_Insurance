import numpy as np

class FeedbackSystem:
    def __init__(self, data):
        self.data = data

    def generate_recommendations(self):
        recommendations = []
        if not self.data:
            return ["No data available for recommendations."]

        avg_speed = np.mean([d['speed'] for d in self.data])
        avg_braking = np.mean([d['braking'] for d in self.data])

        if avg_speed > 80:
            recommendations.append("Reduce your average speed to improve safety and lower premiums.")
        if avg_braking < -3:
            recommendations.append("Avoid harsh braking to reduce accident risk.")
        if any(d['time_of_day'] >= 22 or d['time_of_day'] <= 5 for d in self.data):
            recommendations.append("Be extra cautious when driving at night.")

        if not recommendations:
            recommendations.append("Great driving! Keep it up.")

        return recommendations

