import random
from data_handler import TelematicsLogger
from driver_behavior import DrivingPatternAnalyzer
from risk_evaluator import RiskEvaluator
from policy_pricing import PremiumCalculator
from user_feedback import AdviceEngine

def simulate_driving_data(samples=1000):
    roads = ['highway', 'city', 'residential']
    output = []

    for _ in range(samples):
        road = random.choice(roads)

        speed = random.gauss(100, 15) if road == 'highway' else (
                random.gauss(50, 10) if road == 'city' else random.gauss(30, 5))
        speed = max(0, min(speed, 150))

        accel = max(0, min(random.gauss(2, 1.5), 7))
        brake = max(-8, min(random.gauss(-3, 2), 0))
        hour = random.randint(0, 23)

        output.append((speed, accel, brake, hour, road))

    return output

def run_analysis():
    logger = TelematicsLogger()
    dataset = simulate_driving_data()

    for record in dataset:
        logger.log_trip_data(*record)

    all_logs = logger.fetch_all()

    analyzer = DrivingPatternAnalyzer(all_logs)
    risk_idx = analyzer.compute_risk_index()

    evaluator = RiskEvaluator(risk_idx)
    score = evaluator.get_score()

    calculator = PremiumCalculator(500)
    premium = calculator.calculate_final(score)

    advisor = AdviceEngine(all_logs)
    suggestions = advisor.suggest_tips()

    print(f"Computed Risk Score: {score:.2f}")
    print(f"Estimated Premium: ₹{premium}")
    print("Driving Suggestions:")
    for msg in suggestions:
        print("-", msg)

if __name__ == "__main__":
    run_analysis()
