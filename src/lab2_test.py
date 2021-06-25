import lab2
import unittest
class mTest(unittest.TestCase):
    def test_getNumber(self):
        self.assertEqual(str(lab2.getNumber(0)),"λf.λx.x")
    def test_isZero(self):
        self.assertEqual(str(lab2.betaConversation(lab2.isZero(lab2.getNumber(0)))),"λx.λy.x")
        self.assertEqual(str(lab2.betaConversation(lab2.isZero(lab2.getNumber(1)))),"λx.λy.y")
    def test_suc(self):
        self.assertEqual(str(lab2.betaConversation(lab2.suc(lab2.getNumber(0)))),"λf.λx.(f x)")
    def test_pred(self):
        self.assertEqual(str(lab2.betaConversation(lab2.pred(lab2.getNumber(1)))),"λf.λx.x")
    def test_plus(self):
        self.assertEqual(str(lab2.betaConversation(lab2.plus(lab2.getNumber(1),lab2.getNumber(0)))),"λf.λx.(f x)")
    def test_mutl(self):
        self.assertEqual(str(lab2.betaConversation(lab2.mult(lab2.getNumber(1),lab2.getNumber(0)))),"λf.λx.x")
    def test_factorial(self):
        self.assertEqual(str(lab2.betaConversation(lab2.factorial(lab2.getNumber(0)))), str(lab2.getNumber(1)))







