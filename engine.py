import turtle
import renderPoint

class renderEngine():
    def __init__(self, xWindowLength: int, yWindowLength: int) -> None:
        turtle.tracer(False)
        self.renderQueue = {}
        self.renderQueueIndex = 0
        # setting up turtle

        self.xWindowLength = xWindowLength
        self.yWindowLength = yWindowLength


        self.topLeftScreenPoint = renderPoint.renderPoint(-xWindowLength/2, yWindowLength/2, None)
        self.topRightScreenPoint = renderPoint.renderPoint(xWindowLength/2, yWindowLength/2, None)
        self.bottomLeftScreenPoint = renderPoint.renderPoint(-xWindowLength/2, -yWindowLength/2, None)
        self.bottomRightScreenPoint = renderPoint.renderPoint(xWindowLength/2, -yWindowLength/2, None)
        # defining all screen points in order of 
        #  1 ->  2
        # /\     |
        # |     \/
        # 4 <-  3

        self.topLeftScreenPoint.setConnectingPoint(self.topRightScreenPoint)
        self.topRightScreenPoint.setConnectingPoint(self.bottomLeftScreenPoint)
        self.bottomLeftScreenPoint.setConnectingPoint(self.bottomRightScreenPoint)
        self.bottomRightScreenPoint.setConnectingPoint(self.topLeftScreenPoint)
        # defining the connections between all the points

        self.allScreenPoints = [self.topLeftScreenPoint,
                                self.topRightScreenPoint, 
                                self.bottomLeftScreenPoint, 
                                self.bottomRightScreenPoint]
        # adding all the points into a list in order of q (1, 2, 3, 4)
    
    def renderScreen(self):
        turtle.update()


while True:
    turtle.fd(1)
    turtle.update()