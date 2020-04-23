"""

This is a model of 2DEG nanotube

"""
import kwant
import calculusMathod as cM

hoppingElement = 1


def makeSystem(length = 50, width = 100):

    # variables scope

    # model building scope
    global lattice
    system = kwant.builder.Builder()
    lattice = kwant.lattice.square(a = 1)


    # hopping elements setting scope
    system[(lattice(x, y) for x in range(length) for y in range(width))] = 4 * hoppingElement
    system[(lattice.neighbors())] = -1 * hoppingElement


    # nanotube modeling scope
    global tubeHoping
    tubeHoping = kwant.builder.HoppingKind((length-1 , 0), lattice)
    system[tubeHoping] = -1 * hoppingElement


    return system


def makeLead(length = 50, width = 100):

    #Lead building scope
    lead = kwant.builder.Builder(kwant.lattice.TranslationalSymmetry((0, 1)))
    lead[(lattice(x, 0) for x in range(length))] = 4 * hoppingElement
    lead[(lattice.neighbors())] = -1 * hoppingElement
    lead[tubeHoping] = -1 * hoppingElement


    return lead


def main(length = 50, width = 25, energyMaxmum = 4):

    system = makeSystem(length, width)
    lead = makeLead(length, width)

    system.attach_lead(lead)
    system.attach_lead(lead.reversed())

    system = system.finalized()
    kwant.plot(system)

    systemToDOS = makeSystem(length, width)
    systemToDOS = systemToDOS.finalized()

    cM.plotDOS(systemToDOS, energyMaxmum)

    energies = [-2 * 0.1 + 0.1 * (4 / 100) * i for i in range(100)]
    cM.plotConductance(system, energyMaxmum)

    cM.plotWavefunction(system, 1)

    cM.computeEigenvalues(system)

    momenta = [-2 + 0.02 * i for i in range(201)]
    lead = lead.finalized()
    cM.plotBandstructure(lead, momenta, energyMaxmum)



if __name__ == "__main__":
    main()
