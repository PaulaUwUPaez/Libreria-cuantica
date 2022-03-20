#Escuela Colombiana de Ingeniera Julio Garabito
#Ing sistemas
#Paula Natalia Paez Vega

import math


def tensor_productv(vectorco1, vectorco2):
    """ producto tensor entre los vectores
    :parametros del vectorco1: vecotr de valores complejos
    :parametros del vectorco2: vectotr de valores complejos
    :return: producto tensor
    """
    longitud_tensor = len(vectorco1) * len(vectorco2)
    R = [(0, 0)] * longitud_tensor
    index = 0
    for i in range(len(vectorco1)):
        for j in range(len(vectorco2)):
            R[index] = multiplicacion_complejos(vectorco1[i], vectorco2[j])
            index += 1

    return R


def hermitiana(matriz):
    """ determina si una matriz es hermitiana
    :parametros de la matriz: una matriz de complejos
    :return: un valor booleano
    """
    matrizh = adjunta(matriz)
    if matrizh == matriz:
        return True
    else:
        return False


def unitaria(matriz):
    """ revisa si una matriz es unitaria
    :parametros de la matriz: matriz de complejos
    :return: valor booleano
    """
    matrizt = adjunta(matriz)
    identidad = [[(0, 0) for i in range(len(matriz[0]))] for j in range(len(matriz))]
    for i in range(len(identidad)):
        for j in range(len(identidad[0])):
            if i == j:
                identidad[i][j] = (1, 0)
    if multiplicacion_matrices(matrizt, matriz) == identidad:
        return True
    else:
        return False


def distanciav(vectorc1, vectorc2):
  "parametros del vectorc1: vector complejo"
  "parametros del vectorc2: vector complejo"
    if len(vectorc1) == len(vectorc2):
        dif1 = []
        for i in range(len(vectorc1)):
            dif1.append(resta_complejos(vectorc1[i], vectorc2[i]))
    productodif = int_product(dif1, dif1)
    distancia = modulo_complejos(productodif)

    return distancia


def norma_vector(vectorc):
    """ realiza la norma de un vector
    :parametros del vectorc: vector de complejos
    :return: norma del vector
    """
    productoint = int_product(vectorc, vectorc)
    norma = modulo_complejos(productoint)
    return norma


def int_product(vectorc1, vectorc2):
    """producto interno entre dos vectores complejos
    :parametros del vectorc1: vector de numeros complejos
    :parametros del vectorc2: vector de numeros complejos
    :return: porducto interno entre vecotres
    """
    if len(vectorc1) == len(vectorc2):
        productoint = (0, 0)
        vectorc1 = conjugadov(vectorc1)
        for i in range(len(vectorc1)):
            productoint = suma_complejos(productoint, multiplicacion_complejos(vectorc1[i], vectorc2[i]))

        return productoint
    else:
        return False


def accionmatriz_vector(matrix, vector):
    """ accion de una matriz sobre un vector
    :parametros del matrix: matriz de complejos
    :parametros del vector: vector de complejos
    :return: accion de la matriz sobre un vector
    """
    if len(matrix[0]) == len(vector):
        accion = []
        for i in range(len(matrix)):
            accion.append((0, 0))
        for i in range(len(matrix)):
            for j in range(len(vector)):
                for k in range(len(matrix[0])):
                    accion[i] = suma_complejos(accion[i], multiplicacion_complejos(matrix[i][k], vector[j]))
        return accion
    else:
        return False


def multiplicacion_matrices(matrix1, matrix2):
    """ multiplicacion entre matrices complejas
    :parametros de la matrix1: matriz de compliejos
    :parametros de la matrix2: matriz de complejos
    :return: producto entre matrices
    """
    if len(matrix1[0]) == len(matrix2):
        matrixr = []
        for i in range(len(matrix1)):
            matrixr.append([])
            for j in range(len(matrix2[0])):
                matrixr[i].append((0, 0))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix1[0])):
                    matrixr[i][j] = suma_complejos(matrixr[i][j],
                                                   multiplicacion_complejos(matrix1[i][k], matrix2[k][j]))

        return matrixr
    else:
        return False


def adjunta(matriz):
    """ adjunta de una matriz
    :parametros de la matriz: matriz de complejos
    :return: adjunta de la matriz
    """
    matrizad = conjugadom(transpuesta(matriz))

    return matrizad


def conjugadom(matriz):
    """ conjugado de una matriz de complejos
    :parametros de la matriz: matriz de complejos
    :return: conjugado de la matriz
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = conjugado_complejos(matriz[i][j])

    return matriz


def conjugadov(lista):
    """ conjugado de un vector de complejos
    :parametros de la lista: vector de complejos
    :return: conjugado vector o matriz de complejos
    """
    for i in range(len(lista)):
        lista[i] = conjugado_complejos(lista[i])
    return lista


def transpuesta(lista):
    """ transpuesta de una matriz
    :parametros de la lista: matriz de complejos
    :return: transpuesta de la matriz
    """
    transp = []
    for i in range(len(lista[0])):
        transp.append([])
        for j in range(len(lista)):
            transp[i].append(lista[j][i])

    return transp


def multiescalar_matrix(complexn, matrix):
    """multiplicacion escalar por una matriz
    :parametros del complexn: numero complejo
    :parametros matrix: matriz de complejos
    :return: multiplicacion escalar
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = multiplicacion_complejos(complexn, matrix[i][j])

    return matrix


def inversa_add_matrizc(matrizc):
    """inversa aditiva de una matriz compleja
    :parametros de la matrizc: matriz de numeros complejos
    :return: inversa aditiva de la matriz
    """
    for i in range(len(matrizc)):
        for j in range(len(matrizc[0])):
            matrizc[i][j] = multiplicacion_complejos((-1, 0), matrizc[i][j])

    return matrizc


def suma_matricesc(matrizc1, matrizc2):
    """suma de dos matricves complejas
    :parametros de la matrizc1: matriz de numeros complejos
    :type matrizc1: list
    :parametros de la matrizc2: matriz de numeros complejos
    :type matrizc2: matriz de numeros complejos
    :return: suma de las matrices
    :rtype: list
    """
    if len(matrizc1) == len(matrizc2) and len(matrizc1[0]) == len(matrizc2[0]):
        line = [(0, 0)] * len(matrizc1[0])
        matriz_r = [line] * len(matrizc1)
        for j in range(len(matrizc1)):
            for k in range(len(matrizc1[0])):
                matriz_r[j][k] = suma_complejos(matrizc1[j][k], matrizc2[j][k])

    return matriz_r


def multi_escalar(complex_num, complex_v):
    """ multiplicacion por un escalar
    :parametros del complex_num: un numero complejo
    :typecomplex_num: tuple
    :parametros del complex_v: vector complejo
    :type complex_v: list
    :return: vector resultante
    :rtype list
    """
    r_vector = [(0, 0)] * len(complex_v)
    for x in range(len(complex_v)):
        r_vector[x] = multiplicacion_complejos(complex_num, complex_v[x])

    return r_vector


def inverse_vectorcx(vectorc):
    """ inverso aditivo de un vector complejo
    :parametros del vectorc: vector de numeros complejos
    :return: inverso aditivo del vector ingresado
    :rtype: list
    """
    inverse_v = [(0, 0)] * len(vectorc)
    for x in range(len(vectorc)):
        inverse_v[x] = multiplicacion_complejos((-1, 0), vectorc[x])

    return inverse_v


def suma_vectorescpx(vectorc_1, vectorc_2):
    """ suma de dos vectores complejos
    :parametros del vectorc_1: vector complejo
    :parametros del vectorc_2: vector complejo
    :return: vector suma
    :rtype: list
    """
    if len(vectorc_1) == len(vectorc_2):
        svector = [(0, 0)] * len(vectorc_1)
        for x in range(len(vectorc_1)):
            svector[x] = (suma_complejos(vectorc_1[x], vectorc_2[x]))

    return svector


def potencia_polar(polar1, num):
    """potencia de un numero complejo en representación polar
    :parametros de polar1: numero complejo en representacion polar
    :type polar1: tuple
    :parametros del num: exponente
    :return: potencia del numero complejo
    :rtype: tuple
    """
    potencia_complejo = (round(polar1[0] ** num, 2), round(num * polar1[1], 2))

    return potencia_complejo


def division_polar(polar1, polar2):
    """division de dos numeros complejos en representacion polar
        :parametros del polar1: numero complejo en representacion polar
        :type polar1: tuple
        :parametros del polar2: numero complejo en representacion polar
        :type polar2: tuple
        :return: division entre los numeros complejos en representación polar
        :rtype: tuple
        """
    complejo_polar = (round(polar1[0] / polar2[0], 2), round(polar1[1] - polar2[1], 2))

    return complejo_polar


def multiplicacion_polar(polar1, polar2):
    """multiplicación de dos numeros complejos en representacion polar
    :parametros del polar1: numero complejo en representacion polar
    :type polar1: tuple
    :parametros del polar2: numero complejo en representacion polar
    :type polar2: tuple
    :return: producto entre los numeros complejos en representación polar
    :rtype: tuple
    """
    complejo_polar = (round(polar1[0] * polar2[0], 2), round(polar1[1] + polar2[1], 2))

    return complejo_polar


def rep_cartesiana(par):
    """representa un numero complejo en representanción cartesiana
    :parametros de par: representacion polar de un numero complejo
    :type par: tuple
    :return: representación cartesiana de un nnumero complejo
    :rtype: tuple
    """
    complejo = (round(par[0] * math.cos(par[1]), 2), round(par[0] * math.sin(par[1]), 2))

    return complejo


def rep_polar(par):
    """representa un numero complejo en una representacion polar
    :parametros de par: representacion cartesiana de un numero complejo
    :type par: tuple
    :return: representacion polar de un numero complejo
    :rtype: tuple
    """
    p = modulo_complejos(par)
    ang = round(math.atan(par[1] / par[0]), 2)
    result = (p, ang)

    return result


def conjugado_complejos(par):
    """ realiza el conjugado de un numero complejo
    :parametros de par: representacion de un numero complejo en coordenadas cartesianas
    :type par: tuple
    :return: el numero complejo conjugado
    :rtype: tuple
    """
    new_b = par[1] * -1
    new_par = (par[0], new_b)

    return new_par


def modulo_complejos(par):
    """ Realiza el conjugado de un numero complejo
    :parametros de par: representación de un numero complejo en coordenadas cartesianas
    :type par: tuple
    :return: un entero valor del modulo de un numero complejo
    :rtype: int
    """
    modulo = (par[0] ** 2 + par[1] ** 2)

    return round(math.sqrt(modulo), 2)


def division_complejos(par1, par2):
    """
    :parametros de par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: tuple
    :param par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: tuple
    :return: una lista como representación de el numero complejo resultante de la division
    :rtype: tuple
    """
    d = (par2[0] ** 2 + par2[1] ** 2)
    x = (par1[0] * par2[0] + par1[1] * par2[1]) / d
    y = (par2[0] * par1[1] - par1[0] * par2[1]) / d
    result = (round(x, 2), round(y, 2))

    return result


def resta_complejos(par1, par2):
    """Resta de dos numeros complejos
    :parametros del par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: tuple
    :parametros del par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: tuple
    :return: una lista como representación de el numero complejo resultante de la resta
    :rtype: tuple
    """
    result = (round(par1[0] - par2[0], 2), round(par1[1] - par2[1], 2))

    return result


def suma_complejos(par1, par2):
    """Suma dos numeros complejos
    :parametros de par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: tuple
    :parametros de par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: tuple
    :return: una lista como representación de el numero complejo resultante de la suma
    :rtype: tuple
    """
    result = (round(par1[0] + par2[0], 2), round(par1[1] + par2[1], 2))

    return result


def multiplicacion_complejos(par1, par2):
    """Multiplicacion de dos numeros complejos
    :parametros de par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: tuple
    :parametros de par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: tuple
    :return: una lista como representación de el numero complejo resultante de la multiplicacion
    :rtype: tuple
    """
    result = (round((par1[0] * par2[0]) - (par1[1] * par2[1]), 2), round((par1[0] * par2[1]) + (par1[1] * par2[0]), 2))

    return result


if __name__ == '__main__':
    print("Escriba el subprograma que desea usar como se indica en los comentarios""")
