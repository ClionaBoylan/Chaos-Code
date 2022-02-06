import numpy as np
import matplotlib.pyplot as plt

#Initialising time increment and number
h=0.001
steps=100000

#Initialising some arrays to be of the correct size
x=np.zeros(steps)
y=np.zeros(steps)
z=np.zeros(steps)

#Defining Lorenz equations as functions 
def f1(x,y,z,p):
    return p*(y-x)

def f2(x,y,z,r):
    return -(x*z)+(r*x)-y

def f3(x,y,z,b):
    return x*y-b*z

#Setting specified initial conditions
x[0]=1
y[0]=1
z[0]=1

#While loop that performs numerical integration
i=0
while i<steps-1:
    x[i+1]=x[i]+(h/2.0)*(f1(x[i],y[i],z[i],10.0)+f1(x[i]+h*(f1(x[i],y[i],z[i],10.0)),y[i],z[i],10.0))
    y[i+1]=y[i]+(h/2.0)*(f2(x[i],y[i],z[i],28.0)+f2(x[i]+h*(f2(x[i],y[i],z[i],28.0)),y[i],z[i],28.0))
    z[i+1]=z[i]+(h/2.0)*(f3(x[i],y[i],z[i],8.0/3.0)+f3(x[i]+h*(f3(x[i],y[i],z[i],8.0/3.0)),y[i],z[i],8.0/3.0))
    i=i+1

#Creating a time array to plot variables against
time=np.arange(0,h*steps,h)

#Plotting x(t),y(t), and z(t)
fig1=plt.figure(figsize=(4,12))
ax1=fig1.add_subplot(311)
ax2=fig1.add_subplot(312)
ax3=fig1.add_subplot(313)
ax1.plot(time,x,linewidth=0.5)
ax1.set_ylabel('x(t)')
ax1.set_xlabel('t')
ax2.plot(time,y,linewidth=0.5)
ax2.set_ylabel('y(t)')
ax2.set_xlabel('t')
ax3.plot(time,z,linewidth=0.5)
ax3.set_ylabel('z(t)')
ax3.set_xlabel('t')
plt.subplots_adjust(hspace=0.4)
plt.savefig('Versus Time',dpi=300)
plt.show()

#Plotting x vs y, y vs z, and z vs x
fig2=plt.figure(figsize=(12,3.1))
ax1=fig2.add_subplot(131)
ax2=fig2.add_subplot(132)
ax3=fig2.add_subplot(133)
ax1.plot(y,x,linewidth=0.5)
ax1.set_xlabel('y')
ax1.set_ylabel('x')
ax1.axis('equal')
ax1.set_title('x vs y')
ax2.plot(z,y,linewidth=0.5)
ax2.set_xlabel('z')
ax2.set_ylabel('y')
ax2.axis('equal')
ax2.set_title('y vs z')
ax3.plot(x,z,linewidth=0.5)
ax3.set_xlabel('x')
ax3.set_ylabel('z')
ax3.axis('equal')
ax3.set_title('z vs x')
plt.subplots_adjust(wspace=0.4)
plt.savefig('Versus Each Other',dpi=300)
plt.show()

#3D plot to see Lorenz attractor
fig1=plt.figure()
ax = fig1.add_subplot(111, projection='3d')
ax.scatter(x,y,z,c=z,cmap='plasma',s=0.005,alpha=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz Attractor')
plt.savefig('Lorenz Attractor',dpi=400)
plt.show()

#Rotation to see previous graphs
fig=plt.figure(figsize=(12,3.1))
ax1=fig.add_subplot(131, projection='3d')
ax1.scatter(x,y,z,c=z,cmap='plasma',s=0.005,alpha=0.5)
ax1.set_title('Lorenz Attractor (x vs y)')
ax1.view_init(-90,180)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax2=fig.add_subplot(132, projection='3d')
ax2.scatter(x,y,z,c=z,cmap='plasma',s=0.005,alpha=0.5)
ax2.set_title('Lorenz Attractor (y vs z)')
ax2.view_init(-180,0)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax3=fig.add_subplot(133, projection='3d')
ax3.scatter(x,y,z,c=z,cmap='plasma',s=0.005,alpha=0.5)
ax3.set_title('Lorenz Attractor (z vs y)')
ax3.view_init(-180,0)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
plt.subplots_adjust(wspace=0.4)
plt.savefig('Rotations',dpi=400)
plt.show()

#Modified version of previous graphing code that produces a series of images at
#different viewing angles (COMMENTED DUE TO LONG RUNTIME)
#Used to create the first attached GIF
#gradations=360.0
#i=0
#while i<gradations:
#    fig=plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
#    ax.scatter(x,y,z,c=z,cmap='jet',s=0.01)
#    ax.set_xlabel('X')
#    ax.set_ylabel('Y')
#    ax.set_zlabel('Z')
#    ax.view_init(0, (360.0/gradations)*i)
#    plt.savefig('GIF3/{0}.png'.format(i),dpi=100)
#    print(i/gradations*100)
#    plt.close(fig)
#    i=i+1

#Modified version of previous graphing code that produces a series of images at
#different points in the creation of the graph (COMMENTED DUE TO LONG RUNTIME)
#Used to create the second attached GIF
#frames=1000
#i=0
#while i<frames:
#    ins=int((i/frames)*steps)
#    fig=plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
#    ax.scatter(x[:ins],y[:ins],z[:ins],s=0.01)
#    ax.scatter(x[ins],y[ins],z[ins],s=0.1)
#    ax.set_xlabel('X')
#    ax.set_ylabel('Y')
#    ax.set_zlabel('Z')
#    ax.set_zlim(-10,50)
#    ax.set_xlim(-20,20)
#    ax.set_ylim(-20,20)
#    plt.savefig('GIF6/{0}.png'.format(i),dpi=100)
#    print(i/frames*100)
#    plt.close(fig)
#    i=i+1
