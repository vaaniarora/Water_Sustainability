"""Shared matplotlib style for the paper figures.

ACM two-column (acmart sigconf): column width ~3.33 in, full text width ~7.0 in.
Figures are drawn at their printed size so font sizes are the real printed sizes.
Colour meaning is fixed across figures: blue = AI accelerators/systems, orange = general-purpose CPUs / HPC.
"""
import matplotlib as mpl

COL_W, TEXT_W = 3.33, 7.0

# Reference categorical palette slots 1-2 (validated colour-blind safe as a pair); neutral grey for context
C_AI, C_GP, C_NEUTRAL = '#2a78d6', '#eb6834', '#8a8984'
TEXT, TEXT_2, GRID = '#0b0b0b', '#52514e', '#e4e3df'


def apply():
    mpl.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'font.size': 7, 'axes.labelsize': 7, 'xtick.labelsize': 6.5, 'ytick.labelsize': 6.5,
        'legend.fontsize': 6.5,
        # black outline on all four sides; black axis labels and tick labels
        'axes.edgecolor': 'black', 'axes.linewidth': 0.6, 'axes.labelcolor': 'black',
        'xtick.color': 'black', 'ytick.color': 'black', 'xtick.labelcolor': 'black', 'ytick.labelcolor': 'black',
        'axes.spines.top': True, 'axes.spines.right': True, 'axes.spines.left': True, 'axes.spines.bottom': True,
        'xtick.major.size': 2.5, 'ytick.major.size': 2.5, 'xtick.major.width': 0.6, 'ytick.major.width': 0.6,
        'xtick.direction': 'out', 'ytick.direction': 'out',
        'axes.grid': True, 'axes.grid.axis': 'y', 'grid.color': GRID, 'grid.linewidth': 0.5,
        'axes.axisbelow': True,
        'pdf.fonttype': 42, 'ps.fonttype': 42,  # embed TrueType fonts (ACM/PDF eXpress requirement)
        'savefig.bbox': 'tight', 'savefig.pad_inches': 0.02, 'figure.dpi': 150,
    })


def panel_label(ax, text):
    """'(a) Title' at the top-left of a panel."""
    ax.text(0, 1.03, text, transform=ax.transAxes, fontsize=7.5, fontweight='bold', color=TEXT,
            va='bottom', ha='left')
