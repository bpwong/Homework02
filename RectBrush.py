'''
   RectBrush.py plots the Iris Flower data and allows a user to brush
    over the data.  The brush functionality is halfway complete, as the
    data selection process has not been finished -- only rectangles can
    be drawn and cleared if 'd' or 'D' is pressed while mouse-overed.
    
    To run in bash, enter $python RectBrush.py.
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


matplotlib.rc('xtick', labelsize=7) 
matplotlib.rc('ytick', labelsize=7) 

# Read in the data
dt = [('s_len',np.float32),('s_wid',np.float32),('p_len',np.float32),('p_wid',np.float32),('spec','S20')]
flowers = np.loadtxt('txt/iris_data.txt',dt,skiprows=1)

# Set the color code
colors = ['r' if f == 'setosa' else 'g' if f == 'versicolor' else 'b' for f in flowers['spec']]

# Plot Data and Label the Plots
s = ['s_len', 's_wid', 'p_len', 'p_wid']
label = ['Sepal Length','Sepal Width','Petal Length','Petal Width']
fig, axsub = plt.subplots(4,4)
for i in range(0,4):
    for j in range(0,4):
        axsub[i][j].scatter(flowers[s[j]],flowers[s[i]],c=colors)
        if j==0:
            axsub[i][j].set_ylabel(label[i])
        if i==3: 
            axsub[i][j].set_xlabel(label[j])



class RectBrush:
    
    def __init__(self):
        self.x0, self.y0 = 0, 0
        self.xlast, self.ylast = 0, 0
        self.active_ax = axsub[0][0]
        self.click = False
        self.gray = False
    
    def onclick(self,event):
        '''
            This Event detects when the mouse is clicked.  It resets 
            position data and sets self.click = True.
        '''
        #print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
        #    event.button, event.x, event.y, event.xdata, event.ydata)
        self.x0, self.y0 = event.xdata, event.ydata
        self.xlast, self.ylast = event.xdata, event.ydata
        self.click = True
    
    def onrelease(self,event):
        '''
            This Event detects when the mouse is unclicked.  It will 
            add the rectangle if conditions are met.
        '''

        #print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
        #    event.button, event.x, event.y, event.xdata, event.ydata)
        
        # An exception is thrown if the button is released outside of any axes
        try:
            # If the button was pressed only while in the same axis, add the rectangle patch
            if self.click and (self.x0!=self.xlast or self.y0!=self.ylast):
                rect = matplotlib.patches.Rectangle((self.x0,self.y0), self.xlast-self.x0, self.ylast-self.y0, color='red',alpha=.15)
                self.active_ax.add_patch(rect)
                plt.show()
                self.click = False
        except:
            return
    
    
    def mouse_move(self,event):
        '''
            This Event follows the mouse.  It sets the active axis to the 
            axis where the mouse was first clicked.  If the active axis
            changes while the mouse is clicked, the rectange will not be 
            generated.
        '''
        #print event.inaxes
        prev_ax = self.active_ax
        
        # Find the Active Axis
        for row in axsub:
            for col in row:
                if event.inaxes == col: 
                    self.active_ax = col
        
        # Save the Last (x,y) coordinate
        if self.click:
            self.xlast, self.ylast = event.xdata, event.ydata
            if prev_ax != self.active_ax:
                # Turn off "mouse down" state if mouse changes Axes
                self.click = False
    
        #fig.canvas.draw()
    
    def onpress(self,event):
        '''
            This Event detects if 'd' or 'D' is pressed while the mouse is
            over a rectangle(s).  If so, remove the rectangle(s) from the
            current axis.
        '''
        if event.key in ('a','A'):
            self.updateaxes()
        elif event.key not in ('d', 'D'): return
        #print event.xdata, event.ydata
        
        to_remove = [patch for patch in self.active_ax.patches if patch.contains(event)[0]]
        for patch in to_remove:
            self.active_ax.patches.remove(patch)
        
        fig.canvas.draw()

    def updateaxes(self):
        # Set the color code
        
        if not self.gray:
            colors = ['gray' if f == 'setosa' else 'y' if f == 'versicolor' else 'm' for f in flowers['spec']]
            self.gray = not self.gray
        else:
            colors = ['r' if f == 'setosa' else 'g' if f == 'versicolor' else 'b' for f in flowers['spec']]
            self.gray = not self.gray
        
        # Update Data
        s = ['s_len', 's_wid', 'p_len', 'p_wid']
        
        for i in range(0,4):
            for j in range(0,4):
                axsub[i][j].scatter(flowers[s[j]],flowers[s[i]],c=colors)
            
            

brush = RectBrush()        

cid = fig.canvas.mpl_connect('button_press_event', brush.onclick)
cid = fig.canvas.mpl_connect('button_release_event', brush.onrelease)
cid = fig.canvas.mpl_connect('motion_notify_event', brush.mouse_move)
cid = fig.canvas.mpl_connect('key_press_event', brush.onpress)
plt.suptitle('Iris Flower Data')
plt.show()