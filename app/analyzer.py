import random

def analyze_contract(clauses):
    risk_levels = ["Low", "Medium", "High"]
    results = []
    for clause in clauses:
        # Placeholder logic: assign random risk
        risk = random.choice(risk_levels)
        results.append((clause, risk))
    return results
