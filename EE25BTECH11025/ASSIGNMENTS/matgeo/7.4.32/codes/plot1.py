import numpy as np
import matplotlib.pyplot as plt
from call import get_results

ratio, focus, directrix_y, area, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, T1x, T1y, T2x, T2y, T3x, T3y = get_results()



theta = np.linspace(0, 2*np.pi, 200)
A = ([Ax, Bx, Cx, Dx, Ax, Bx])
B = ([Ay, By, Cy, Dy, Ay, By])

C = ([Ax, 0])
D = ([Ay, 1.41])
plt.plot(C, D, color='green')

C = ([Bx, 0])
D = ([By, 1.41])
plt.plot(C, D, color='green')

C = ([Cx, 0])
D = ([Cy, 1.41])
plt.plot(C, D, color='green')

C = ([Dx, 0])
D = ([Dy, 1.41])
plt.plot(C, D, color='green')

C = ([Ax, -0.5])
D = ([Ay, 0.854])
plt.plot(C, D, color='green')

C = ([Bx, -0.5])
D = ([By, 0.854])
plt.plot(C, D, color='green')

C = ([Cx, -0.5])
D = ([Cy, 0.854])
plt.plot(C, D, color='green')

C = ([Dx, -0.5])
D = ([Dy, 0.854])
plt.plot(C, D, color='green')

plt.plot(A, B, color='black')
plt.plot(0, 0, "ko")
plt.plot(0, 1.414, "ko")
plt.text(Ax+0.1, Ay+0.1, "A(1,1)", fontsize = 10, color = 'black')
plt.text(Bx+0.1, By+0.1, "B(-1,1)", fontsize = 10, color = 'black')
plt.text(Cx+0.1, Cy+0.1, "C(-1,-1)", fontsize = 10, color = 'black')
plt.text(Dx+0.1, Dy+0.1, "D(1,-1)", fontsize = 10, color = 'black')
plt.text(0,0, "(0,0)", fontsize = 10, color = 'black')
plt.text(0.1, 1.414, "Q", fontsize = 10, color = 'black')
plt.plot(-0.5, 0.854, "ko")
plt.text(-0.4, 0.854, "P", fontsize = 10, color = 'black')

plt.plot(np.cos(theta), np.sin(theta), label="Inner Circle C1")
plt.plot(np.sqrt(2)*np.cos(theta), np.sqrt(2)*np.sin(theta), label="Outer Circle C2")

plt.axis("equal")
plt.grid(True)
plt.savefig("../figs/plot1.png")
plt.show()
