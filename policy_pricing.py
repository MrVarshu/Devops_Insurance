class PremiumCalculator:
    def __init__(self, base_amount=500):
        self.base_amount = base_amount

    def calculate_final(self, risk_value):
        updated_premium = self.base_amount * (1 + 0.5 * risk_value)
        return round(updated_premium, 2)
