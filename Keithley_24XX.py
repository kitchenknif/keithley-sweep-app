from Keithley import Keithley

class Keithley_24XX(Keithley):
    'Keithley 24XX I-V Measurement Class'

    def __init__(self, port, supportPulse):
        self.port = port
        self.supportPulse = supportPulse
        self.DCArmed = False
        self.PulseArmed = False
    
    def __del__(self):
        self.port.close()

    
    #
    # Factory Sweep Thing
    #
    
    def doLegacySweep(self, startV=0.0, endV=3.0, numberOfPoints=100, remoteSensing=True, logSteps=False, autorange=True, range=1e-3, limit=1.0, pulseSweep=False, pulseWidth=1e-3, pulseDelay=1e0):
        if self.port.closed == True:
            return False
        if not self.supportPulse and pulseSweep:
            return False
            
        self.port.write(b"*RST;\n")
        self.port.flushInput()
        
        self.DCArmed = False
        self.PulseArmed = False    
        
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
        
    #
    # Realtime DC Sweep
    #
    
    def armDCMeasurements(self, remoteSensing=True, autorange=True, range=1e-3, limit=1.0):
         if self.port.closed == True:
            return False

        self.port.write(b"*RST;\n")
        self.port.flushInput()
    
        self.PulseArmed = False
    
        if autorange
            self.port.write(b":SOUR:SWE:RANG AUTO;\n")
        else:
            s =  ":SENS:CURR:RANGE " + str(range) + ";\n"
            self.port.write(s.encode('ascii'))
        
        if remoteSensing:
            self.port.write(b":SYST:RSEN ON;\n")
        else:
            self.port.write(b":SYST:RSEN OFF;\n")
       
        s = "" 
    
        s += ":SENS:CURR:NPLC 10; "
        s += ":SOUR:FUNC VOLT; "
        s += ":SENS:FUNC \"CURR\"; "
        s += ":SENS:FUNC:CONC ON; "
        s += ":SENS:CURR:PROT " + str(limit) + "; "
        s += ":FORM:ELEM VOLT,CURR; "
        s += ":SOUR:CLE:AUTO ON; "

        self.port.write(s.encode('ascii'))          

        self.DCArmed = True
        return True   
    def getDCPoint(self, voltage=1.0, repeats=2):
         if not self.DCArmed:
            return False
         
         if self.port.closed == True:
            return False
        s = "" 
    
        s += ":TRIG:COUN " + str(repeats) + "; "
        s += ":SOUR:VOLT " + str(voltage) + "; "
        s += "READ?; "

        self.port.write(s.encode('ascii'))          

        dataPoint = [0.0, 0.0]
        p = self.port.readline()
        
        t = p.split(b",")
        for i in range(0, len(t), 2):    
            try:
                dataPoint[0] += float(t[i])
                dataPoint[1] += float(t[i+1])
            except ValueError:
                pass
        dataPoint[0] /= repeats
        dataPoint[1] /= repeats        
        return dataPoint

    #
    # Realtime Pulse Sweep
    #
    def armPulseMeasurements(self, remoteSensing=True, limit=1.0, pulseWidth=1e-3, pulseDelay=1e0):
         if self.port.closed == True:
            return False

        self.port.write(b"*RST;\n")
        self.port.flushInput()

        self.DCArmed = False

        if remoteSensing:
            self.port.write(b":SYST:RSEN ON;\n")
        else:
            self.port.write(b":SYST:RSEN OFF;\n")
       
        s = "" 
    
        s += ":SOUR:FUNC:SHAP PULS; "
        s += ":SOUR:PULS:WID " + str(pulseWidth) + "; "
        s += ":SOUR:PULS:DEL " + str(pulseDelay) + "; " 
        s += ":SOUR:FUNCtion VOLT; "
        s += ":SOUR:VOLT:MODE FIX; "
        s += ":SENS:FUNC \"CURR\"; "
        s += " :SENS:FUNC:CONC ON;"
        s += ":SENS:CURR:NPLC 0.1; "
        s += ":SENS:CURR:PROT " + str(limit) + "; "
        s += ":FORM:ELEM VOLT,CURR; "
        s += ":SYST:AZER ON; "
        

        self.port.write(s.encode('ascii'))          
        self.PulseArmed = True
        
        return True   
        
    def getPulsePoint(self, voltage=1.0, repeats=2, vRange=1e-2, cRange=1e-3):
        if not self.PulseArmed:
            return False
        
        if self.port.closed == True:
            return False
        s = "" 
        s += ":SOUR:VOLT:RANG " + str(vRange) + "; "
        s += ":SOUR:VOLT:LEV " + str(voltage) + "; "

        s += ":SENS:CURR:RANG " + str(cRange) + "; "

        s += ":TRIG:COUN " + str(repeats) + "; "
        s += ":READ?    
        s += ":TRIG:COUN " + str(repeats) + "; "
        s += ":SOUR:VOLT " + str(voltage) + "; "
        s += "READ?; "

        self.port.write(s.encode('ascii'))          

        dataPoint = [0.0, 0.0]
        p = self.port.readline()
        
        t = p.split(b",")
        for i in range(0, len(t), 2):    
            try:
                dataPoint[0] += float(t[i])
                dataPoint[1] += float(t[i+1])
            except ValueError:
                pass
        dataPoint[0] /= repeats
        dataPoint[1] /= repeats        
        return dataPoint    
                    s =  ":SENS:CURR:RANGE " + str(range) + ";\n"
            self.port.write(s.encode('ascii'))
    