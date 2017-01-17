
from matplotlib import pyplot as mplp

def draw_graph(x,y):
    mplp.plot(x,y)
    mplp.xlabel('x-coordinate')
    mplp.ylabel('y-coordinate')
    mplp.title('sample')

class Line:


    def getline(self,xt,yval):

        self.x = []
        self.y = []
        self.line = (self.x, self.y)
        for i in xt:
            self.x.append(i)
            self.y.append(yval)

        return self.line


