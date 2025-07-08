class TelematicsLogger:
    def __init__(self):
        self.records = []

    def log_trip_data(self, speed, accel, brake, hour, road_env):
        """
        Records one driving event.
        :param speed: current speed (km/h)
        :param accel: acceleration (m/s²)
        :param brake: braking force (m/s²), should be negative
        :param hour: time of day (0-23)
        :param road_env: one of 'highway', 'city', 'residential'
        """
        self.records.append({
            'speed': speed,
            'acceleration': accel,
            'braking': brake,
            'time_of_day': hour,
            'road_type': road_env
        })

    def fetch_all(self):
        return self.records
