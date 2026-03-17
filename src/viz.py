import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import numpy as np
from matplotlib.pyplot import figure, axes
from pathlib import Path

figures_path = Path("figures")
figures_path.mkdir(exist_ok=True)

# Heatmap Settings
figsize = (8, 8)
cmap = sns.color_palette("Blues", as_cmap=True)
cmap.set_bad(color="lightgrey")
label = ["BBB", "BBR", "BRB", "BRR", "RBB", "RBR", "RRB", "RRR"]

def create_heatmap(data: np.ndarray,
                   x_label: str,
                   y_label: str,
                   title: str,
                   annot_data: np.ndarray,
                   mask: np.ndarray,
                   figsize: tuple = (8, 8),
                   cmap: str = cmap) -> tuple[figure, axes]:
    '''
    Generates a heatmap for np.ndarray data.
    Returns fig, ax variables for further visualization customization.
    x_label, y_lable, title, figsize, and cmap are all preset settings to the heatmap.
    The diagonal values of the heatmap are masked with a 'lightgrey' color.
    figsize, and cmap are both preset settings to the heatmap.

    Required arguments
    data: a numpy.ndarray.
    annot_data: a numpy.ndarray.
    mask: a numpy.ndarray.
    x_label: a string.
    y_lable: a string.
    title: a string.

    Optional arguments
    annot_data: a numpy.ndarray labeling heatmap values of win(tie) probabilities
    cmap: a string.
    '''

    if not isinstance(data, np.ndarray):
        raise TypeError("data must be a numpy array")

    fig, ax = plt.subplots(figsize=figsize)
    cmap.set_bad(color="lightgrey")

    sns.heatmap(data=data,
                cmap=cmap,
                annot=annot_data,
                fmt='',
                cbar=False,
                mask=mask,
                xticklabels=label,
                yticklabels=label,
                ax=ax)

    if x_label:
        ax.set_xlabel(x_label)

    if y_label:
        ax.set_ylabel(y_label)

    if title:
        ax.set_title(title)

    plt.yticks(rotation=0)

    # Differentiation for heatmap files
    timestamp = datetime.datetime.now().strftime("%d%m%y_%H%M%S_%f")
    filename = f"heatmap_{timestamp}.png"
    fig.savefig(figures_path / filename)
    plt.show()
    plt.close()
    
    return fig, ax