import kwant


class nanotube():

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.lattice = kwant.lattice.square(a = 1)
        self.tubeHoping = kwant.builder.HoppingKind((length-1, 0), self.lattice)
        self.hoppingElement = 1
        self.name = "length = " + str(self.length) + " and width = " + str(self.width)

        pass


    def __str__(self):
        return "length = " + str(self.length) + " and width = " + str(self.width)



    def __makeSystem(self):

        system = kwant.builder.Builder()
        system[(self.lattice(x, y) for x in range(self.length) for y in range(self.width))] = 4* self.hoppingElement
        system[(self.lattice.neighbors())] = -1 * self.hoppingElement
        system[self.tubeHoping] = -1 * self.hoppingElement

        return system

    def makeLead(self):

        lead = kwant.builder.Builder(kwant.lattice.TranslationalSymmetry((0, 1)))
        lead[(self.lattice(x, 0) for x in range(self.length))] = 4 * self.hoppingElement
        lead[(self.lattice.neighbors())] = -1 * self.hoppingElement
        lead[self.tubeHoping] = -1 * self.hoppingElement

        return lead


    def addLead(self):

        system = self.__makeSystem()
        lead = self.makeLead()

        system.attach_lead(lead)
        system.attach_lead(lead.reversed())

        return system


    def finalized(self):

        system = self.__makeSystem()
        lead = self.makeLead()

        system.attach_lead(lead)
        system.attach_lead(lead.reversed())

        system = system.finalized()
        return system
