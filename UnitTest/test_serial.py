import unittest
import serial
import time




class test_calc(unittest.TestCase):

    @staticmethod
    def decode(ser):
        return ser.readline().decode("utf-8").strip()

    @classmethod
    def setUpClass(cls):
        cls.ser = serial.Serial("COM6", 115200, timeout=1)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.ser.close()

    def test_on(self):
        self.ser.write(b"LED ON\n")
        self.assertEqual(self.decode(self.ser), 'OK')

    def test_on_off(self):
        self.ser.write(b"LED ON\n")
        self.assertEqual(self.decode(self.ser), "OK")
        time.sleep(1)
        self.ser.write(b"LED OFF\n")
        self.assertEqual(self.decode(self.ser), "OK")

    def test_ping(self):
        self.ser.write(b"PING\n")
        self.assertEqual(self.decode(self.ser), "PONG")

    def test_add(self):
        self.ser.write(b"ADD 4 5\n")
        self.assertEqual(self.decode(self.ser), "9")

if __name__ == '__main__':
    
    unittest.main()