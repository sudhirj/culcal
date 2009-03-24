import extendedtestcase
from google.appengine.ext.db import *
from models.show import Show

class ShowTests(extendedtestcase.ExtendedTestCase):
  def test_show_creation(self):
    self.assertRaises(BadValueError,Show,None)