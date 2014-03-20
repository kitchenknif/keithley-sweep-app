from Keithley import Keithley

class Keithley_24XX(Keithley):
    'Keithley 24XX I-V Measurement Class'

    def __init__(self, port, supportPulse):
        self.port = port
        self.supportPulse = supportPulse
    
    def __del__(self):
        self.port.close()

    def doLegacySweep(self, startV=0.0, endV=3.0, numberOfPoints=100, remoteSensing=True, logSteps=False, autorange=True, range=1e-3, limit=1.0, pulseSweep=False, pulseWidth=1e-3, pulseDelay=1e0):
        if self.port.closed == True:
            return False
        if not self.supportPulse and pulseSweep:
            return False
            
        self.port.write(b"*RST;\n")
        self.port.flushInput()
    
        if autorange and not pulseSweep:
            self.port.write(b":SOUR:SWE:RANG AUTO;\n")
        else:
            s =  ":SENS:CURR:RANGE " + str(range) + ";\n"
            self.port.write(s.encode('ascii'))
        
        if remoteSensing:
            self.port.write(b":SYST:RSEN ON;\n")
        else:
            self.port.write(b":SYST:RSEN OFF;\n")
       
        s = "" 
    
        if not pulseSweep:
            s += ":SENS:CURR:NPLC 10; :TRIG:COUN " + str(numberOfPoints) + "; "
            s += ":SOUR:FUNC VOLT; :SENS:FUNC \"CURR\"; :SENS:FUNC:CONC ON; :SENS:CURR:PROT " + str(limit) + "; "
            s += ":SOUR:VOLT:START " + str(startV) + "; :SOUR:VOLT:STOP " + str(endV) + "; "
            s += ":SOUR:VOLT:STEP " + str( (endV - startV)/(numberOfPoints-1.0)) + "; :SOUR:VOLT:MODE SWE; "
            s += ":FORM:ELEM VOLT,CURR; "
            if logSteps:
                s += ":SOUR:SWE:SPAC LOG; "
            else:
                s += ":SOUR:SWE:SPAC LIN; "
            s += ":OUTP ON; :READ?; :SYST:BEEP 500,1;\n"
        else:
            s += ":SOUR:FUNC:SHAP PULS; :SOUR:PULS:WIDT " + str(pulseWidth) + "; "
            s += ":SOUR:PULS:DEL " + str(pulseDelay) + "; " 
            s += ":SENS:CURR:NPLC 0.1; :TRIG:COUN " + str(numberOfPoints) + "; "
            s += ":SOUR:FUNC VOLT; :SENS:FUNC \"CURR\"; :SENS:FUNC:CONC ON; :SENS:CURR:PROT " + str(limit) + "; "
            s += ":SOUR:VOLT:START " + str(startV) + "; :SOUR:VOLT:STOP " + str(endV) + "; "
            s += ":SOUR:VOLT:STEP " + str( (endV - startV)/(numberOfPoints-1.0)) + "; :SOUR:VOLT:MODE SWE; "
            s += ":FORM:ELEM VOLT,CURR; "
            if logSteps:
                s += ":SOUR:SWE:SPAC LOG; "
            else:
                s += ":SOUR:SWE:SPAC LIN; "
            s += ":OUTP ON; :READ?; :SYST:BEEP 500,1;\n"

        self.port.write(s.encode('ascii'))          

        return True
    
    def legacyReadDataPoints(self,numberOfPoints):
        dataPoints = []
        self.port.write(b":OUTP OFF;\n")
        p = self.port.readline()
        
        t = p.split(b",")
        for i in range(0, len(t), 2):    
            try:
                dataPoints.append([float(t[i]), float(t[i+1])])
            except ValueError:
                pass
        return dataPoints