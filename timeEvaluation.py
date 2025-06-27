from datetime import datetime

class TimeEvaluator:
    def __init__(self):
        pass

    def get_time_weight(self):

        hour = datetime.now().hour
        
        if 22 <= hour <= 24 or 5 > hour >= 0:
            return 0.9
        elif 20 <= hour < 22:
            return 0.6
        elif 5 <= hour < 7 or 18 <= hour < 20:
            return 0.4
        else:
            return 0.1

