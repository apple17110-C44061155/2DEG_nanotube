import kwant
import calculusMathod as cmath
import openpyxl

hoppingElementInOneDimension = 1
hoppingElementOfInterlayer = 0.9



def makeSystem(length, width, scrollNumber):

    system = kwant.builder.Builder()
    global lattice
    lattice =kwant.lattice.square(a = 1)

    system[(lattice(x, y) for x in range(length) for y in range(width))] = 4 * hoppingElementInOneDimension
    system[(lattice.neighbors())] = -1 * hoppingElementInOneDimension

    global interlayerCoupling
    interlayerCoupling = kwant.builder.HoppingKind((length - scrollNumber, 0), lattice)
    system[interlayerCoupling] = -1*hoppingElementOfInterlayer

    return system


def makeLeed(length, width, scrollNumber):

    lead = kwant.builder.Builder(kwant.lattice.TranslationalSymmetry((0, 1)))
    lead[(lattice(x, 0) for x in range(length))] = 4 * hoppingElementInOneDimension
    lead[(lattice.neighbors())] = -1 * hoppingElementInOneDimension
    lead[interlayerCoupling] = -1 * hoppingElementOfInterlayer

    return lead


def main(length, width, scrollNumber):
    system = makeSystem(length, width, scrollNumber)
    lead = makeLeed(length, width, scrollNumber)

    system.attach_lead(lead)
    system.attach_lead(lead.reversed())

    system = system.finalized()

    cmath.plotWavefunction(system, 1)

    lead = lead.finalized()
    momentum = 6.28
    momenta = [-momentum + 0.02 * i for i in range(int(momentum*100) + 1)]
    cmath.plotBandstructure(lead, momenta, energyMaxmum = 10)




if __name__ == '__main__':
    main(10, 10, 1)
