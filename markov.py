import numpy as np
import pandas as pd

class Markov:
    def __init__(self):
        self.states = ['Normal', 'Suspeito', 'Invasao']


        self.mc = {'Normal': [0.8, 0.2, 0.0],
            'Suspeito': [0.1, 0.7, 0.2],
            'Invasao': [0.1, 0.0, 0.9]}

        self.mc = pd.DataFrame(data=self.mc, index=self.states)

        print("Matriz de transição:")
        print(self.mc)
        