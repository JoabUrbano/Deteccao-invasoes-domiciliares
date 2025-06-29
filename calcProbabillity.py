from timeEvaluation import TimeEvaluator
from bayes import BayesNet, enumeration_ask
from controlGate import controlGate
from markov import Markov

class CalcProbability:
    def __init__(self):
        self.time_evaluator = TimeEvaluator()
        self.controlGate = controlGate()

        self.rede = BayesNet([
            ('Invasion', [], 0.02),
            ('DetectionConfidenceHigh', ['Invasion'], {
                (True,): 0.95,
                (False,): 0.05  
            }),
            ('CriticalTime', ['Invasion'], {
                (True,): 0.85,
                (False,): 0.15
            }),
             ('ControlGate', ['Invasion'], {
                (True,): 0.15,
                (False,): 0.85
            })
        ])

        self.markov = Markov()

    def calc_probability_invasion(self, confidence):
        if  confidence >= 0.7:
            confidence_high = True
        else:
            confidence_high = False
        
        time_weight = self.time_evaluator.get_time_weight()

        if time_weight == "Critical" or time_weight == "Medium":
            critical_time = True
        else:
            critical_time = False

        controlActived = self.controlGate.returnStateControl()
        
        self.markov.stateTransition(controlActived, confidence, time_weight)

        evidence = {
            'DetectionConfidenceHigh': confidence_high,
            'CriticalTime': critical_time,
            'ControlGate': controlActived
        }

        result = enumeration_ask('Invasion', evidence, self.rede)

        invasion_prob = result[True]*100
        if invasion_prob < 45:
            print(f"Baixa chance de invasão {invasion_prob:.2f}%")
        elif invasion_prob >= 45 and invasion_prob < 65:
            print(f"Média chance de invasão {invasion_prob:.2f}%")
        else:
            print(f"Chance crítica de invasão invasão {invasion_prob:.2f}%")