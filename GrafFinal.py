import os
import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("explicito_001.dat")
x=datos[:,0]
y=datos[:,1]
x1=[]
y1=[]
for i in range(len(x)):
    if (x[i]<=(4*np.pi)):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(figsize=(10,10))
plt.plot(x1,y1)
plt.xlabel('T')
plt.ylabel('Y')
plt.legend()
plt.savefig("explicito_001.png") 

datos = np.loadtxt("explicito_01.dat")
x=datos[:,0]
y=datos[:,1]
x1=[]
y1=[]
for i in range(len(x)):
    if (x[i]<=(4*np.pi)):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(figsize=(10,10))
plt.plot(x1,y1)
plt.xlabel('T')
plt.ylabel('Y')
plt.legend()
plt.savefig("explicito_01.png") 

datos = np.loadtxt("explicito_1.dat")
x=datos[:,0]
y=datos[:,1]
x1=[]
y1=[]
for i in range(len(x)):
    if (x[i]<=(4*np.pi)):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(figsize=(10,10))
plt.plot(x1,y1)
plt.xlabel('T')
plt.ylabel('Y')
plt.legend()
plt.savefig("explicito_1.png") 

datos = np.loadtxt("runge_001.dat")
x=datos[:,0]
y=datos[:,1]
x1=[]
y1=[]
for i in range(len(x)):
    if (x[i]<=(4*np.pi)):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(figsize=(10,10))
plt.plot(x1,y1)
plt.xlabel('T')
plt.ylabel('Y')
plt.legend()
plt.savefig("runge_001.png") 

datos = np.loadtxt("runge_01.dat")
x=datos[:,0]
y=datos[:,1]
x1=[]
y1=[]
for i in range(len(x)):
    if (x[i]<=(4*np.pi)):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(figsize=(10,10))
plt.plot(x1,y1)
plt.xlabel('T')
plt.ylabel('Y')
plt.legend()
plt.savefig("runge_01.png") 

datos = np.loadtxt("runge_1.dat")
x=datos[:,0]
y=datos[:,1]
x1=[]
y1=[]
for i in range(len(x)):
    if (x[i]<=(4*np.pi)):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(figsize=(10,10))
plt.plot(x1,y1)
plt.xlabel('T')
plt.ylabel('Y')
plt.legend()
plt.savefig("runge_1.png")

datos = np.loadtxt("rana_001.dat")
x=datos[:,0]
y=datos[:,1]
x1=[]
y1=[]
for i in range(len(x)):
    if (x[i]<=(4*np.pi)):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(figsize=(10,10))
plt.plot(x1,y1)
plt.xlabel('T')
plt.ylabel('Y')
plt.legend()
plt.savefig("rana_001.png") 

datos = np.loadtxt("rana_01.dat")
x=datos[:,0]
y=datos[:,1]
x1=[]
y1=[]
for i in range(len(x)):
    if (x[i]<=(4*np.pi)):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(figsize=(10,10))
plt.plot(x1,y1)
plt.xlabel('T')
plt.ylabel('Y')
plt.legend()
plt.savefig("rana_01.png") 

datos = np.loadtxt("rana_1.dat")
x=datos[:,0]
y=datos[:,1]
x1=[]
y1=[]
for i in range(len(x)):
    if (x[i]<=(4*np.pi)):
        x1.append(x[i])
        y1.append(y[i])

plt.figure(figsize=(10,10))
plt.plot(x1,y1)
plt.xlabel('T')
plt.ylabel('Y')
plt.legend()
plt.savefig("rana_1.png") 