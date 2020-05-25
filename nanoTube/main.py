import kwant
import calculusMathod
from  nanoTube import nanotube
import openpyxl

def momenta(momentum = 3.14):

    momenta = [-momentum + 0.02 * i for i in range(int(momentum*100) + 1)]
    return momenta


def main(length, width):

    workbook = openpyxl.Workbook()

    system = nanotube(length, width)
    name = system.name + ".xlsx"

    lead = system.makeLead()
    lead = lead.finalized()

    system = system.addLead()
    system = system.finalized()

    kwant.plot(system)

    calculusMathod.getDOS(system, workbook)
    calculusMathod.getBandStructure(lead, momenta(3.14), length, workbook)
    calculusMathod.getConductance(system, 10, workbook)




    workbook.save(name)


main(2, 5)
