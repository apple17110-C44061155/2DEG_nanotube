"""

This is a model of 2DEG nanotube

"""
import kwant

def makeSystem():

    # variables scope
    length = 100
    width =10
    hoppingElement = 1


    # model building scope

    system = kwant.builder.Builder()

    lattice = kwant.lattice.square(a = 1)



    # hopping elements setting scope
    system[(lattice(x, y) for x in range(length) for y in range(width))] = 4 * hoppingElement
    system[(lattice.neighbors())] = -1 * hoppingElement

    # nanotube modeling scope









    return system


if __name__ == "__main__":
    system = makeSystem()
    system.finalized()

    kwant.plot(system)
