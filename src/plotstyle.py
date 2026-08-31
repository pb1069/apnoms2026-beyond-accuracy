"""Shared dark chart theme for all demo figures.

Palette: categorical slots 1-3 of a CVD-validated dark set (adjacent-pair
Delta-E and contrast checks pass on the card surface). Text wears text tokens,
never series colors.
"""
import matplotlib

SURFACE = "#1a2233"
INK = "#e8edf6"
DIM = "#8fa0bb"
GRID = "#2a3450"
CAT = ["#3987e5", "#d95926", "#199e70"]     # blue / orange / aqua (fixed order)


def apply():
    matplotlib.rcParams.update({
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "text.color": INK, "axes.labelcolor": DIM,
        "xtick.color": DIM, "ytick.color": DIM,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
        "grid.alpha": 0.7,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.spines.left": False, "axes.spines.bottom": False,
        "xtick.major.size": 0, "ytick.major.size": 0,
        "font.family": "Segoe UI", "font.size": 11,
        "axes.titlesize": 12.5, "axes.titlecolor": INK,
        "axes.titlelocation": "left", "axes.titlepad": 12,
        "legend.frameon": False, "legend.fontsize": 10,
        "lines.linewidth": 2.2, "lines.markersize": 6.5,
        "figure.dpi": 150,
    })
