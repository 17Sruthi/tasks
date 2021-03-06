import unittest


class TestWordCount(unittest.TestCase):

    
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


def numbinput(numb):
    if(type(numb) not in [int]):
        raise TypeError("NUMBER MUST BE A POSITIVE INTEGER")
    elif(numb<1):
        raise ValueError("NUMBER CANNOT BE NEGATIVE")
    return numb
        
        
if __name__=='__main__':
    unittest.main()

                 
