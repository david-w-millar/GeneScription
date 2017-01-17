from Algorithm.CreateDoseCurve import CDC
from Algorithm.CreateLine import Line

from matplotlib import pyplot as mplp



def draw_graph(x,y,cr):
    line = mplp.plot(x,y)
    mplp.setp(line, color=cr)
    mplp.xlabel('x-coordinate')
    mplp.ylabel('y-coordinate')
    mplp.title('sample')


class Graph:
    """®
    input:
    DI
    weight
    dose
    mul
    """

    def graph_main(self, di, weight, dose, mul):
        cdc1 = CDC()
        cdc2 = CDC()
        line = Line()
        curve_1 = cdc1.cdc_main(di,weight,dose,mul)
        curve_2 = cdc2.cdc_main(di,weight,dose,1)
        line_1 = line.getline(curve_1[0],di.ec)
        line_2 = line.getline(curve_2[0],di.tc)


        sample_x=[]
        sample_y=[]
        for i in(0,10):
            sample_x.append(i*10)
            sample_y.append(i*2)

        #mpl.plot(sample_x, sample_y)


        draw_graph(curve_1[0], curve_1[1], "b")
        draw_graph(curve_2[0], curve_2[1], "y")
        draw_graph(line_1[0], line_1[1], "g")
        draw_graph(line_2[0], line_2[1], "r")

        mplp.show()
