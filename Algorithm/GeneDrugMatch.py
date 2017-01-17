
from Data.DrugInteraction import DI
from Data.DrugEnzyme import DETable
from Data.DrugMultiplier import DM
from Data.Allele import Allele

from Algorithm.Graph import Graph



class gdm:

    def gdm_main(self, pr, dr):
        di = DI()
        gr = Graph()

        mult = 0
        dec = 0
        inc = 0

        flag = 0
        for row in (0,DETable.drug.__sizeof__()):
            for drt in (0, dr.drug.__sizeof__()):
                if(DETable.drug[row] == dr.drug[drt]):
                    if(DETable.enzyme[row] == dr.enzyme[drt]):
                        flag+=1

        if (flag==0):
            print("No Interaction Detected")

        else:
            print("Interaction Detected")



            if (mult != 0):
                gr.graph_main(di, pr.weight, dr.dose, mult)

            elif (di.pmm != 0):
                mult = di.pmm
                gr.graph_main(di, pr.weight, dr.dose, mult)

            else:
                for ind in Allele.__sizeof__():
                    if ( pr.allele1 == Allele.allele[ind] or pr.allele2 == Allele.allele[ind]):
                        if (Allele.aei[ind] ==1 ):
                            inc += 1
                        elif (Allele.aei[ind] == 0):
                            dec += 1

                if (inc > 0 or dec > 0):
                    mult = 1 + (inc * 0.33) - (dec * 0.33)
                    gr.graph_main(di, pr.weight, dr.drug, mult)
                else:
                    print("Not Enough Information to Graph")








