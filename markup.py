import matplotlib.pyplot as plt
import numpy as np

# Create three vectors of 288 random values
vector1 = np.random.rand(288)
vector2 = np.random.rand(288)
vector3 = np.random.rand(288)

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the three vectors on the axis object
ax.plot(vector1)
ax.plot(vector2)
ax.plot(vector3)

# Set the title and labels for the plot
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
