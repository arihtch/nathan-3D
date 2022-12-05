class renderPoint:
    def __init__(self, xPosition: int, yPosition: int,  connectingPoint) -> None:
        self.xPosition = xPosition
        self.yPosition = yPosition

        
        self.connectingPoint = None

        if connectingPoint != None:
            self.connectingPoint = connectingPoint

    def setConnectingPoint(self, connectingPoint) -> None:
        if connectingPoint == renderPoint:
            self.connectingPoint = connectingPoint
        else:
            self.connectingPoint = None