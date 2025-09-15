import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import os

f = open("C:\\Users\\12457\\OneDrive\\Рабочий стол\\KursachPart1\\KursachPart1\\output.txt",'r')
try:
    lines = f.readlines()

    t_tmp = []
    Ca_tmp = []
    t = []
    Ca = []

    for line in lines:
        if line != "c\n":
            data = line.split(';')
            Ca_tmp.append(float(data[0]))
            t_tmp.append(float(data[1]))
        else:
            if (len(t_tmp) != 0 and len(Ca_tmp) != 0):
                t.append(list(t_tmp))
                Ca.append(list(Ca_tmp))

                t_tmp = []
                Ca_tmp = []

    Ca.append(Ca_tmp)
    t.append(t_tmp)

    for i in range(len(Ca[0])):
        if Ca[0][i] - Ca[1][i] != 0:
            print("jgjg")

    x = np.array(t[0])
    y = np.array(Ca[0])

    plt.plot(x, y, color='g')

    x2 = np.array(t[1])
    y2 = np.array(Ca[1])

    plt.plot(x2, y2, color='r')

    plt.show()
finally:
    f.close()
#f = open("C:\\Users\\12457\\OneDrive\\Рабочий стол\\KursachPart1\\KursachPart1\\graph.txt",'r')
#caMax = open("C:\\Users\\12457\\OneDrive\\Рабочий стол\\KursachPart1\\KursachPart1\\CaMax.txt",'r')
#caMin = open("C:\\Users\\12457\\OneDrive\\Рабочий стол\\KursachPart1\\KursachPart1\\CaMin.txt",'r')
# try:
   #CaMax = []
   #CaMin=[]
   #v4CaMin = []
   #v4CaMax = []

   # lines = caMax
   # for line in lines:
   #     data = line.split(';')
   #     CaMax.append(float(data[0]))
   #     v4CaMax.append(float(data[1]))

   # lines = caMin
   # for line in lines:
   #     data = line.split(';')
   #     CaMin.append(float(data[0]))
   #     v4CaMin.append(float(data[1]))
   # x1 = np.array(v4CaMax)
   # y1 = np.array(CaMax)
   # x2 = np.array(v4CaMin)
   # y2 = np.array(CaMin)
   # plt.plot(x1,y1,x2,y2)
   # plt.xlabel("v4")
   # plt.ylabel("[Ca^2+],muM")
   # plt.show()

# finally:
#    caMax.close()
#    caMin.close()

# try:
#     CaMax = []
#     CaMaxX = []
#
#     CaMin = []
#     CaMinX = []
#
#     fx = []
#     fy = []
#
#     lines = caMax
#     for line in lines:
#         data = line.split(';')
#         CaMaxX.append(float(data[0]))
#         CaMax.append(float(data[1]))
#
#     lines = caMin
#     for line in lines:
#         data = line.split(';')
#         CaMinX.append(float(data[0]))
#         CaMin.append(float(data[1]))
#
#     lines = f
#     for line in lines:
#         data = line.split(';')
#         fx.append(float(data[0]))
#         fy.append(float(data[1]))
#
#     x1 = np.array(CaMaxX)
#     y1 = np.array(CaMax)
#
#     x2 = np.array(CaMinX)
#     y2 = np.array(CaMin)
#
#     x3 = np.array(fx)
#     y3 = np.array(fy)
#
#     plt.plot(x3,y3)
#     plt.scatter(x2, y2,c="red")
#     plt.scatter(x1, y1, c="green")
#     plt.xlabel("t")
#     plt.ylabel("[Ca^2+],muM")
#     plt.show()
# finally:
#     caMax.close()
#     caMin.close()
#     f.close()