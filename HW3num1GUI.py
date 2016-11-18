#This program shows how to use the Velocity Verlet method to model planetary motion
from pylab import *
from Tkinter import *
from numpy import *
import matplotlib.pyplot as plt
import numpy.fft as fourier
from numpy import *
import matplotlib.pyplot as plt


class TwoBody:
	def acceleration(self,variables,params,t):
		[x,y]=variables	
		MG = params[0]
		alpha = params[1]
		beta=params[2]
		r=sqrt(x**2+y**2) #Last night I got ^ and ** confused
		
		a = MG*(1+alpha/r**2)/(r**beta)
		
		return array([-a*x/r,-a*y/r])
	def start(self,tmmax=1,dt=.0001,r0=1,v0=1,alpha=0,beta=2):
		#Variables that we'll need
		#r0 = .38#1#0.387 #This is the initial distance, in units of AU
		#Assume that we start from theta = 0, at least for one planet
		vr0 = 0 #We start at aphelion or perihelion, so no radial velocity
		
		vt0 = v0*2*pi/sqrt(r0)#1.32*pi/sqrt(r0) #All of the velocity is initially tangential
		#alpha =.005 #0.005 #This is a parameter from General Relativity
		MG = 4*pi**2 #In units of AU^3/year^2
		params = array([MG,alpha,beta],dtype='float')

		dt = 0.04 #In units of years
		onehalfdtsquared = 0.5*dt**2 #We use this a lot so just calculate it once
		tmax = 15
		numtimes = int(tmax/dt)

		#Initialize arrays
		times = linspace(0,tmax,numtimes)
		#Position and velocity arrays
		coordinates = zeros([numtimes,2]) #Careful with the brackets for 2D arrays!
		velocities = zeros([numtimes,2])
		coordinates[0] = array([r0,0])
		velocities[0] = array([vr0,vt0])
		aold = self.acceleration(coordinates[0],params,0)

		#The main loop
		for t in range(1,numtimes):
			coordinates[t] = coordinates[t-1]+velocities[t-1]*dt+onehalfdtsquared*aold
			anew = self.acceleration(coordinates[t],params,times[t-1])
			velocities[t] = velocities[t-1]+0.5*(anew+aold)*dt
			aold = anew #Why calculate two accelerations per iteration when I can recycle?



		#If we want to monitor precession, we need to monitor r and  theta
		r = zeros(numtimes)
		theta = zeros(numtimes)
		for t in range(0,numtimes):
			r[t] = sqrt(dot(coordinates[t],coordinates[t])) #Square root of r dot r
			theta[t] = arctan(coordinates[t,1]/coordinates[t,0]) #Arctangent of y over x

		#Time to show results
		plt.figure()
		plt.subplot(311)
		plt.plot(coordinates[:,0],coordinates[:,1],label='Orbit')
		plt.xlabel('X coordinate')
		plt.ylabel('Y coordinate')
		plt.legend(loc = 'upper right')
		plt.subplot(312)
		plt.plot(times,r,label='Distance from sun')
		plt.xlabel('Time')
		plt.ylabel('Distance from sun')
		plt.legend(loc = 'upper right')
		plt.subplot(313)
		plt.plot(times,theta*180/3.14,label=r'$\theta$')
		plt.xlabel('Time')
		plt.ylabel('Angle')
		plt.legend(loc = 'upper right')
		plt.show()
		return
###################Display Window############################################
class Gui:	
	def prob1(self):
		self.window_prob1=Toplevel()#the new GUI window for prob#1 HW 3
		self.window_prob1.protocol("WM_DELETE_WINDOW",self.close)
		Frame(self.window_prob1,width=600, height=0,takefocus=True).pack()
		
		
		Label(self.window_prob1,text="Max. Time").pack()
		self.maxTimeScale=Spinbox(self.window_prob1, from_=1, to=10**3)
		self.maxTimeScale.pack()
		
		
		Label(self.window_prob1,text="Delta T (step time)").pack()
		self.deltaT=Spinbox(self.window_prob1,from_=.001,to=10,increment=.001)
		self.deltaT.pack()
		
		
		Label(self.window_prob1,text="Initial Distance (in AU)").pack()
		self.distanceScale=Spinbox(self.window_prob1, from_=0.5, to=360)
		self.distanceScale.pack()
		
		Label(self.window_prob1,text="Initial Velocity (in AU/T)").pack()
		self.velocityScale=Spinbox(self.window_prob1, from_=0, to=360)
		self.velocityScale.pack()
		
		Label(self.window_prob1,text="Initial Alpha").pack()
		self.AlphaScale=Spinbox(self.window_prob1, from_=0, to=2, increment=0.1)
		self.AlphaScale.pack()
		
		Label(self.window_prob1,text="Initial Beta (in AU)").pack()
		self.betaScale=Spinbox(self.window_prob1, from_=0, to=2, increment=0.1)
		self.betaScale.pack()
		
		Label(self.window_prob1,relief=RAISED,text="Press 'Graph' to graph using both Velocity Verlet").pack()
		self.graph=Button(self.window_prob1,text="Graph",command=self.plot)
		self.graph.pack()
		self.window_prob1.focus_set()#need this to make modal window
		self.window_prob1.grab_set()
		self.window_prob1.transient(self.window)
		self.window_prob1.wait_window(self.window_prob1)#end modal
		return
	def plot(self):
		tBody = TwoBody()
		
		return tBody.start(float(self.maxTimeScale.get()),float(self.deltaT.get()),float(self.distanceScale.get()),float(self.velocityScale.get()),float(self.AlphaScale.get()),float(self.betaScale.get()))
		
	def __init__(self,window):#MAIN WINDOW
		self.window = window
		window.title("Programming Assignment #3")
		window.geometry("500x100")
		window.eval('tk::PlaceWindow %s center' % window.winfo_pathname(window.winfo_id()))
		label = Label( window, text="Press one of the following options.", relief=RAISED ).pack()
		Button(window,text="Problem 3.1",command=self.prob1).pack()
	def on_closing(self):
		print("Program terminated.")
		close('all')#close all python graphs
		root.destroy()	
	def close(self):
			close('all')
			self.window_prob1.grab_release()
			self.window_prob1.withdraw()
	def reGraph(self):
		close('all')
root = Tk()
window = Gui(root)
root.protocol("WM_DELETE_WINDOW",window.on_closing)#close all graphs
root.mainloop()
