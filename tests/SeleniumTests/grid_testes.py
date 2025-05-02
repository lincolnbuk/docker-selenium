import unittest
from __init__ import SeleniumGenericTests

if __name__ == "__main__":
    # Adiciona os testes da classe SeleniumGenericTests
    suite = unittest.TestLoader().loadTestsFromTestCase(SeleniumGenericTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
