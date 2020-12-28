import serial
import numpy as np
import pandas as pd
x = np.array([])
c = np.array([])
data = np.empty((0,2), int)
ser = serial.Serial("/dev/cu.wchusbserial14230", 9600, timeout=1)

cnt = 0
val = ser.readline()
while cnt < 1000:
    val = ser.readline()
    val = val.strip().decode('utf-8')
    x = np.append(x, val)
    c = np.append(c, cnt)
    data = np.append(data,np.array([[val,cnt]]), axis=0)
    cnt += 1
    print(val, cnt)

print(data)
# data = np.c_[x, c]
# np.savetxt('out.csv', data, delimiter=',')
df=pd.DataFrame(data, columns=['data','count'])
df.to_csv('fast.csv', index=False)
