import matplotlib.pyplot as plt
import numpy as np
import pickle
import tkinter as tk
import math
import pandas as pd
import datetime
import pickle
import numpy as np
import matplotlib.pyplot as plt


INDEX=0

# ~ data = pickle.load(open('speed.pkl','rb'))

data=None

def load_state():
    global data, INDEX
    try:
        with open('speed-processed.pkl', 'rb') as f:
            data = pickle.load(f)
            
    except FileNotFoundError:
        INDEX = 0
        data = pickle.load(open('speed.pkl','rb'))
        
def save_state():
    global data
    # ~ state = {'index': INDEX, 'good': good}
    with open('speed-processed.pkl', 'wb') as f:
        pickle.dump(data, f)

load_state()

IDS = sorted(data.keys())
# ~ print(IDS[:10])

for i in range(len(IDS)):
    if data[IDS[i]]['startM']!=-1:
        print(i, data[IDS[i]]['startM'], data[IDS[i]]['endM'])
        INDEX+=1


fig, ax = plt.subplots(figsize=(12,4))

clicks = []
click_counter = 0

from sklearn.preprocessing import MinMaxScaler

def standard_scale(input_vector):
    """
    This function performs standard scaling between 0 and 1 of an input vector.
    
    Args:
    input_vector (list or numpy array): The input vector to be scaled.
    
    Returns:
    numpy array: The scaled input vector.
    """
    
    # Create a MinMaxScaler object
    scaler = MinMaxScaler(feature_range=(0, 1))

    # Reshape the input vector to a 2D array with one column
    input_vector_reshaped = [[x] for x in input_vector]

    # Use the scaler to perform the standard scaling
    scaled_input_vector = scaler.fit_transform(input_vector_reshaped)

    # Return the scaled input vector
    return scaled_input_vector.flatten()
    
    
    
def plot_data(ax,data):
    # ~ print(data.keys())
    # ~ plt.figure(figsize=(11,3))
    ax.clear()
    ax.set_title(data['ID']+' '+str(INDEX))
    ax.axvline(x=data['start5'],c='r',lw=3,ls='--',label='Disruption Start')
    ax.axvline(x=data['end5'],c='b',lw=3,ls='--',label='Disruption End')

    ax.plot(data['day'],label='Day',lw=3)
    ax.plot(data['profile'],label='Profile',lw=3)
    ax.plot((data['day'].max()/2)* standard_scale(data['chebSQ']),label='Segmentation',ls='--',lw=2)
    # ~ ax.plot((data['day'].max()/2)* standard_scale(data['cheb']),label='Chebyshev',ls='--')
    ax.plot((data['day'].max()/2)* standard_scale(data['WD']),label='WD',ls='--')
    ax.set_xlim(0,288)
    ax.grid()
    ax.legend()
    ax.set_xticks(np.arange(0,288,12),np.arange(0,288,12)*5//60)
    ax.set_xlabel('Hours')
    ax.set_ylabel('(Speed [km/h]) or (Scaled Norm Cheb/WD / 2)')
    # ~ plt.tight_layout(pad=0)

def redraw():
	row = data[IDS[INDEX]]
	
	
	plot_data(ax,row)

	
	clicks = []
	click_counter = 0
	fig.canvas.draw()
        
        
clicks = []
click_counter = 0

# Function to handle mouse click events
def onclick(event):
    global clicks
    global click_counter
    global INDEX
    
    # Check if right-click occurred
    if event.button == 3:
        # Redraw the plot
        data[IDS[INDEX]]['startM'] = -2
        data[IDS[INDEX]]['endM'] = -2
        INDEX+=1
        redraw()
        return
    
    # Record the click position and increment the counter
    clicks.append(event.xdata)
    click_counter += 1
    
    # Draw a vertical line where the click occurred
    ax.axvline(event.xdata, color='r')
    fig.canvas.draw()
    
    # If the second click occurred, record the click positions into an array
    if click_counter == 3:
        print('Click positions:', np.array(clicks[:2]).astype(int))
        
        data[IDS[INDEX]]['startM'] = np.array(clicks[:2]).astype(int)[0]
        data[IDS[INDEX]]['endM'] = np.array(clicks[:2]).astype(int)[1]
        
        clicks = []
        click_counter = 0
        INDEX+=1
        redraw()

# Connect the mouse click event to the plot
cid = fig.canvas.mpl_connect('button_press_event', onclick)



# ~ plot_vectors()
redraw()

plt.show()


save_state()



import sys
sys.exit(0)

# Create three vectors of 288 random values
vector1 = np.random.rand(288) #read daily speed
vector2 = np.random.rand(288) #read speed profile
vector3 = np.random.rand(288) #read WD result
	#read start and end points

# Create a figure and axis object
fig, ax = plt.subplots()
ax.clear()
ax.plot(vector1)
ax.plot(vector2)
ax.plot(vector3)
ax.set_title('Three Vectors')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
        
# Initialize variables to store click positions and counter
clicks = []
click_counter = 0

# Function to handle mouse click events
def onclick(event):
    global clicks
    global click_counter
    
    # Check if right-click occurred
    if event.button == 3:
        # Redraw the plot
        ax.clear()
        ax.plot(vector1)
        ax.plot(vector2)
        ax.plot(vector3)
        ax.set_title('Three Vectors')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        clicks = []
        click_counter = 0
        fig.canvas.draw()
        return
    
    # Record the click position and increment the counter
    clicks.append(event.xdata)
    click_counter += 1
    
    # Draw a vertical line where the click occurred
    ax.axvline(event.xdata, color='r')
    fig.canvas.draw()
    
    # If the second click occurred, record the click positions into an array
    if click_counter == 2:
        print('Click positions:', clicks)
        clicks = []
        click_counter = 0

# Connect the mouse click event to the plot
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Show the plot
plt.show()

print('END')
