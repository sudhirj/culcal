from google.appengine.ext.db import *
from models.show import Show
import extendedtestcase

class ShowTests(extendedtestcase.ExtendedTestCase):
  def test_show_creation(self):
    self.assertRaises(BadValueError,Show,None)