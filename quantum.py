from math import sqrt
from matplotlib import pyplot
import numpy as np
from numpy.linalg import eig
import LibNumerosComplejos.numeroscomplejos as lc
import random
def Experiment_Marbles(A, V, t):
    """Función que simula los clicks para el experimento 
    de la canicas con coeficientes booleanos.
    (list),(list),(int) → (list)"""
    vector = V
    index = 0
    while index < t:
        vector_click = lc.AccionMatVec(A, vector)
        vector = vector_click
        index += 1
    return vector
def ExperimentSlitsMatriz(matriz_adyacencia):
    """Función que simula el experimento de las múltiples 
    rendijas clásico probabilístico, con más de dos rendijas.
    Generador de la matriz resultante
    (list) → (list)"""
    b2 = lc.ProductMatrix(matriz_adyacencia, matriz_adyacencia)
    return b2
def ExperimentSlitsVector(b2, state):
    """Función que simula el experimento de las múltiples 
    rendijas clásico probabilístico, con más de dos rendijas.
    Generador del vector
    (list),(list) → (list)"""
    vector_click = lc.AccionMatVec(b2, state)
    return vector_click
def random_color():
    """Función que genera colores al azar → implementación para el graficador"""
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    return color
def graficador(vector_estados):
    """Función que grafica con un diagrama de barras las probabilidades de un vector de estados.
     Guardar el gráfico en el computador con un formato png"""
    vertices = []
    colores = []
    for i in range(1, len(vector_estados) + 1):
        vertices += [i]
        colores += [random_color()]
    pyplot.title("probabilidades de un vector de estados")
    pyplot.bar(vertices, height = vector_estados, color = colores, width = 0.5)
    pyplot.ylabel("probabilidad")
    pyplot.savefig("probabilidades.png")
    pyplot.show()
"""================================Sección 4.1======================================"""
def ProbParticleInLine(p, ket):
    """Función que calcula la probabilidad de encontrar la partícula en una posición determinada.
    (int),(list) → (float)"""
    denominador = lc.SquareModuleVec(ket)
    numerador = lc.squaremodule(ket[p][0])
    prob = numerador/denominador
    return prob

def AmpliTransition(ket1, ket2):
    transition = lc.ProductoInterno(lc.normalizar(ket2),lc.normalizar(ket1))
    return transition

def ProbSpinUp(ket):
    return ProbParticleInLine(0, ket)

def ProbSpinDown(ket):
    return ProbParticleInLine(1, ket)

def probabilidadTransitar(bi, ket):
    return lc.squaremodule(AmpliTransition(bi, ket))


"""================================Sección 4.2======================================"""

def conmutador(sigma1, sigma2):
    return lc.SustracMatriz(lc.ProductMatrix(sigma1, sigma2), lc.ProductMatrix(sigma2, sigma1))

def ExpectedValue(psi, sigma):
    sigmapsi = lc.ProductMatrix(sigma, psi) 
    return lc.ProductoInterno(sigmapsi, psi)

def delta(sigma, psi):
    return lc.SustracMatriz(sigma, lc.MultEscalarMatriz(ExpectedValue(psi, sigma),lc.identidad(sigma)))

def variance(sigma, psi):
    return ExpectedValue(psi, lc.ProductMatrix(delta(sigma, psi), delta(sigma, psi)))


"""================================Sección 4.3======================================"""

def ChageNotation(A):
    """Función que aplica notación de números complejos para librería Numpy"""
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = complex(A[i][j][0], A[i][j][1])
    return A

def UseNotationValue(A):
    """Función que aplica notación de números complejos para librería la librería implementada"""
    real, imaginario, result = "", "", []
    for i in range(len(A)):
        pos = str(A[i]).find("+")
        if pos == -1:
            pos = str(A[i]).find("-")
            #if pos == 0:
                #pos = str(A[i])[1:].find("-")
                #new_pos = str(A[i])[pos + 1:].find("-")
                #if new_pos != -1:
                #else:
            #else:
                #real = str(A[i])[:pos]
                #imaginario = str(A[i])[pos+1:len(A[i]) - 2]

        else:
            real = str(A[i])[:pos]
            imaginario = str(A[i])[pos+1:len(A[i]) - 2]
        
        result += [(float(real), float(imaginario))]
        real, imaginario = "", ""

        
        
    return result


def EigenValues(sigma):
    """Genera todas las medidas que podría llegar a registrar respecto al observable (valores propios)"""
    mat = np.array(ChageNotation(sigma))
    eigenvalue, featurevector = np.linalg.eig(mat)
    eigenvalue = str(eigenvalue).replace("[", "").replace("]", "").split()
    eigenvalue = UseNotationValue(eigenvalue)
    return eigenvalue


def EigenVectors(sigma):
    """Genera todas las medidas que podría llegar a registrar respecto al observable (valores propios)"""
    mat = np.array(ChageNotation(sigma))
    eigenvalue, featurevector = np.linalg.eig(mat)
    #print(featurevector)
    #featurevector = str(featurevector).replace("[", "").replace("]", "").split()
    #eigenvalue = UseNotationValue(eigenvalue)
    return featurevector
def ProbTransition(psi, e):
    #e = EigenVectors(sigma)
    return lc.squaremodule(AmpliTransition(e, psi))

def FinalState(U, psi, t):
    vector = psi
    index = 1
    finaldin = U
    while index < t:
        din = lc.ProductMatrix(U,U)
        finaldin = din
        index += 1
    return lc.AccionMatVec(finaldin, psi)
