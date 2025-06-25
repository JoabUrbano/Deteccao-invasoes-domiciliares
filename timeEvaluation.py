from datetime import datetime

class TimeEvaluator:
    def __init__(self):
        pass

    def get_time_weight(self):

        hour = datetime.now().hour
        
        if 2 <= hour < 4:
            return 1.0
        elif 0 <= hour < 2 or 4 <= hour < 6:
            return 0.8
        elif 20 <= hour < 24:
            return 0.6
        elif 6 <= hour < 8 or 18 <= hour < 20:
            return 0.4
        else:
            return 0.2

