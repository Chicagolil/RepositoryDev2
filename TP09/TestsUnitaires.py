from Fraction import Fraction
import unittest
import coverage


class onVaLaTesterCteFraction(unittest.TestCase):

    def testCreationFraction(self):
        fraction = Fraction(3, 4)
        fraction1 = Fraction(2, 4)
        fraction2 = Fraction(1, -3)
        fraction3 = Fraction(-3, -4)
        fraction4 = Fraction(0, 1)
        fraction5 = Fraction(4, 2)
        self.assertEqual(fraction.numerateur, 3)
        self.assertEqual(fraction.denominateur, 4)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)
        self.assertEqual(fraction1.numerateur, 1)
        self.assertEqual(fraction1.denominateur, 2)
        self.assertEqual(fraction2.numerateur, -1)
        self.assertEqual(fraction2.denominateur, 3)
        self.assertEqual(fraction3.numerateur, 3)
        self.assertEqual(fraction3.denominateur, 4)
        self.assertEqual(fraction4.numerateur, 0)
        self.assertEqual(fraction4.denominateur, 1)
        self.assertEqual(fraction5.numerateur, 2)
        self.assertEqual(fraction5.denominateur, 1)
    def testRepresentationTextuelle(self):
        fraction1 = Fraction(5, 2)
        fraction2 = Fraction(3, 4)
        fraction3 = Fraction(4, 2)
        fraction4 = Fraction(1, -2)
        # __str__
        self.assertEqual(str(fraction1), '5/2')
        self.assertEqual(str(fraction2), '3/4')
        self.assertEqual(str(fraction3), '2')
        self.assertEqual(str(fraction4), '-1/2')
        # as_mixed_number
        self.assertEqual(fraction1.as_mixed_number(), '2 + 1/2')
        self.assertEqual(fraction2.as_mixed_number(), '3/4')
        self.assertEqual(str(fraction3), '2')
        self.assertEqual(str(fraction4), '-1/2')

    def testOperationsMathematiques(self):
        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(2, 3)
        fraction3 = Fraction(1, -3)
        fraction4 = Fraction(0, 1)
        fraction5 = Fraction(0, 4)
        fraction6 = Fraction(4, 2)
        fraction7 = Fraction(9, 3)
        fraction8 = Fraction(-4, 2)
        fraction9 = Fraction(-9,3)
        # __add__
        resultatAddition = fraction1 + fraction2
        self.assertEqual(resultatAddition.numerateur, 17)
        self.assertEqual(resultatAddition.denominateur, 12)
        resultatAddition1 = fraction1 + fraction3
        self.assertEqual(resultatAddition1.numerateur, 5)
        self.assertEqual(resultatAddition1.denominateur, 12)
        resultatAddition2 = fraction2 + fraction4
        self.assertEqual(resultatAddition2.numerateur, 2)
        self.assertEqual(resultatAddition2.denominateur, 3)
        resultatAddition3 = fraction4 + fraction5
        self.assertEqual(resultatAddition3.numerateur, 0)
        self.assertEqual(resultatAddition3.denominateur, 1)
        resultatAddition4 = fraction6 + fraction7
        self.assertEqual(resultatAddition4.numerateur, 5)
        self.assertEqual(resultatAddition4.denominateur, 1)

        # __sub__
        resultatSoustraction = fraction1 - fraction2
        self.assertEqual(resultatSoustraction.numerateur, 1)
        self.assertEqual(resultatSoustraction.denominateur, 12)
        resultatSoustraction1 = fraction1 - fraction3
        self.assertEqual(resultatSoustraction1.numerateur, 13)
        self.assertEqual(resultatSoustraction1.denominateur, 12)
        resultatSoustraction2 = fraction2 - fraction4
        self.assertEqual(resultatSoustraction2.numerateur, 2)
        self.assertEqual(resultatSoustraction2.denominateur, 3)
        resultatSoustraction3 = fraction4 - fraction5
        self.assertEqual(resultatSoustraction3.numerateur, 0)
        self.assertEqual(resultatSoustraction3.denominateur, 1)
        resultatSoustraction4 = fraction8 - fraction9
        self.assertEqual(resultatSoustraction4.numerateur, 1)
        self.assertEqual(resultatSoustraction4.denominateur, 1)
        # __mul__
        resultatMultiplication = fraction1 * fraction2
        self.assertEqual(resultatMultiplication.numerateur, 1)
        self.assertEqual(resultatMultiplication.denominateur, 2)
        resultatMultiplication1 = fraction6 * fraction3
        self.assertEqual(resultatMultiplication1.numerateur, -2)
        self.assertEqual(resultatMultiplication1.denominateur, 3)
        resultatMultiplication2 = fraction3 * fraction9
        self.assertEqual(resultatMultiplication2.numerateur, 1)
        self.assertEqual(resultatMultiplication2.denominateur, 1)
        resultatMultiplication3 = fraction1 * fraction4
        self.assertEqual(resultatMultiplication3.numerateur, 0)
        self.assertEqual(resultatMultiplication3.denominateur, 1)
        resultatMultiplication4 = fraction6 * fraction7
        self.assertEqual(resultatMultiplication4.numerateur, 6)
        self.assertEqual(resultatMultiplication4.denominateur, 1)

        # __truediv__
        resultatDivision = fraction1 / fraction2
        self.assertEqual(resultatDivision.numerateur, 9)
        self.assertEqual(resultatDivision.denominateur, 8)
        resultatDivision1 = fraction1 / fraction3
        self.assertEqual(resultatDivision1.numerateur, -9)
        self.assertEqual(resultatDivision1.denominateur, 4)
        resultatDivision2 = fraction8 / fraction3
        self.assertEqual(resultatDivision2.numerateur, 6)
        self.assertEqual(resultatDivision2.denominateur, 1)
        with self.assertRaises(ZeroDivisionError):
            fraction6 / fraction4

        resultatDivision3 = fraction4 / fraction7
        self.assertEqual(resultatDivision3.numerateur, 0)
        self.assertEqual(resultatDivision3.denominateur, 1)


        # __pow__
        resultatPuissance = fraction1 ** 2
        self.assertEqual(resultatPuissance.numerateur, 9)
        self.assertEqual(resultatPuissance.denominateur, 16)
        resultatPuissance1 = fraction3 ** 2
        self.assertEqual(resultatPuissance1.numerateur, 1)
        self.assertEqual(resultatPuissance1.denominateur, 9)
        resultatPuissance2 = fraction1 ** 1
        self.assertEqual(resultatPuissance2.numerateur, 3)
        self.assertEqual(resultatPuissance2.denominateur, 4)
        resultatPuissance3 = fraction1 ** 0
        self.assertEqual(resultatPuissance3.numerateur, 1)
        self.assertEqual(resultatPuissance3.denominateur, 1)

        # __eq__
        self.assertTrue(fraction1 == fraction1)
        self.assertFalse(fraction8 == fraction6)


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
        fraction1 = Fraction(4,2)
        fraction2 = Fraction(-1,3)
        fraction3 = Fraction(-9,3)
        self.assertEqual(float(fraction), 0.75)
        self.assertEqual(float(fraction1), 2)
        self.assertEqual(float(fraction2), -0.33)
        self.assertEqual(float(fraction3), -3)



if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    cov.stop()
    cov.report()





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
