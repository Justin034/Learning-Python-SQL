import unittest
import serial
import time

ser = serial.Serial("COM4", 115200, timeout=1)

def decode(ser):
    return ser.readline().decode("utf-8").strip()

class test_calc(unittest.TestCase):
    def test_on(self):
        ser.write(b"LED ON\n")
        self.assertEqual(decode(ser), 'OK')

    def test_on_off(self):
        ser.write(b"LED ON\n")
        self.assertEqual(decode(ser), "OK")
        time.sleep(1)
        ser.write(b"LED OFF\n")
        self.assertEqual(decode(ser), "OK")

    def test_ping(self):
        ser.write(b"PING\n")
        self.assertEqual(decode(ser), "PONG")

    def test_add(self):
        ser.write(b"ADD 4 5\n")
        self.assertEqual(decode(ser), "9")

if __name__ == '__main__':
    unittest.main()