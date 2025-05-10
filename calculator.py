import matplotlib.pyplot as plt
import matplotlib.patches as patches

class TreePlotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.axis('off')
        self.levels = {}

    def plot_tree(self, data, x=0, y=0, dx=4, level=0):
        label = "list" if isinstance(data, list) else str(data)
        self.ax.text(x, y, label, ha='center', va='center',
                     bbox=dict(boxstyle="round", facecolor='lightblue', edgecolor='gray'))

        if isinstance(data, list):
            count = len(data)
            for i, item in enumerate(data):
                x_child = x + dx * (i - (count - 1) / 2)
                y_child = y - 1.5
                # Draw line
                self.ax.plot([x, x_child], [y - 0.2, y_child + 0.2], 'k-')
                self.plot_tree(item, x_child, y_child, dx / 2, level + 1)

def visualize_nested_list(data):
    tree = TreePlotter()
    tree.plot_tree(data)
    plt.show()

# 테스트용 리스트
nested_list = [1, [2, [3, 4], 5], 6]
visualize_nested_list(nested_list)
