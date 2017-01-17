
from Data.DrugInteraction import DI
from Algorithm.CreateDoseCurve import CDC
from Algorithm.Graph import Graph


class SampleMain:

    def __Init__(self):
        sampleDi = DI(0,"kim","f","d",37,4,14,93,0.2,0.9,1,"sample")

    def run(self):
        sampleDi = DI(0,"kim","f","d",37,4,14,93,0.2,0.9,1,"sample")

        gr = Graph()
        gr.graph_main(sampleDi, 78, 5, 2)


if __name__ == "__main__":
    main = SampleMain()
    main.run()