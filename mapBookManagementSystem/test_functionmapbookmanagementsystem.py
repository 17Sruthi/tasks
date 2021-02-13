import unittest


class TestMapBook(unittest.TestCase):


    def test_choiceinput(self):
        print("\nUNIT-TESTING CASE 1: 0 AS INPUT")
        self.assertRaises(ValueError,choiceinput, 0)

    def test_choiceinputnegative(self):
        print("\nUNIT-TESTING CASE 2: NEGATIVE INPUT")
        self.assertRaises(ValueError,choiceinput, -6)        

    def test_choiceinputfloat(self):
        print("\nUNIT-TESTING CASE 3: FLOAT INPUT")
        self.assertRaises(TypeError,choiceinput,6.23)

    def test_choiceinputoutofrange(self):
        print("\nUNIT-TESTING CASE 4: OUT OF RANGE AS INPUT")
        self.assertRaises(ValueError,choiceinput,60)

    def test_choiceinputboolean(self):
        print("\nUNIT-TESTING CASE 5: BOOLEAN INPUT")
        self.assertRaises(TypeError,choiceinput, True)

    def test_choiceinputstring(self):
        print("\nUNIT-TESTING CASE 6: STRING INPUT")
        self.assertRaises(TypeError,choiceinput, "string")

    def test_choiceinputvalid(self):
        print("\nUNIT-TESTING CASE 7: VALID INPUT")
        self.assertIsInstance(choiceinput(3), int)


    def test_digitnumberboolean(self):
        print("\nUNIT-TESTING CASE 8: 0 AS INPUT")
        self.assertRaises(TypeError,numberofbooks, True)

    def test_digitnumberstring(self):
        print("\nUNIT-TESTING CASE 9: 0 AS INPUT")
        self.assertRaises(TypeError,numberofbooks, "string")

    def test_digitnumber(self):
        print("\nUNIT-TESTING CASE 10: 0 AS INPUT")
        self.assertRaises(ValueError,numberofbooks, 0)

    def test_digitnumbernegative(self):
        print("\nUNIT-TESTING CASE 11: 0 AS INPUT")
        self.assertRaises(ValueError,numberofbooks, -6)

    def test_digitnumberfloat(self):
        print("\nUNIT-TESTING CASE 12: 0 AS INPUT")
        self.assertRaises(TypeError,numberofbooks,6.23)

    def test_digitnumbervalid(self):
        print("\nUNIT-TESTING CASE 13: 0 AS INPUT")
        self.assertIsInstance(numberofbooks(3), int)


def choiceinput(numb):
    if(type(numb) not in [int]):
        raise TypeError("NUMBER MUST BE A POSITIVE INTEGER")
    elif(numb<1 or numb>7):
        raise ValueError("NUMBER MUST BE IN RANGE [1,7]")
    return numb 


def numberofbooks(number):
    if(type(number) not in [int]):
        raise TypeError("INPUT MUST BE A POSITIVE INTEGER")
    elif(number<1):
        raise ValueError("NUMBER CANNOT BE NEGATIVE")
    return number


        
if __name__=='__main__':
    unittest.main()
