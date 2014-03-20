from Keithley import Keithley

class Keithley_2635a(Keithley):
    'Keithley 2635a I-V Measurement Class'

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