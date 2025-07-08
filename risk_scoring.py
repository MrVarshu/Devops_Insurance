class RiskScoring:
    def __init__(self, risk_factor):
        self.risk_factor = risk_factor

    def compute_score(self):
        # For now, risk factor itself is score (0 to 1)
        return self.risk_factor
