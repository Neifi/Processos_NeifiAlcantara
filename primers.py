# -*- coding: utf-8 -*-

import sys


class llista_primers:
    """
    Llista els primers numeros fins a n

    >>> llista_primers(3).llista
    [2, 3, 5]

    >>> llista_primers(7).llista
    [2, 3, 5, 7, 11, 13, 17]

    >>> llista_primers(10).llista
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """

    def __init__(self, n):
        # Es defineix una llista buida
        self.n = n
        self.llista = []
        self.busca()

    def busca(self):
        """
        Busca els primers utilitzan el módul i els afegeix a la llista
        """
        if (len(self.llista) == 0):
            self.llista.append(2)
            self.busca()
        elif (len(self.llista) < self.n):
            trobat = False
            seguent = self.llista[-1]+1
            # seguent val el ultim valor de la llista més 1

            while not trobat:
                for i in self.llista:
                    if seguent % i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)
            self.busca()


if __name__ == '__main__':

    import doctest
    doctest.testmod()
