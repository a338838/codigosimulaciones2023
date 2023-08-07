##simulación de el sistema de segundo orden (d^2 y(t))/(dt^2 )+12  (dy(t))/dt+32y(t)=10x(t) 
##con la aproximacion de euler y(t_(n+1) )=y(t_n )+0.1 u_1 (t_n)
## y u_1 (t_(n+1) )=u_1 (t_n )+0.1 (10u(t_n )-12u_1 (t_n )-32y(t_n)

import numpy as np
import matplotlib.pyplot as mpl


def u(A,k,t):
	resp=0
	if t>=k:
		resp=A
	return resp

def ppal(tini,tfin,h,y0,yprima0):
	ts=np.arange(tini,tfin,h)
	ys=[]
	yante=y0
	u1ante=yprima0
	for t in ts:
		y=yante + h * u1ante
		u1=u1ante + h * (u(10,0,t)-12*u1ante-32*yante)
		ys.append(y)
		yante=y
		u1ante=u1
	mpl.plot(ts,ys)
	mpl.title('Respuesta de Segundo orden al escalón')
	mpl.xlabel('t')
	mpl.ylabel('Amperes')
	mpl.grid()
	mpl.show()
if __name__ == '__main__':
	ppal(0,10,0.1,0,0)