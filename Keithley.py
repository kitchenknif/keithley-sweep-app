import serial

class Keithley:
    'Keithley Generic SourceMeter Class'
        
    @staticmethod
    def factory(type, port):
        if "2430" in type: return Keithley_24XX(port, True)
        if "2400" in type: return Keithley_24XX(port, False)
        if "2635a" in type: return Keithley_2635a(port, True)
        assert 0, "Bad identification string: " + type

#
# Keithley 24XX
#        
        
        
class Keithley_24XX(Keithley):
    'Keithley 24XX I-V Measurement Class'

    def __init__(self, port, supportPulse):
        self.port = port
        self.port.open()
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
    
        if autorange:
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
# Keithley 2635a
#        

class Keithley_2635a(Keithley):
    'Keithley 2635a I-V Measurement Class'

    def __init__(self, port, supportPulse):
        self.port = port
        self.port.open()
        self.supportPulse = supportPulse
    
    def __del__(self):
        self.port.close()

    def doLegacySweep(self, startV=0.0, endV=3.0, numberOfPoints=100, remoteSensing=True, logSteps=False, autorange=True, range=1e-3, limit=1.0, pulseSweep=False, pulseWidth=1e-3, pulseDelay=1e0):
        if self.port.closed == True:
            return False
        if not self.supportPulse and pulseSweep:
            return False
        self.port.write(b"reset(); smua.nvbuffer1.clear(); errorqueue.clear(); \n")
        s = "smua.source.limiti = " + str(limit) + ';\n'
        self.port.write(s.encode('ascii'))
    
        if autorange and not pulseSweep:
            self.port.write(b"smua.measure.autorangei = smua.AUTORANGE_ON; smua.measure.lowrangei = 10e-12;\n")
            self.port.write(b"smua.measure.autorangev = smua.AUTORANGE_ON; smua.measure.lowrangev = 10e-12;\n")
            self.port.write(b"smua.source.autorangei = smua.AUTORANGE_ON; smua.source.lowrangei = 10e-9;\n")
            self.port.write(b"smua.source.autorangev = smua.AUTORANGE_ON; smua.source.lowrangev = 10e-9;\n")
        else:
            s =  "smua.measure.autorangev = smua.AUTORANGE_OFF;smua.measure.autorangei = smua.AUTORANGE_OFF; smua.measure.rangei = " + str(range) + ";\n"
            s += "smua.source.autorangei = smua.AUTORANGE_OFF;smua.source.autorangev = smua.AUTORANGE_OFF; smua.source.rangev = " + str(range) + ";\n"
            s += "smua.measure.autozero = smua.AUTOZERO_ONCE; \n";
            self.port.write(s.encode('ascii'))
        
        if remoteSensing:
            self.port.write(b"smua.sense = smua.SENSE_REMOTE; \n")
        else:
            self.port.write(b"smua.sense = smua.SENSE_REMOTE; \n")
    
        self.port.write(b"smua.source.output = smua.OUTPUT_ON; \n")
        self.port.write(b"smua.measure.nplc = 25; \n")
    
        s = "" 
    
        if not pulseSweep:
            if logSteps:
                s += "SweepVLogMeasureI(smua, "
            else:
                s += "SweepVLinMeasureI(smua, "
            s += str(startV) + ', ' + str(endV) + ', ' + str(0.1) + ', ' + str(numberOfPoints) + ');\n'
        else:
            if logSteps:
                s += "f, msg = ConfigPulseVMeasureISweepLog"
            else:
                s += "f, msg = ConfigPulseVMeasureISweepLin"
            s += "(smua,0," + str(startV) + ', ' + str(stopV) + ', ' + str(limit) + ', ', + str(pulseWidth) + ', ' + str(pulseDelay) + ', ' + str(numPoints) + "smua.nvbuffer1, 1)"
            s += "smua.nvbuffer1.appendmode=1; \n"
            s += "f1, msg1 = InitiatePulseTest(1);" 
            s += "smua.source.output = smua.OUTPUT_OFF\n";

        self.port.write(s.encode('ascii'))
        self.port.write(b"smua.source.output = smua.OUTPUT_OFF; \n")           

        return True
    
    def legacyReadDataPoints(self, numberOfPoints):
        self.port.flushInput()
        dataPoints = []
        for i in range (1, numberOfPoints+1):
            s = "printbuffer(" + str(i) + ", " + str(i) + ", smua.nvbuffer1.sourcevalues,smua.nvbuffer1.readings); \n"
            self.port.write(s.encode('ascii'))
        
            p = self.port.readline()
        
            l = []
            for t in p.split(b","):
                try:
                    l.append(float(t))
                except ValueError:
                    pass
            dataPoints.append(l)
        return dataPoints         