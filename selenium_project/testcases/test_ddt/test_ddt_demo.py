import unittest
import os
from ddt import ddt, data, unpack,file_data



@ddt
class TestDDT(unittest.TestCase):
    @data(1,2,3)
    def test_ddt_demo(self, value):
        print(value)
    
    @data((1,2),(3,4),(5,6))
    def test_2(self, value):
        print(value)

    @data((1, 2), (3, 4))
    @unpack
    def test_3(self, value1, value2):
        print(value1, value2)
    
    @data({'name': 'tom', 'age': 10}, {'name': 'ken', 'age': 11})
    def test_4(self, value):
        print(value)    
    
    @data({'name': 'tom', 'age': 10}, {'name': 'ken', 'age': 11})
    @unpack
    def test_5(self,name, age):
        print(name,age)

if __name__ == '__main__':  
    unittest.main()
