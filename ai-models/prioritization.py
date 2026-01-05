"""
AI Prioritization Logic - Placeholder
"""

def calculate_priority(debt_amount, overdue_days, complaint_count):
    """
    Returns a simple priority score based on rule-based logic
    """
    score = (debt_amount * 0.5) + (overdue_days * 0.3) - (complaint_count * 0.2)
    return max(score, 0)
