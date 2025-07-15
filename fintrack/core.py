from datetime import datetime

class Transaction:
    def __init__(self, amount: float, category: str, date: str = None):
        self.amount = amount
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d") if date else datetime.now()

    def __repr__(self):
        return f"<Transaction ${self.amount} - {self.category} on {self.date.strftime('%Y-%m-%d')}>"
