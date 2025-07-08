class DataCollection:
    def __init__(self):
        self.data = []

    def add_telematics_data(self, speed, acceleration, braking, time_of_day, road_type):
        """
        Parameters:
        - speed (km/h)
        - acceleration (m/s²)
        - braking (m/s², negative)
        - time_of_day (0-23)
        - road_type ('highway', 'city', 'residential')
        """
        self.data.append({
            'speed': speed,
            'acceleration': acceleration,
            'braking': braking,
            'time_of_day': time_of_day,
            'road_type': road_type
        })

    def get_all_data(self):
        return self.data
