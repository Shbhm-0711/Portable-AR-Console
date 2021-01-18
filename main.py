import serial
import time
from re import search

# set up the serial line
ser = serial.Serial('COM6', 115200)
# ser = serial.Serial('COM5', 115200)
time.sleep(2)

# Read and record the data

data =[]                       # empty list to store the data
while True:
# for i in range(5):
    y = ser.readline()         # read a byte string
    # string_n = b.decode()  # decode byte string into Unicode
    # string = string_n.rstrip() # remove \n and \r
    # flt = float(string)        # convert string to float
    # print(flt)
    # data.append(flt)           # add to the end of data list
    z = str(y)
    data.append(z)           # add to the end of data list

    print(data)


    inp = data[0]
    data.clear()

    to_find = "a"


    if search(to_find, inp):
        a = inp.index("a")
        b = inp.index("B")
        c = inp.index("c")
        d = inp.index("d")
        e = inp.index("e")
        f = inp.index("f")
        g = inp.index("g")
        h = inp.index("h")

        Ax = int(inp[a + 1:b])
        Ay = int(inp[b + 1:c])
        Az = int(inp[c + 1:d])

        Gx = int(inp[d + 1:e])
        Gy = int(inp[e + 1:f])
        Gz = int(inp[f + 1:g])

        id = int(inp[g + 1:h])

        processed = [id, Ax, Ay, Az, Gx, Gy, Gz]

        print(processed)

    else:
        print("no data")


    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()


# show the data

# for line in data:
#     print(line)






# inp = "a12204b7428c9896d-602e-399f-475g3220742541h"

