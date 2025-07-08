class RiskEvaluator:
    def __init__(self, risk_metric):
        self.risk_metric = risk_metric

    def get_score(self):
        return self.risk_metric  # Direct mapping for simplicity