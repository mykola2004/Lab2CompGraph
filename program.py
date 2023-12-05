import pandas as pd
import matplotlib.pyplot as plt

def plot_points_from_file(file_path):
    data = pd.read_csv(file_path, delim_whitespace=True, header=None, names=['x', 'y'])

    plt.figure(figsize=(960/96, 540/96), dpi=96)
    plt.scatter(data['x'], data['y'])

    plt.xlim(min(data['x']), max(data['x']))
    plt.ylim(min(data['y']), max(data['y']))
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Points Visualization')

    plt.savefig("output.png")
    plt.show()  

plot_points_from_file("/Users/mzcola/Documents/Lab2ASD/DS8.txt")

