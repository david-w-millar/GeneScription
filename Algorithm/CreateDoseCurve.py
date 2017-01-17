
from matplotlib import pyplot as mplp

from Data.DrugInteraction import DI
from Data.SequenceTable import SequenceTable
from Calculation.CalPPC import CDPC


def draw_graph(x,y):
    mplp.plot(x,y)
    mplp.xlabel('x-coordinate')
    mplp.ylabel('y-coordinate')
    mplp.title('sample')
    mplp.show()

class CDC:
    """
    input :
        DI
        patient weight
        drug dose
        mult
    """



    def cdc_main(self, di, weight, dose, mul):
        self.x=[]
        self.y=[]
        self.curve = (self.x,self.y)

        k = 0.693 / di.hl
        cdpc_temp = CDPC()
        ppc = cdpc_temp.cal_ppc(dose, di.ba, di.vd, weight, k);

        if (mul!=1):
            ppc *= mul
            di.hl *= mul

        # plot 1st part of curve using di.pt, ppc : Q2
        for i in range(1, 22):
            st = SequenceTable()
            x_tmp = st.getmultx(i) *  di.pt
            y_tmp = st.getmulty(i) * ppc

            self.x.append(x_tmp)
            self.y.append(y_tmp)


        if (mul>1):
            hl5x = di.hl * 10 + x_tmp
        else:
            hl5x = di.hl * 10 / mul + x_tmp

        #Q1
        while ( x_tmp + (di.hl/5) < hl5x ):
            x_tmp = x_tmp + (di.hl/5)
            y_tmp = y_tmp * 0.9

            self.x.append(x_tmp)
            self.y.append(y_tmp)
            #plot (x,y) to curve

        return self.curve

    def draw(self):
        draw_graph(self.x,self.y)




