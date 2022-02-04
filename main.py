from re import U
import numpy as np
import matplotlib.pyplot as plt



rng = 50
d_t = 10**-4
vol = int(rng/d_t)

A = 0.1
B = 2.
C = 0.2
D = 1.5
X0 = 0

T = np.zeros(vol)
U = np.zeros(vol)
X = np.zeros(vol)
X[0] = X0
Y = np.zeros(vol)

for i in range(vol):
    T[i] = i*d_t
 
for t in range(0, vol):
    U[t] = np.sin(T[t])
    
    
for t in range(0, vol-1):
    X[t+1] = X[t] + (A*X[t]+B*U[t])*d_t
    Y[t+1] = C*X[t] + D*U[t]
    

# plt.plot(T, U,'ro')
# plt.axis([0,rng,-1,1])
# plt.show()    

height = 10

plt.plot(T, U,'r,', label = '입력')
plt.plot(T, X,'g,', label = 'X')
plt.plot(T, Y,'b,', label = '출력')

plt.axis([0,rng,-2,height])
plt.show()  

