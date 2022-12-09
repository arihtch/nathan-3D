class renderPoint:
    def __init__(self, xPosition: int, yPosition: int, command:str) -> None:
        self.commandType = command
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.colour = ""
        self.penup = False
        self.pendown = False
        self.startfill = False
        self.endfill = False
        