import unittest


class TestNoToFig(unittest.TestCase):

    
    def test_numbinput(self):
        print("\nUNIT-TESTING CASE 1: 0 AS INPUT")
        self.assertRaises(ValueError,numbinput, 0)
        
    def test_numbinputnegative(self):
        print("\nUNIT-TESTING CASE 2: NEGATIVE INPUT")
        self.assertRaises(ValueError,numbinput, -6)
        
    def test_numbinputfloat(self): 
        print("\nUNIT-TESTING CASE 3: FLOAT INPUT")
        self.assertRaises(TypeError,numbinput,6.23)
        
    def test_numbinputboolean(self):
        print("\nUNIT-TESTING CASE 4: BOOLEAN INPUT")
        self.assertRaises(TypeError,numbinput, True)
        
    def test_numbinputstring(self):
        print("\nUNIT-TESTING CASE 5: STRING INPUT")
        self.assertRaises(TypeError,numbinput, "string")
    
    def test_numbinputvalid(self):
        print("\nUNIT-TESTING CASE 6: VALID INPUT")
        self.assertGreater(numbinput(3), 0)


    def test_intdigitnumbernegative(self):
        print("\nUNIT-TESTING CASE 7: NEGATIVE INPUT")
        self.assertRaises(ValueError,numberwithdigit, -6)

    def test_intdigitnumberboolean(self):
        print("\nUNIT-TESTING CASE 8: BOOLEAN INPUT")
        self.assertRaises(TypeError,numberwithdigit, True)

    def test_intdigitnumberstring(self):
        print("\nUNIT-TESTING CASE 9: STRING INPUT")
        self.assertRaises(TypeError,numberwithdigit, "string")

    def test_intdigitnumber(self):
        print("\nUNIT-TESTING CASE 10: VALID INPUT")
        self.assertIsInstance(numberwithdigit(3), (int))


def numbinput(numb):
    if(type(numb) not in [int]):
        raise TypeError("NUMBER MUST BE A POSITIVE INTEGER")
    elif(numb<1):
        raise ValueError("NUMBER CANNOT BE NEGATIVE")
    return numb 

def numberwithdigit(number):
    if(type(number) not in [int]):
        raise TypeError("INPUT MUST BE A NUMERIC VALUE HAVING DIGITS")
    elif(number<1):
        raise ValueError("NUMBER CANNOT BE NEGATIVE")
    return number        
        
if __name__=='__main__':
    unittest.main()         



