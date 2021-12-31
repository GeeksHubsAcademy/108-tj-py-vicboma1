import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):
    
    def test_apply_1(self):
        expected = "None";
        result = apply(None);
        assert(expected == result) 

    def test_apply_1(self):
        expected =  61000;
        result = apply(0,1,1);
        assert(expected == result) 

    def test_apply_2(self):
        expected =  0;
        result = apply(0,0,0);
        assert(expected == result) 

    def test_apply_3(self):
        expected =  3601000;
        result = apply(1,0,1);
        assert(expected == result) 

    def test_apply_4(self):
        expected =  3661000;
        result = apply(1,1,1);
        assert(expected == result) 

    def test_apply_5(self):
        expected =  3600000;
        result = apply(1,0,0);
        assert(expected == result) 

    def test_apply_6(self):
        expected =  60000;
        result = apply(0,1,0);
        assert(expected == result) 

    def test_apply_7(self):
        expected =  1000;
        result = apply(0,0,1);
        assert(expected == result) 

    def test_apply_8(self):
        expected =  86399000;
        result = apply(23,59,59);
        assert(expected == result) 

    def test_apply_9(self):
        expected =  -1;
        result = apply(24,10,10);
        assert(expected == result) 

    def test_apply_10(self):
        expected =  -1;
        result = apply(1,60,0);
        assert(expected == result) 

    def test_apply_11(self):
        expected =  -1;
        result = apply(0,0,60);
        assert(expected == result) 

    def test_apply_12(self):
        expected =  55506000;
        result = apply(15,25,6);
        assert(expected == result) 

    def test_apply_13(self):
        expected =  85510000;
        result = apply(23,45,10);
        assert(expected == result) 

    def test_apply_14(self):
        expected =  37508000;
        result = apply(10,25,8);
        assert(expected == result) 

    def test_apply_15(self):
        expected =  2400000;
        result = apply(0,40,0);
        assert(expected == result) 

    def test_apply_16(self):
        expected =  -1;
        result = apply(-1,12,0);
        assert(expected == result) 

    def test_apply_17(self):
        expected =  -1;
        result = apply(50,-1,16);
        assert(expected == result) 

    def test_apply_18(self):
        expected =  -1;
        result = apply(39,45,-1);
        assert(expected == result) 

    def test_apply_19(self):
        expected =  21966000;
        result = apply(6,6,6);
        assert(expected == result) 

    def test_apply_20(self):
        expected =  -1;
        result = apply(99,76,60);
        assert(expected == result) 
    

if __name__ == '__main__':
	unittest.main()