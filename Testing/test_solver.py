from unittest import TestCase
from solver import Solver

__author__ = 'nickbortolotti'


class  TestSolver(TestCase):
  def test_negative(self):
      s = Solver
      self.assertRaises(Exception, s.demo, 2, 1, 2)

  def test_demo(self):
      self.fail()