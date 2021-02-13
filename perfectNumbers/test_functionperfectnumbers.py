import unittest


class TestPerfectNumber(unittest.TestCase):

    
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


    def test_digitnumber(self):
        print("\nUNIT-TESTING CASE 7: BOOLEAN INPUT")
        self.assertRaises(ValueError,numberwithdigit, 0)

    def test_digitnumbernegative(self):
        print("\nUNIT-TESTING CASE 8: NEGATIVE INPUT")
        self.assertRaises(ValueError,numberwithdigit, -6)

    def test_digitnumberfloat(self):
        print("\nUNIT-TESTING CASE 9: FLOAT INPUT")
        self.assertRaises(TypeError,numberwithdigit, 3.5)

    def test_digitnumberboolean(self):
        print("\nUNIT-TESTING CASE 10: BOOLEAN INPUT")
        self.assertRaises(TypeError,numberwithdigit, True)

    def test_digitnumberstring(self):
        print("\nUNIT-TESTING CASE 11: STRING INPUT")
        self.assertRaises(TypeError,numberwithdigit, "string")

    def test_digitnumbervalid(self):
        print("\nUNIT-TESTING CASE 12: VALID INPUT")
        self.assertIsInstance(numberwithdigit(3), (int))



def numbinput(numb):
    if(type(numb) not in [int]):
        raise TypeError("NUMBER MUST BE A POSITIVE INTEGER")
    elif(numb<1):
        raise ValueError("NUMBER CANNOT BE NEGATIVE")
    return numb 

def numberwithdigit(number):
    if(type(number) not in [int]):
        raise TypeError("INPUT MUST BE A POSITIVE INTEGER")
    elif(number<1):
        raise ValueError("NUMBER CANNOT BE NEGATIVE")
    return number

        
        
if __name__=='__main__':
    unittest.main()                 
