from datetime import datetime

class TimeEvaluator:
    def __init__(self):
        pass

    def get_time_weight(self):

        hour = datetime.now().hour
        
        if 22 <= hour <= 24 or 5 > hour >= 0:
            return "Critical"
        elif 5 <= hour < 7 or 18 <= hour < 22:
            return "Medium"
        else:
            return "Low"

