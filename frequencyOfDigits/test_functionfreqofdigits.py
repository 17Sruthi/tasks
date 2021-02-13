import unittest


class TestFreqOfDigits(unittest.TestCase):


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


    def test_digitnumbeboolean(self):
        print("\nUNIT-TESTING FOR INPUT DIGIT CASE 7: BOOLEAN AS INPUT")
        self.assertRaises(TypeError,numberwithdigit, True)

    def test_digitnumberstring(self):
        print("\nUNIT-TESTING FOR INPUT DIGIT CASE 8: STRING AS INPUT")
        self.assertRaises(TypeError,numberwithdigit, "string")

    def test_digitnumberintint(self):
        print("\nUNIT-TESTING FOR INPUT DIGIT CASE 9: INTEGER AS INPUT")
        self.assertIsInstance(numberwithdigit(3), (int,float))

    def test_digitnumberfloat(self):
        print("\nUNIT-TESTING FOR INPUT DIGIT CASE 10: FLOAT AS INPUT")
        self.assertIsInstance(numberwithdigit(8.3), (int,float))



def numbinput(numb):
    if(type(numb) not in [int]):
        raise TypeError("NUMBER MUST BE A POSITIVE INTEGER")
    elif(numb<1):
        raise ValueError("NUMBER CANNOT BE NEGATIVE")
    return numb 

def numberwithdigit(number):
    if(type(number) not in [int,float]):
        raise TypeError("INPUT MUST BE A NUMERIC VALUE HAVING DIGITS")
    return number

        
        
if __name__=='__main__':
    unittest.main()               
