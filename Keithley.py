import serial

class Keithley:
    'Keithley Generic SourceMeter Class'
        
    @staticmethod
    def factory(type, port):
        if "2430" in type: return Keithley_24XX(port, True)
        if "2400" in type: return Keithley_24XX(port, False)
        if "2635a" in type: return Keithley_2635a(port, True)
        assert 0, "Bad identification string: " + type