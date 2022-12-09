import engine
import turtle as t


class api():
    
    def __init__(self, xLength: int, yLength: int) -> None:

        self.render2d = engine.renderEngine(xLength, yLength)

    def add(self, x, y):
        self.render2d.addGotoToRenderQueue(x, y)

    def parseRenderQueue(self):
        print(self.render2d.renderQueue)

        for indexOfQueue in range(len(self.render2d.renderQueue)):

            currentInstruction = self.render2d.renderQueue[indexOfQueue]

            match currentInstruction.commandType:
                case "NonCommand":
                    print("no command")

                case "goto":
                    t.goto(currentInstruction.xPosition, currentInstruction.yPosition)
                    
            
            

app = api(500, 500)
app.add(100, 200)
app.add(100, 100)
app.add(0, 100)
app.add(0, 200)
app.add(100, 200)
app.parseRenderQueue()

    