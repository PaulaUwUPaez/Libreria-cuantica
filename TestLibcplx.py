import numeroscomplejos as lc
import unittest
class TestCplxOperations(unittest.TestCase):
    def test_suma_complejos(self):
        suma = lc.suma_complejos((3,5),(-2.6,6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)
        suma2 = lc.suma_complejos((2,5),(3,8))
        self.assertAlmostEqual(suma2[0], 5)
        self.assertAlmostEqual(suma2[1], 13)
    def test_producto_complejos(self):
        producto = lc.producto_complejos((2,5),(6,7))
        self.assertAlmostEqual(producto[0], -23)
        self.assertAlmostEqual(producto[1], 44)
        producto2 = lc.producto_complejos((-3,-1),(1,-2))
        self.assertAlmostEqual(producto2[0], -5)
        self.assertAlmostEqual(producto2[1], 5)
    def test_resta_complejos(self):
        resta = lc.resta_complejos((5,4),(3,2))
        self.assertAlmostEqual(resta[0], 2)
        self.assertAlmostEqual(resta[1], 2)
        resta2 = lc.resta_complejos((7,8),(3,5))
        self.assertAlmostEqual(resta2[0], 4)
        self.assertAlmostEqual(resta2[1], 3)
    def test_division_complejos(self):
        division = lc.division_complejos((-2,1),(1,2))
        self.assertAlmostEqual(division[0], 0)
        self.assertAlmostEqual(division[1], 1)
        division2 = lc.division_complejos((0,3),(-1,-1))
        self.assertAlmostEqual(division2[0], -1.5)
        self.assertAlmostEqual(division2[1], -1.5)
    def test_modulo_complejos(self):
        modulo = lc.modulo_complejo((1,-1))
        self.assertAlmostEqual(modulo, 1.4142135623730951)
        modulo2 = lc.modulo_complejo((4,-3))
        self.assertAlmostEqual(modulo2, 5)
    def test_conjugado_complejos(self):
        conjugado = lc.conjugado_complejo((3,4))
        self.assertAlmostEqual(conjugado[0], 3)
        self.assertAlmostEqual(conjugado[1], -4)
        conjugado2 = lc.conjugado_complejo((5, 0))
        self.assertAlmostEqual(conjugado2[0], 5)
        self.assertAlmostEqual(conjugado2[1], 0)
    def test_polartocartesian(self):
        cartesian = lc.polartocartesian((5, 60))
        self.assertAlmostEqual(cartesian[0], 2.5)
        self.assertAlmostEqual(cartesian[1], 4.330127018922193)
        cartesian2 = lc.polartocartesian((25, 45))
        self.assertAlmostEqual(cartesian2[0], 17.67766952966369)
        self.assertAlmostEqual(cartesian2[1], 17.67766952966369)
    def test_fase_complejos(self):
        fase = lc.fase_complejos((2,2))
        self.assertAlmostEqual(fase, 0.7853981633974483)
        fase2 = lc.fase_complejos((1,-1))
        self.assertAlmostEqual(fase2, -0.7853981633974483)
    def test_AdicionVectores(self):
        adicion = lc.AdicionVectoresComplejos([(6,-4),(7,3),(4.2,-8.1),(0,-3)], [(16,2.3),(0,-7),(6,0),(0,-4)])
        self.assertAlmostEqual(adicion, [(22, -1.7000000000000002), (7, -4), (10.2, -8.1), (0, -7)])
        adicion2 = lc.AdicionVectoresComplejos([(5,-3),(8,9),(4,-8),(0,-3)], [(20,2),(0,7),(6,0),(0,0)])
        self.assertAlmostEqual(adicion2, [(25, -1), (8, 16), (10, -8), (0, -3)])
    def test_invvector(self):
        inverso_aditivo = lc.invvector([(5, -3), (8, 9), (4, -8), (0, -3)])
        self.assertAlmostEqual(inverso_aditivo, [(-5, 3), (-8, -9), (-4, 8), (0, 3)])
        inverso_aditivo2 = lc.invvector([(7, 8), (4, 6), (0, 0), (1, 7)])
        self.assertAlmostEqual(inverso_aditivo2, [(-7, -8), (-4, -6), (0, 0), (-1, -7)])
    def test_MultEscalarVector(self):
        multesc = lc.MultEscalarVector((3,2),[(6,3),(0,0),(5,1),(4,0)])
        self.assertAlmostEqual(multesc,[(12,21),(0,0),(13,13),(12,8)])
        multesc2 = lc.MultEscalarVector((2, 0), [(8, 6),(2, 0),(4, 5),(8, 3)])
        self.assertAlmostEqual(multesc2, [(16, 12), (4, 0), (8, 10), (16, 6)])
    def test_AdicionMatriz(self):
        a = [[(-5,0),(10,0),(0,0)],[(2,0),(-14,0),(9,0)],[(-6,0),(3,0),(8,0)]]
        b = [[(-8,0),(3,0),(4,0)],[(-9,0),(7,0),(-5,0)],[(15,0),(-3,0),(0,0)]]
        adicionmatriz = lc.AdicionMatriz(a,b)
        self.assertAlmostEqual(adicionmatriz, [[(-13, 0), (13, 0), (4, 0)], [(-7, 0), (-7, 0), (4, 0)], [(9, 0), (0, 0), (8, 0)]])
        a2 = [[(-5,8),(10,9),(0,0)],[(2,7),(-14,8),(9,6)],[(-6,0),(3,6),(8,9)]]
        b2 = [[(-8,4),(3,7),(4,9)],[(-9,1),(7,2),(-5,3)],[(15,0),(-3,5),(0,7)]]
        adicionmatriz2 = lc.AdicionMatriz(a2, b2)
        self.assertAlmostEqual(adicionmatriz2, [
                               [(-13, 12), (13, 16), (4, 9)], [(-7, 8), (-7, 10), (4, 9)], [(9, 0), (0, 11), (8, 16)]])
    def test_InversaAditivaMatriz(self):
       a = [[(-5,0),(10,0),(0,0)],[(2,0),(-14,0),(9,0)],[(-6,0),(3,0),(8,0)]]
       a2 = [[(-5, 8), (10, 9), (0, 0)], [(2, 7), (-14, 8), (9, 6)],
             [(-6, 0), (3, 6), (8, 9)]]
       invadma2 = lc.InversaAditivaMatriz(a2)  
       invadma = lc.InversaAditivaMatriz(a)
       self.assertAlmostEqual(invadma, [[(5, 0), (-10, 0), (0, 0)], [(-2, 0), (14, 0), (-9, 0)], [(6, 0), (-3, 0), (-8, 0)]])
       self.assertAlmostEqual(invadma2, [
                              [(5, -8), (-10, -9), (0, 0)], [(-2, -7), (14, -8), (-9, -6)], [(6, 0), (-3, -6), (-8, -9)]])
    def test_MultEscalarMatriz(self):
        multescalarmatriz = lc.MultEscalarMatriz((3, 0), [[(-5, 8), (10, 9), (0, 0)], [(2, 7), (-14, 8), (9, 6)],[(-6, 0), (3, 6), (8, 9)]])
        self.assertAlmostEqual(multescalarmatriz, [[(-15, 24), (30, 27), (0, 0)], [(6, 21), (-42, 24), (27, 18)], [(-18, 0), (9, 18), (24, 27)]])
        multescalarmatriz2 = lc.MultEscalarMatriz((3, 2), [[(-13, 12), (13, 16), (4, 9)], [(-7, 8), (-7, 10), (4, 9)], [(9, 0), (0, 11), (8, 16)]])
        self.assertAlmostEqual(multescalarmatriz2, [[(-63, 10), (7, 74), (-6, 35)], [(-37, 10), (-41, 16), (-6, 35)], [(27, 18), (-22, 33), (-8, 64)]])
    def test_transpuesta(self):
        matriz = [[(1,0),(2,0),(3,0)],[(4,0),(5,0),(6,0)]]
        vector = [[(1,0)],[(2,0)],[(3,0)]]
        transpuesta = lc.Transpuesta(matriz)
        self.assertAlmostEqual(transpuesta, [[(1,0),(4,0)],[(2,0),(5,0)],[(3,0),(6,0)]])
        transpuesta2 = lc.Transpuesta(vector)
        self.assertAlmostEqual(transpuesta2, [[(1,0),(2,0),(3,0)]])
    def test_conjugada(self):
        matriz = [[(1,-1),(2,1),(3,2)],[(4,5),(5,-6),(6,0)]]
        vector = [[(1, -1)], [(2, 1)], [(3, -7)]]
        conjugada = lc.ConjugadaMatVec(matriz)
        conjugada2 =lc.ConjugadaMatVec(vector)
        self.assertAlmostEqual(conjugada, [[(1, 1), (2, -1), (3, -2)], [(4, -5), (5, 6), (6, 0)]])
        self.assertAlmostEqual(conjugada2, [[(1, 1)], [(2, -1)], [(3, 7)]])
    def test_adjunta(self):
        matriz = [[(1, -1), (2, 1), (3, 2)], [(4, 5), (5, -6), (6, 0)]]
        vector = [[(1, -1)], [(2, 1)], [(3, -7)]]
        daga1 = lc.AdjuntaMatVec(matriz)
        daga2 = lc.AdjuntaMatVec(vector)
        self.assertAlmostEqual(daga1, [[(1, 1), (4, -5)], [(2, -1), (5, 6)], [(3, -2), (6, 0)]])
        self.assertAlmostEqual(daga2, [[(1, 1), (2, -1), (3, 7)]])

    def test_ProductMatrix(self):
        a = [[(1,0),(2,0),(3,0)],[(4,0),(5,0),(6,0)]]
        b = [[(1,0),(2,0)],[(3,0),(4,0)],[(5,0),(6,0)]]
        a2 = [[(1,-3),(2,2),(3,5)],[(4,-7),(5,-9),(6,5)]]
        b2 = [[(1,6),(2,7)],[(3,8),(4,-2)],[(5,0),(6,3)]]
        producto = lc.ProductMatrix(a, b)
        producto2 = lc.ProductMatrix(a2, b2)
        self.assertAlmostEqual(producto,[[(22, 0), (28, 0)], [(49, 0), (64, 0)]])
        self.assertAlmostEqual(producto2, [[(24, 50), (38, 44)], [(163, 55), (80, 16)]])
    def test_AccionMatVec(self):
        matriz = [[(-1, 0), (1, 1), (0, 0)], [(2, -1), (0, 0), (1, 0)],[(0,0),(1,-1),(0,1)]]
        vector = [[(1, 0)], [(1, 1)],[(0,1)]]
        matriz2 = [[(-1,0),(1,1),(0,0)],[(2,-1),(0,0),(1,0)],[(0,0),(1,-1),(0,1)]]
        vector2 = [[(1,0)],[(1,1)],[(0,1)]]
        accion = lc.AccionMatVec(matriz,vector)
        accion2 = lc.AccionMatVec(matriz2, vector2)
        self.assertAlmostEqual(accion, [[(-1, 2)], [(2, 0)],[(1,0)]])
        self.assertAlmostEqual(accion2,[[(-1, 2)], [(2, 0)], [(1, 0)]])
    def test_ProductoInterno(self):
        v1 = [[(1,0)],[(0,1)],[(1,-3)]]
        v2 = [[(2,1)],[(0,1)],[(2,0)]]
        v3 = [[(2,0)],[(1,0)],[(3,0)]]
        v4 = [[(0,0)],[(-1,0)],[(2,0)]]
        productointerno = lc.ProductoInterno(v1,v2)
        productointerno2 = lc.ProductoInterno(v3, v4)
        self.assertAlmostEqual(productointerno, (5, 7))
        self.assertAlmostEqual(productointerno2, (5, 0))
    def test_Norma(self):
        v = [[(7.8,2.6)],[(5.2,-8.5)]]
        norma= lc.Norma(v)
        self.assertAlmostEqual(norma,12.918591254467337)
        v2 = [[(4,3)],[(6,-4)],[(12,-7)],[(0,13)]]
        norma2 = lc.Norma(v2)
        self.assertAlmostEqual(norma2, 20.952326839756964)
    def test_DistanciaVec(self):
        v1 = [[(3,0)],[(1,0)],[(2,0)]]
        v2 = [[(2,0)],[(2,0)],[(-1,0)]]
        v3 = [[(3,-5)],[(1,3)],[(2,4)]]
        v4 = [[(2,-6)],[(2,2)],[(-1,1)]]
        distancia = lc.DistanciaVec(v1,v2)
        distancia2 = lc.DistanciaVec(v3,v4)
        self.assertAlmostEqual(distancia,3.3166247903554)
        self.assertAlmostEqual(distancia2, 4.69041575982343)
    def test_unitaria(self):
        matriz = [[(0,2),(0,0)],[(0,0),(0,-2)]]
        unitaria = lc.Unitaria(matriz)
        self.assertAlmostEqual(unitaria, "No unitaria")
        matriz2 = [[(0, 1), (0, 0)],
                   [(0, 0), (1, 0)]]
        unitaria2 = lc.Unitaria(matriz2)
        self.assertAlmostEqual(unitaria2, "Unitaria")
    def test_hermitiana(self):
        matriz = [[(-1,0),(0,-1)],[(0,1),(1,0)]]
        hermitiana = lc.Hermitiana(matriz)
        self.assertAlmostEqual(hermitiana, "Hermitiana")
        matriz2 = [[(-1,0),(1,-1)],[(0,1),(1,0)]]
        hermitiana2 = lc.Hermitiana(matriz2)
        self.assertAlmostEqual(hermitiana2, "No es hermitiana")
    def test_ProductTensor(self):
        v1 = [(3, 0), (1, 0)]
        v2 = [(2,1),(0,1),(2,0)]
        v3 = [(2,0),(1,0),(3,0)]
        v4 = [(2,-6),(2,2),(-1,1)]
        tensor1 = lc.ProductTensor(v1,v2)
        tensor2 = lc.ProductTensor(v3, v4)
        self.assertAlmostEqual(tensor1, [(6,3),(0,3),(6,0),(2,1),(0,1),(2,0)])
        self.assertAlmostEqual(tensor2,[(4,-12),(4,4),(-2,2),(2,-6),(2,2),(-1,1),(6,-18),(6,6),(-3,3)])
if __name__ == '__main__':
    unittest.main()
