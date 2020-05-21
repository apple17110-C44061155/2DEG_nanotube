import kwant


class nanotube:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.lattice = kwant.lattice.square(a = 1)
        self.tubeHoping = kwant.builder.HoppingKind((length-1, 0), self.lattice)
        self.hoppingElement = 1

        pass

    def __str__(self):
        return "length = " + str(self.length) + "and width = " + str(self.width)


    def makeSystem(self):

        system = kwant.builder.Builder()
        system[(self.lattice(x, y) for x in range(length) for y in range(width))] = 4* hoppingElement
        system[(self.lattice.neighbors())] = -1 * hoppingElement
        system[self.tubeHoping] = -1 * hoppingElement

        return system

    def plotSystem(self):

        kwant.plot(self.system)

def main():

    nanotube(5, 10).makeSystem.plotSystem()

main()
