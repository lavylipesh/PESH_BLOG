import unittest
from models import Quote
quote = quote.Quote

class QuoteTest(unittest.TestCase):
    def SetUp(self):
        self.new_quote = Quote('http://quotes.stormconsultancy.co.uk/random.json')
        def test_instance(self):
            self.assertTrue(isinstance(self.new_quote,Quote))
if __name__=='__main__':
    unittest.main()