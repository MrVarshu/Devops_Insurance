import random
from data_collection import DataCollection
from behavior_analysis import BehaviorAnalysis
from risk_scoring import RiskScoring
from pricing_adjustment import PricingAdjustment
from feedback_system import FeedbackSystem

def generate_large_dataset(num_samples=1000):
    road_types = ['highway', 'city', 'residential']
    data = []

    for _ in range(num_samples):
        road = random.choice(road_types)
        
        # Speed distribution based on road type
        if road == 'highway':
            speed = random.gauss(100, 15)  # mean 100 km/h, std dev 15
        elif road == 'city':
            speed = random.gauss(50, 10)
        else:
            speed = random.gauss(30, 5)
        speed = max(0, min(speed, 150))  # clamp speed between 0 and 150
        
        # Acceleration between 0 and 5 m/s² (some harsh)
        acceleration = random.gauss(2, 1.5)
        acceleration = max(0, min(acceleration, 7))
        
        # Braking negative acceleration, between -8 and 0 (harsh braking possible)
        braking = random.gauss(-3, 2)
        braking = min(0, max(braking, -8))
        
        # Random time of day 0-23
        time_of_day = random.randint(0, 23)
        
        data.append((speed, acceleration, braking, time_of_day, road))

    return data

def main():
    collector = DataCollection()
    large_data = generate_large_dataset(num_samples=1000)

    for sample in large_data:
        collector.add_telematics_data(*sample) 

    all_data = collector.get_all_data()

    analyzer = BehaviorAnalysis(all_data)
    risk_factor = analyzer.analyze()

    scorer = RiskScoring(risk_factor)
    risk_score = scorer.compute_score()

    pricing = PricingAdjustment(base_premium=500)
    adjusted_premium = pricing.adjust_premium(risk_score)

    feedback = FeedbackSystem(all_data)
    recommendations = feedback.generate_recommendations()

    print(f"Risk Score: {risk_score:.2f}")
    print(f"Adjusted Premium: ${adjusted_premium}")
    print("Safety Recommendations:")
    for rec in recommendations:
        print("-", rec)

if __name__ == "__main__":
    main()
