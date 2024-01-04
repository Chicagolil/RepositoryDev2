#TP09 - LES TESTS UNITAIRES
# On continue avec la classe Fraction -> On va la tester
# Test Drive, Development : jsp cque c'est pcq et ça ne me concerne pas cheh
import unittest


# on va partir de la fonction factorielle pour illustrer tout l'essence de tp :

class exceptionParamNegatif(Exception):
    pass
def factorielle(n: int) -> int:
    """calcule la factorielle de n
    PRE : n est un entier
    POST : Renvoie n! si n>= 0
    RAISES : exceptionParamNegatif si n<0
    """
    if n > 0:
        resultat = n
        while n > 1:
            n -= 1
            resultat *= n
        return resultat
    elif n==0 :
        resultat = 1
        return resultat
    else:
        raise exceptionParamNegatif("\nUn paramètre négatif n'est pas accepté -> TU CONNAIS PAS TES MATH GROS CON \nNan mais une factorielle d'un nombre négatif on est ou là")



# 1ère étape : analyser la précondition -> n est un entier
# donc pour les tests il est logique de prendre un échantillon de valeurs :
# entières positives
# entières négatives
# après on fait un joli ptit tableau avec les résultats attendus QUI RESSEMBLE A CA :

"""
   n     |  Résultat
________ |________________
   -10   |  lance NegativeParamExcpetion
    -1   |  lance NegativeParamException 
     0   |  renvoie 1
     1   |  renvoie 1
     3   |  renvoie 6 
    10   |  renvoie un grand chiffre genre 3 628 800
"""

# Mtn ces test là on peut les créer
# Librairie unittest


class FactTestCase(unittest.TestCase):
    def testFactorielleEntierPositif(self):   # n > 0
        self.assertEqual(factorielle(1),1,"Factorielle(1)")
        self.assertEqual(factorielle(3), 6, "Factorielle(3)")
        self.assertEqual(factorielle(10), 3628800, "Factorielle(10)")


    def testFactorielleEntierNul(self): # boooo il est trop nul n==0
        self.assertEqual(factorielle(0),1,"Factorielle(0)")

    def testFactorielleEniterNegatif(self):   #n < 0
        with self.assertRaises(exceptionParamNegatif):
            factorielle(-1)
        with self.assertRaises(exceptionParamNegatif):
            factorielle(-10)
if __name__== '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# REM :
# les tests unitaires se focalisent prioritairement sur les préconditions

# MISE EN PRATIQUE__________________________________________________________________________________________________


import unittest
import pydoc
from math import gcd


class Fraction:
    """Classe qui représente une fraction et des opérations qu'on peut lui opérationner

    Auteur : Lilian Devroye
    Date : Novembre 2023
    Cette classe permet des manipulations et opérations sur les fractions
    """

    def __init__(self, num: int = 0, den: int = 1) -> int:
        """Construit la fraction avec un numérateur et dénominateur

        PRE : 'num' entier, 'den' est un entier non nul
        POST : crée une fraction représentée sous forme simplfiée ->  PGCD, les attributs sont privés
        RAISES : ZeroDivisionError si 'den' est nul -> on arrête tout
        """
        if den == 0:
            raise ZeroDivisionError("\nLe dénominateur est zéro, t'as cassé tout l'univers ")

        PGDC = gcd(abs(num), abs(den))
        self.__num = num // PGDC  # // division entière -> précaution pour ne pas obtenir de flottant , même si c'est le PGDC
        self.__den = den // PGDC

    @property
    def numerateur(self):
        """
        Getter pour le numérateur
        PRE:/
        POST : Renvoie le numérateur de la fraction

        """
        return self.__num

    @property
    def denominateur(self):
        """
        Getter pour le dénominateur
        PRE : /
        POST : Renvoie le dénominateur de la fraction

        """
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Renvoie une répresentation textuelle  de la fraction simplifiée

        PRE : /
        POST : Renvoie une représentation textuelle réduite de la fraction
        et renvoie le num si den==1
        """
        if self.__den == 1:
            return str(self.__num)
        return f'{self.__num}/{self.__den}'

    def as_mixed_number(self):
        """Retourne une représentation textuelle de la fraction sous forme de nombre mixte

        Un nombre mixe est une somme d'un entier et d'une fraction
        PRE : /
        POST : Renvoie la représentation textuelle sous forme de nombre mixte de la fraction réduite
                si par hasard il n'y a pas de reste, tqt on gère
        """
        partieEntier = self.__num // self.__den
        reste = self.__num % self.__den
        if reste == 0:
            return str(partieEntier)
        elif abs(self.__num / self.__den) < 1:
            return f'{reste}/{self.__den}'

        return f'{partieEntier} + {reste}/{self.__den}'

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """surcharge l'opérateur + pour les fractions

         PRE : 'other' est une instance de Fraction
         POST : Renvoie une nouvelle fraction représentant la somme des deux fractions
         """
        nveauNum = self.__num * other.__den + self.__den * other.__num
        nveauDen = self.__den * other.__den
        return Fraction(nveauNum, nveauDen)

    def __sub__(self, other):
        """surcharge l'opérateur - pour les fractions
        PRE : 'other' est une instance de Fraction
        POST : Renvoie une nouvelle fraction représentant la différence des deux fractions
        """
        nveauNum = self.__num * other.__den - self.__den * other.__num
        nveauDen = self.__den * other.__den
        return Fraction(nveauNum, nveauDen)

    def __mul__(self, other):
        """surcharge l'opérateur *  pour les fractions

               PRE : 'other' est une instance de Fraction
               POST : Renvoie une nouvelle fraction représentant la multiplication des deux fractions
               """

        nveauNum = self.__num * other.__num
        nveauDen = self.__den * other.__den
        return Fraction(nveauNum, nveauDen)

    def __truediv__(self, other):
        """Surcharge l'opérateur / pour les frations

        PRE : 'other' est une instance de Fraction et 'other' n'est pas une fraction nulle
        POST : Renvoie une nouvelle fraction représentant la division des deux fractions
        RAISES : ZeroDivisionError si 'den' est nul
        """
        if other.__num == 0:
            raise ZeroDivisionError("La division par zéro n'est pas autorisée.")
        nveauNum = self.__num * other.__den
        nveauDen = self.__den * other.__num
        return Fraction(nveauNum, nveauDen)

    def __pow__(self, power):
        """Surcharge l'opérateur ** pour les fractions

        PRE : 'other ' est un entier
        POST : Renvoie une nouvelle fraction représentant la puissance de la fraction
        """
        nveauNum = self.__num ** power
        nveauDen = self.__den ** power
        return Fraction(nveauNum, nveauDen)

    def __eq__(self, other):
        """Surcharge de l'opérateur == pour les fractions

        PRE : 'other' est une instance de Fraction
        POST : Renvoie True si les deux fractions sont équivalentes , False sinon

        """
        return self.__num == other.__num and self.__den == other.__den

    def __float__(self):
        """Retourne la valeur décimale de la fraction

        PRE : /
        POST : Renvoie la valeur décimale de la fraction
        """
        return self.__num / self.__den

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Vérifie si valeur de la fraction est 0

        POST : Renvoie True si la fraction est nulle, False sinon
        """
        return self.__num == 0

    def is_integer(self):
        """Vérifie si la fraction est un entier entier


        POST : Renvoie True si la fraction est un entier, False sinon
        """
        return self.__num / self.__den == int(self.__num / self.__den)

    def is_proper(self):
        """Vérifie si la valeur absolue de la fraction est < 1

        POST : Renvoie True si la fraction est propre, False sinon
        """
        return abs(self.__num) < abs(self.__den)

    def is_unit(self):
        """Vérifie si le numérateur de la fraction est 1 dans sa forme simplfiée


        POST : Renvoie True si le numérateur est 1, False sinon
        """
        return self.__num == 1

    def is_adjacent_to(self, other):
        """Vérifie si deux fractions diffèrent d'une fraction unitaire

        Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire

        POST : Renvoie True si les deux fractions sont adjacentes, False sinon
        """
        diff = abs(self.__num * other.__den - other.__num * self.__den)
        return diff == 1


class onVaLaTesterCteFraction(unittest.TestCase):
    pass

    def testCreationFraction(self):
        fraction = Fraction(3, 4)
        self.assertEqual(fraction.numerateur, 3)
        self.assertEqual(fraction.denominateur, 4)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def testRepresentationTextuelle(self):
        fraction1 = Fraction(5, 2)
        fraction2 = Fraction(3, 4)
        # __str__
        self.assertEqual(str(fraction1), '5/2')
        self.assertEqual(str(fraction2), '3/4')
        # as_mixed_number
        self.assertEqual(fraction1.as_mixed_number(), '2 + 1/2')
        self.assertEqual(fraction2.as_mixed_number(), '3/4')

    def testOperationsMathematiques(self):
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(2, 3)
        # __add__
        resultatAddition = fraction1 + fraction2
        self.assertEqual(resultatAddition.numerateur, 17)
        self.assertEqual(resultatAddition.denominateur, 12)

        # __sub__
        resultatSoustraction = fraction1 - fraction2
        self.assertEqual(resultatSoustraction.numerateur, 1)
        self.assertEqual(resultatSoustraction.denominateur, 12)

        # __mul__
        resultatMultiplication = fraction1 * fraction2
        self.assertEqual(resultatMultiplication.numerateur, 1)
        self.assertEqual(resultatMultiplication.denominateur, 2)

        # __truediv__
        resultatDivision = fraction1 / fraction2
        self.assertEqual(resultatDivision.numerateur, 9)
        self.assertEqual(resultatDivision.denominateur, 8)

        # __pow__
        resultatPuissance = fraction1 ** 2
        self.assertEqual(resultatPuissance.numerateur, 9)
        self.assertEqual(resultatPuissance.denominateur, 16)

    def testProprietesFraction(self):
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(4, 3)
        fraction3 = Fraction(5, 1)
        fraction4 = Fraction(0, 1)
        fraction5 = Fraction(1, 1)

        # is_zero
        self.assertFalse(fraction1.is_zero())
        self.assertTrue(fraction4.is_zero())

        # is_integer
        self.assertFalse(fraction1.is_integer())
        self.assertTrue(fraction3.is_integer())

        # is_proper
        self.assertTrue(fraction1.is_proper())
        self.assertFalse(fraction2.is_proper())

        # is_unit
        self.assertFalse(fraction1.is_unit())
        self.assertTrue(fraction5.is_unit())

        # is_adjacent_to
        self.assertFalse(fraction1.is_adjacent_to(Fraction(7, 4)))
        self.assertTrue(fraction1.is_adjacent_to(Fraction(2, 3)))

    def testConversionEnDecimal(self):
        fraction = Fraction(3, 4)
        self.assertEqual(float(fraction), 0.75)


if __name__ == '__main__':
    pydoc.writedoc(Fraction)
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

"""commentaires : 

____________________________________________________________________________________________________________________________________________________________________________________________________________________
erreur trouvée et corrigé dans as_mixed_number (gère désormais le cas ou la fraction est plus petite que 1)  :


          partieEntier = self.__num // self.__den
                reste = self.__num % self.__den
                if reste == 0:
                    return str(partieEntier)

                return f'{partieEntier} + {reste}/{self.__den}'

    remplacé par


          partieEntier = self.__num // self.__den
                reste = self.__num % self.__den
                if reste == 0:
                    return str(partieEntier)
                elif abs(self.__num / self.__den) < 1:
                    return f'{reste}/{self.__den}'

                return f'{partieEntier} + {reste}/{self.__den}'

___________________________________________________________________________________________________________________________________________________________________________________________________________                
erreur trouvée et corrgée dans __add__ (erreur entre paranthèses) :
        nveauNum = self.__num * other.__den + self.__den * (self.__num)
                nveauDen = self.__den * other.__den
                return Fraction(nveauNum,nveauDen)

    remplacé par :

        nveauNum = self.__num * other.__den + self.__den * (other.__num)
                nveauDen = self.__den * other.__den
                return Fraction(nveauNum,nveauDen)

_____________________________________________________________________________________________________________________________________________________________________________________________________________
erreur trouvée et corrigée dans __sub__ : exactement la même qu'au dessus -> un self.num au lieu d'un other.num
_____________________________________________________________________________________________________________________________________________________________________________________________________________

différentes fautes de frappes dans l'écriture des tests -> un True au lieu d'un False, etc...
"""
