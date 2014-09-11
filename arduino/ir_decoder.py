__author__ = 'agervail'
import serial
import sys

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.readline()
f = open('ir_codes.txt', 'w')
try:
    while True:
        d = []
        code = ser.readline()
        #print code
        if '[' in code and ']' in code:
            data = code[1:-1].split(',')
            for i in range(len(data) / 2):
                val = int(data[i * 2 + 1])
                if val > 200:
                    d.append('2')
                elif val > 100:
                    d.append('1')
                else:
                    d.append('0')
            #print d

            i1 = 17
            bstr = ''.join(d[17:17 + 8])
            #print bstr
            if not '2' in bstr:
                print hex(int(bstr, 2)),
                f.write(hex(int(bstr, 2)))
                f.write(', ')


        # for i in range(17, 17+8):
        # print data[i],
except KeyboardInterrupt:
    ser.close()
    f.close()
    print 'BYE'
    sys.exit(1)