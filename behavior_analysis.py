class BehaviorAnalysis:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        risky_events = 0
        total_events = len(self.data)

        for d in self.data:
            speed_limit = {
                'highway': 100,
                'city': 50,
                'residential': 30
            }.get(d['road_type'], 50)

            if d['speed'] > speed_limit:
                risky_events += 1
            if d['braking'] < -5:
                risky_events += 1
            if d['acceleration'] > 3:
                risky_events += 1
            if d['time_of_day'] >= 22 or d['time_of_day'] <= 5:
                risky_events += 0.5

        risk_factor = risky_events / (total_events if total_events else 1)
        return min(risk_factor, 1.0)
