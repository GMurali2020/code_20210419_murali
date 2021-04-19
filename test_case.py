import unittest

from .bmi_calculator import health_risk

class SimpleTest(unittest.TestCase):
   @unittest.skip("demonstrating skipping")
   def testadd1(self):
      self.assertEquals(health_risk(56.140351),"High risk")

if __name__ == '__main__':
   unittest.main()