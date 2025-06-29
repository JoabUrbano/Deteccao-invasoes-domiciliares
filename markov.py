import numpy as np

class Markov:
    def __init__(self):
        self.estados = [0, 1, 2]  # 0=Chance baixa, 1=Chance média, 2=Chance alta

        self.transicoes_base = np.array([
            [0.7, 0.2, 0.1],
            [0.3, 0.4, 0.3],
            [0.2, 0.3, 0.5]
        ])

        self.estado_atual = np.array([0.8, 0.1, 0.1])

    def adjustTransitionsWithSensors(self, controllGate, confidence, hour):
        """
        Aumenta chance de ir para 'Chuvoso' se temperatura estiver baixa.
        """
        transicoes = self.transicoes_base.copy()

        if controllGate == False and confidence > 0.70 and hour == "Critical":
            transicoes[:,2] += 0.8
        elif controllGate == False and confidence < 0.70 and confidence > 0.55 and hour == "Critical":
            transicoes[:,2] += 0.4
        elif controllGate == False and confidence > 0.70 and hour == "Medium":
            transicoes[:,2] += 0.12
        else:
            transicoes[:,0] += 0.8

        # Normaliza as linhas (soma de cada linha deve dar 1)
        transicoes = transicoes / transicoes.sum(axis=1, keepdims=True)
        return transicoes

    def nextSate(self, estado_atual, transicoes):
        return estado_atual @ transicoes  # produto vetorial

    def stateTransition(self, controllGate, confidence, hour):
        transicoes_ajustadas = self.adjustTransitionsWithSensors(controllGate, confidence, hour)
        print(f"Estados Markov: {self.estado_atual.round(3)}")
        self.estado_atual = self.nextSate(self.estado_atual, transicoes_ajustadas)
