"""

There are many functions in this module.

"""
from matplotlib import pyplot
import scipy.sparse.linalg as sla
import kwant
import numpy as np


def computeEigenvalues(system):
    sparseMatrix = system.hamiltonian_submatrix(sparse = True)
    eigenvalues = sla.eigs(sparseMatrix, 5)[0]
    print(eigenvalues.real)


def plotConductance(system, energies):

    data = []

    for energy in energies:
        smatrix = kwant.solvers.default.smatrix(system, energy)
        data.append(smatrix.transmission(0, 1))

    pyplot.figure()
    pyplot.plot(energies, data)
    pyplot.title("Quantum Conductance")
    pyplot.xlabel("energy [t]")
    pyplot.ylabel("conductance [e^2/h]")
    pyplot.show()


def sortedEigens(ev):
    eigenvalues, eigenvectors = ev
    eigenvalues, eigenvectors = map(np.array, zip(*sorted(zip(eigenvalues, eigenvectors.transpose()))))
    return eigenvalues, eigenvectors.transpose()


def plotWavefunction(system):

    hamiltonian_matrix = system.hamiltonian_submatrix(sparse = True)
    eigenvalues, eigenvectors = sortedEigens(sla.eigsh(hamiltonian_matrix.tocsc(), k = 20, sigma = 0))
    a = 0
    for k in range(20):
        a = a + np.abs(eigenvectors[:,k])**2

    kwant.plotter.map(system, a ,colorbar = False, oversampling = 3)
