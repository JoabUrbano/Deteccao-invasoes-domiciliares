from timeEvaluation import TimeEvaluator
from bayes import BayesNet, enumeration_ask
from controlGate import controlGate

class CalcProbability:
    def __init__(self):
        self.time_evaluator = TimeEvaluator()
        self.controlGate = controlGate()

        self.rede = BayesNet([
            ('Invasion', [], 0.02),
            ('DetectionConfidenceHigh', ['Invasion'], {
                (True,): 0.9,
                (False,): 0.1  
            }),
            ('CriticalTime', ['Invasion'], {
                (True,): 0.9,
                (False,): 0.1
            }),
             ('ControlGate', ['Invasion'], {
                (True,): 0.1,
                (False,): 0.9
            })
        ])

    def calc_probability_invasion(self, confidence):
        if  confidence >= 0.7:
            confidence_high = True
        else:
            confidence_high = False
        
        time_weight = self.time_evaluator.get_time_weight()

        if time_weight >= 0.7:
            critical_time = True
        else:
            critical_time = False

        controlActived = self.controlGate.returnStateControl()

        evidence = {
            'DetectionConfidenceHigh': confidence_high,
            'CriticalTime': critical_time,
            'ControlGate': controlActived
        }

        result = enumeration_ask('Invasion', evidence, self.rede)
        return result[True]