class PricingAdjustment:
    def __init__(self, base_premium=500):
        self.base_premium = base_premium

    def adjust_premium(self, risk_score):
        # Premium increases up to 50% proportional to risk score
        premium = self.base_premium * (1 + 0.5 * risk_score)
        return round(premium, 2)
