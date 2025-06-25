from timeEvaluation import TimeEvaluator

class CalcProbability:
    def __init__(self):
        self.time_evaluator = TimeEvaluator()

    def calc_probability_invasion(self, confidence):
        """
        :param confidence: float entre 0 e 1 (ex: 0.85)
        :param hour: opcional - hora da detecção para fins de teste
        :return: probabilidade final de invasão
        """

        time_weight = self.time_evaluator.get_time_weight()

        # Combinação de fatores (simplificada):
        # A confiança é ponderada pelo peso do horário
        probability = confidence * time_weight

        # Ajuste de probabilidade para deixar mais realista
        # Exemplo: aumentar sensibilidade em horários críticos
        if time_weight >= 0.8 and confidence > 0.7:
            probability += 0.1  # pequeno bônus de risco

        # Garantir que o valor fique entre 0 e 1
        return min(probability, 1.0)
