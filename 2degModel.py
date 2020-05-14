"""

This is a model of 2DEG nanotube

"""
import kwant
import calculusMathod as cM
import openpyxl

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


def main(length = 15, width = 2, energyMaxmum = 20):

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
    energies, data = cM.plotConductance(system, energyMaxmum)

    cM.plotWavefunction(system, 1)

    cM.computeEigenvalues(system)

    momentum = 6.28
    momenta = [-momentum + 0.002 * i for i in range(int(momentum*1000) + 1)]
    lead = lead.finalized()

    cM.plotBandstructure(lead, momenta, energyMaxmum)


    bandenergy = cM.BandEnergy(lead, 6.28, length)


    Workbook = openpyxl.Workbook()
    worksheet = Workbook.create_sheet("length = 15")
    worksheet.append(energies)
    worksheet.append(data)
    for i in range(length):
        worksheet.append(bandenergy[i])


    Workbook.save("Band.xlsx")



if __name__ == "__main__":
    main()
