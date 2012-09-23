"""
    Do a mouseclick somewhere, move the mouse to some destination, release
    the button.  This class gives click- and release-events and also draws
    a line or a box from the click-point to the actual mouseposition
    (within the same axes) until the button is released.  Within the
    method 'self.ignore()' it is checked wether the button from eventpress
    and eventrelease are the same.
    
    """
from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def onselect(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print "(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2)
    print " The button you used were: ", eclick.button, erelease.button
    
    rect = matplotlib.patches.Rectangle((x1, y1), x2-x1, y2-y1, color='gray', alpha = .1)
    #rect = matplotlib.patches.Rectangle((x1, y1), x2-x1, y2-y1, fill=False)
    current_ax.add_patch(rect)
    print current_ax.patches
    print current_ax
    fig.canvas.draw()


def toggle_selector(event):
    print ' Key pressed.'
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print ' RectangleSelector deactivated.'
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print ' RectangleSelector activated.'
        toggle_selector.RS.set_active(True)

def mouse_move(event):
    for row in ax_sub:
        for col in row:
            if event.inaxes == col: 
                current_ax = col
                #col.plot(x,x)
    comm = '''     
    try:
        print np.where(current_ax==ax_sub)[0][0]
    except:
        print ''
        '''
    fig.canvas.draw()


def onpress(event):
    if event.key not in ('d', 'D'): return
    print event.xdata, event.ydata
    
    comm = '''
    # check if pointer is inside plot
    if event.inaxes != current_ax.patches[0].axes: return#print 'not in'
    #else: print 'contained'

    # check if pointer is inside rectangle[0]
    contains, attrd = current_ax.patches[0].contains(event)
    #if not contains: return
    #print 'event contains', current_ax.patches[0].xy
    if contains:
        current_ax.patches.remove(current_ax.patches[0])
        fig.canvas.draw()
    '''
    
    to_remove = [patch for patch in current_ax.patches if patch.contains(event)[0]]
    
    for patch in to_remove:
        current_ax.patches.remove(patch)
    
    fig.canvas.draw()




fig,ax_sub = plt.subplots(4,4)                    # make a new plotingrange
N = 100                                       # If N is large one can see
x = np.linspace(0.0, 10.0, N)                    # improvement by use blitting!
#print ax
#current_ax=ax[0]
#ax2=ax[1]
#current_ax.plot(x, +np.sin(.2*np.pi*x), 'o', lw=3.5, c='b', alpha=.7)  # plot something
#current_ax.plot(x, +np.cos(.2*np.pi*x), lw=3.5, c='r', alpha=.5)
#current_ax.plot(x, -np.sin(.2*np.pi*x), lw=3.5, c='g', alpha=.3)
#current_ax.scatter(x,+np.sin(.2*np.pi*x))
#ax2.plot(x,-np.cos(.2*np.pi*x))
ax = []
for row in ax_sub:
    for col in row:
        col.plot(x,-np.cos(.2*np.pi*x))
#for a in ax:
#    a.plot(x,-np.cos(.2*np.pi*x))
#print ax
current_ax=ax_sub[0][0]
#ax2=ax[1]
print "\n      click  -->  release"

# drawtype is 'box' or 'line' or 'none'
toggle_selector.RS = RectangleSelector(current_ax, onselect,drawtype='box', spancoords='pixels')
#toggle_selector1.RS = RectangleSelector(ax2, onselect,drawtype='box', spancoords='pixels')
plt.connect('key_press_event', toggle_selector)
#plt.connect('key_press_event', toggle_selector1)
plt.connect('key_press_event', onpress)
plt.connect('motion_notify_event', mouse_move)

plt.show()