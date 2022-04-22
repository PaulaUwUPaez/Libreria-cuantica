import quantum as q
import LibNumerosComplejos.numeroscomplejos as lc
from math import sqrt
def main():
    #Ejercicio 4.4.1
    U1 = [[(0,0), (1,0)], [(1,0), (0,0)]]
    U2 = [[(sqrt(2)/2, 0), (sqrt(2)/2, 0)],[(sqrt(2)/2, 0), (-sqrt(2)/2, 0)]]
    print("U1 es "+lc.Unitaria(U1)+"\n"+"U2 es "+lc.Unitaria(U2))
    Product = lc.ProductMatrix(U1,U2)
    print("El producto de U1 y U2 es: "+ lc.Unitaria(Product))
    #Ejercicio 4.4.2
    map = [[(0, 0), (1/sqrt(2), 0), (1/(sqrt(2)), 0), (0, 0)], 
           [(0, 1/sqrt(2)), (0, 0), (0, 0), (1/sqrt(2), 0)],
           [(1/sqrt(2), 0), (0, 0), (0, 0), (0, 1/sqrt(2))],
           [(0, 0), (1/sqrt(2), 0), (-1/sqrt(2), 0), (0, 0)]]
    state = [[(1,0)],[(0,0)],[(0,0)],[(0,0)]]
    time = 3
    finalstate = q.Experiment_Marbles(map, state, time)
    print("estado final = "+str(finalstate))
    prob = q.ProbParticleInLine(3, finalstate)
    print("La probabilidad es de: "+str(prob))
main()
