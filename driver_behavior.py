class DrivingPatternAnalyzer:
    def __init__(self, trip_log):
        self.trip_log = trip_log

    def compute_risk_index(self):
        danger_signals = 0
        total = len(self.trip_log)

        for entry in self.trip_log:
            limit = {
                'highway': 100,
                'city': 50,
                'residential': 30
            }.get(entry['road_type'], 50)

            if entry['speed'] > limit:
                danger_signals += 1
            if entry['braking'] < -5:
                danger_signals += 1
            if entry['acceleration'] > 3:
                danger_signals += 1
            if entry['time_of_day'] >= 22 or entry['time_of_day'] <= 5:
                danger_signals += 0.5

        if total == 0:
            return 0.0

        index = danger_signals / total
        return min(index, 1.0)
