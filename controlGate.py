class controlGate:
    def __init__(self):
        self.controlActived = False
    
    def activeControl(self):
        self.controlActived = True
    
    def returnStateControl(self):
        return self.controlActived
