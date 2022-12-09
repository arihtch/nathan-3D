import turtle
import renderPoint

class renderEngine():
    def __init__(self, xWindowLength: int, yWindowLength: int) -> None:
        turtle.tracer(True)
        self.renderQueue = {}
        self.renderQueueIndex = 0
        # setting up turtle

        self.xWindowLength = xWindowLength
        self.yWindowLength = yWindowLength


        self.topLeftScreenPoint = renderPoint.renderPoint(-xWindowLength/2, yWindowLength/2, "NonCommand")
        self.topRightScreenPoint = renderPoint.renderPoint(xWindowLength/2, yWindowLength/2, "NonCommand")
        self.bottomLeftScreenPoint = renderPoint.renderPoint(-xWindowLength/2, -yWindowLength/2, "NonCommand")
        self.bottomRightScreenPoint = renderPoint.renderPoint(xWindowLength/2, -yWindowLength/2, "NonCommand")
        # defining all screen points in order of 
        #  1 ->  2
        # /\     |
        # |     \/
        # 4 <-  3

        self.allScreenPoints = [self.topLeftScreenPoint,
                                self.topRightScreenPoint, 
                                self.bottomLeftScreenPoint, 
                                self.bottomRightScreenPoint]
        # adding all the points into a list in order of q (1, 2, 3, 4)
    
    def renderScreen(self):
        turtle.update()
    
    def addGotoToRenderQueue(self, xPosition: int, yPosition: int):
        if yPosition > self.yWindowLength/2:
            yPosition = int(self.yWindowLength/2)
            print("The yPosition is outside of the upward bounds")
        
        if yPosition < -self.yWindowLength/2:
            yPosition = int(-self.yWindowLength/2)
            print("The yPosition is outside of the downward bounds")
        
        if xPosition > self.xWindowLength/2:
            xPosition = int(self.xWindowLength/2)
            print("The xPosition is outside of the right-side bounds")
        
        if xPosition < -self.xWindowLength/2:
            xPosition = int(-self.xWindowLength/2)
            print("The xPosition is outside of the left-side bounds")
        

        self.renderQueue[self.renderQueueIndex] = renderPoint.renderPoint(xPosition, yPosition, "goto")
        self.renderQueueIndex += 1
    # adds goto command with bounds dectection
    # TODO:: add point to edge expansion
    
    def addPenupToRenderQueue(self):
        command = renderPoint.renderPoint(0, 0, "pen")
        command.penup = True
        self.renderQueue[self.renderQueueIndex] = command
        self.renderQueueIndex += 1
    
    def addPendownToRenderQueue(self):
        command = renderPoint.renderPoint(0, 0, "pen")
        command.pendown = True
        self.renderQueue[self.renderQueueIndex] = command
        self.renderQueueIndex += 1
        

    def addChangeFillColourToRenderQueue(self, hexcode: str):
        index = 0
        amountOfVaildDigets = 0
        
        if len(hexcode) == 7:
            # check if the hexcode is of vaild length
            
            if hexcode[0] == '#':
                amountOfVaildDigets += 1
                #check if the hexcode starts with a hash
                while index != 6:
                    index += 1
                    match hexcode[index]:
                        case '0':
                            amountOfVaildDigets += 1
                        case '1':
                            amountOfVaildDigets += 1
                        case '2':
                            amountOfVaildDigets += 1
                        case '3':
                            amountOfVaildDigets += 1
                        case '4':
                            amountOfVaildDigets += 1
                        case '5':
                            amountOfVaildDigets += 1
                        case '6':
                            amountOfVaildDigets += 1
                        case '7':
                            amountOfVaildDigets += 1
                        case '8':
                            amountOfVaildDigets += 1
                        case '9':
                            amountOfVaildDigets += 1
                        case 'a':
                            amountOfVaildDigets += 1
                        case 'b':
                            amountOfVaildDigets += 1
                        case 'c':
                            amountOfVaildDigets += 1
                        case 'd':
                            amountOfVaildDigets += 1
                        case 'e':
                            amountOfVaildDigets += 1
                        case 'f':
                            amountOfVaildDigets += 1

        if amountOfVaildDigets == 7:
            command = renderPoint.renderPoint(0, 0, "fillcolour")
            command.colour = hexcode
            self.renderQueue[self.renderQueueIndex] = command
            self.renderQueueIndex += 1 
        else:
            print("{} is not a vaild hex code".format(hexcode))
    # takes a hex code as input checks if vaild and then adds to renderQueue
        
        
    def addChangePenColourToRenderQueue(self, hexcode: str):
        index = 0
        amountOfVaildDigets = 0
        
        if len(hexcode) == 7:
            # check if the hexcode is of vaild length
            
            if hexcode[0] == '#':
                amountOfVaildDigets += 1
                #check if the hexcode starts with a hash
                while index != 6:
                    index += 1
                    match hexcode[index]:
                        case '0':
                            amountOfVaildDigets += 1
                        case '1':
                            amountOfVaildDigets += 1
                        case '2':
                            amountOfVaildDigets += 1
                        case '3':
                            amountOfVaildDigets += 1
                        case '4':
                            amountOfVaildDigets += 1
                        case '5':
                            amountOfVaildDigets += 1
                        case '6':
                            amountOfVaildDigets += 1
                        case '7':
                            amountOfVaildDigets += 1
                        case '8':
                            amountOfVaildDigets += 1
                        case '9':
                            amountOfVaildDigets += 1
                        case 'a':
                            amountOfVaildDigets += 1
                        case 'b':
                            amountOfVaildDigets += 1
                        case 'c':
                            amountOfVaildDigets += 1
                        case 'd':
                            amountOfVaildDigets += 1
                        case 'e':
                            amountOfVaildDigets += 1
                        case 'f':
                            amountOfVaildDigets += 1

        if amountOfVaildDigets == 7:
            command = renderPoint.renderPoint(0, 0, "pencolour")
            command.colour = hexcode
            self.renderQueue[self.renderQueueIndex] = command
            self.renderQueueIndex += 1 
        else:
            print("{} is not a vaild hex code".format(hexcode))
            
    def addStartFilltoRenderQueue(self):
        command = renderPoint.renderPoint(0, 0, "startFill")
        command.startfill = True
        self.renderQueue[self.renderQueueIndex] = command
        self.renderQueueIndex += 1
    
    def addEndFilltoRenderQueue(self):
        command = renderPoint.renderPoint(0, 0, "endFill")
        command.endfill = True
        self.renderQueue[self.renderQueueIndex] = command
        self.renderQueueIndex += 1
    
        