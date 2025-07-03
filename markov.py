import numpy as np
import random

class Markov:
    def __init__(self):
        self.estados = ["Chance baixa", "Chance média", "Chance alta"]

        self.transicoes_base = np.array([
            [0.7, 0.2, 0.1],
            [0.3, 0.4, 0.3],
            [0.2, 0.3, 0.5]
        ])

        self.estado_atual = np.array([0.8, 0.1, 0.1])
        self.atual = "Chance baixa"

    def adjustTransitionsWithSensors(self, controllGate, confidence, hour):
        transicoes = self.transicoes_base.copy()

        if controllGate == False and confidence > 0.70 and hour == "Critical":
            if self.atual == "Chance baixa":
                transicoes[:,1] += 0.8
            else:
                transicoes[:,2] += 0.8
        elif controllGate == False and confidence < 0.70 and confidence > 0.55 and hour == "Critical":
            if self.atual == "Chance baixa":
                transicoes[:,1] += 0.4
            else:
                transicoes[:,2] += 0.4
        elif controllGate == False and confidence > 0.70 and hour == "Medium":
            if self.atual == "Chance baixa":
                transicoes[:,1] += 0.12
            else:
                transicoes[:,2] += 0.12
        else:
            if self.atual == "Chance alta":
                transicoes[:,1] += 0.8
            else:
                transicoes[:,0] += 0.8

        # Normaliza as linhas (soma de cada linha deve dar 1)
        transicoes = transicoes / transicoes.sum(axis=1, keepdims=True)
        return transicoes

    def nextSate(self, estado_atual, transicoes):
        if self.atual == "Chance baixa":
            prob = random.randrange(0, int(self.estado_atual[0]*100) + int(self.estado_atual[1]*100))
            if prob <= self.estado_atual[0]*100 - self.estado_atual[1]*100:
                pass
            else:
                self.atual = "Chance média"
        elif self.atual == "Chance média":
            prob = random.randrange(0, int(self.estado_atual[0]*100) + int(self.estado_atual[1]*100) + int(self.estado_atual[2]*100))
            if prob <= self.estado_atual[0]*100:
                self.atual = "Chance baixa"
            elif prob > self.estado_atual[0]*100 and prob <= (self.estado_atual[0]*100 + self.estado_atual[1]*100) :
                self.atual = "Chance média"
            else:
                self.atual = "Chance alta"
        else:
            prob = random.randrange(0, int(self.estado_atual[1]*100) + int(self.estado_atual[2]*100))
            if prob <= self.estado_atual[1]*100 - self.estado_atual[2]*100:
                self.atual = "Chance média"

        return estado_atual @ transicoes  # produto vetorial

    def stateTransition(self, controllGate, confidence, hour):
        transicoes_ajustadas = self.adjustTransitionsWithSensors(controllGate, confidence, hour)
        print(f"Estados Markov: {self.estado_atual.round(3)}")
        print(f"Chace em Markov: {self.atual}")
        self.estado_atual = self.nextSate(self.estado_atual, transicoes_ajustadas)
