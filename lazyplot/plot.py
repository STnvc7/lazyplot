import math
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np

from lazyplot.config import PlotConfig, DrawInfo

GLOBAL_CONFIG = PlotConfig()

#=================================================================================
def custom_plot(draw_info: list[DrawInfo], user_config: dict | None):
    cfg = GLOBAL_CONFIG
    cfg.override(user_config)
    
    if isinstance(draw_info, list) == False:
        raise ValueError("Invalid input data. Must be list[] of DrawInfo.")
    
    fig = plt.figure(figsize=cfg.figsize, linewidth=cfg.linewidth, layout=cfg.layout)
    ax_cols = cfg.columns
    ax_rows = math.ceil(len(draw_info) /cfg.columns)


#=================================================================================
def lazy_plot(input_data: np.ndarray | list[np.ndarray], user_config: dict | None = None) :
    """
    """
    cfg = GLOBAL_CONFIG
    cfg.override(user_config)
    
    if isinstance(input_data, list) is False:
        input_data = [input_data]
    
    fig = plt.figure(figsize=cfg.figsize, linewidth=cfg.linewidth, layout=cfg.layout)
    ax_cols = cfg.columns
    ax_rows = math.ceil(len(input_data) /cfg.columns)
    
    for i, data in enumerate(input_data, 1):
        _title = f'data {i}'
        _ax = fig.add_subplot(ax_rows, ax_cols, i)
        _draw_info = create_draw_info(data, _title, cfg)
        
        plot_ax(_ax, _draw_info)
        
    return fig
        
#====================================================================================
def create_draw_info(data: np.ndarray, title: str, cfg: PlotConfig):
    
    if data.ndim == 1:
        plot_type = cfg.plot_type_1d
    elif data.ndim == 2:
        plot_type = cfg.plot_type_2d
    elif data.ndim == 3:
        plot_type = cfg.plot_type_3d
    else:
        raise ValueError("Invalid data dimension. Data is limited to 3 dimensions or less")
    
    draw_info = DrawInfo(y=data, plot_type=plot_type, title=title, linewidth=cfg.linewidth)
    
    return draw_info
    


def plot_ax(ax: Axes, info: DrawInfo):
    
    match info.plot_type:
        #-------------------------------------------------------------------------------
        case "plot":
            if info.y.ndim == 1:
                info.y = np.expand_dims(info.y, axis=0)
            
            for i, y in enumerate(info.y):
                _color = info.color[i % len(info.color)]
                _linestyle = info.linestyle[(i // len(info.linestyle)) % len(info.linestyle)]
                _t = np.arange(len(y)) if info.t is None else info.t
                _label = f"graph {i+1}" if info.label is None else info.label[i]
                ax.plot(_t, y, label=_label, color=_color, alpha=info.alpha,
                        linewidth=info.linewidth, linestyle=_linestyle)
            
        case "hist":
            pass
        case "bar":
            pass
        case "boxplot":
            pass
        case "scatter":
            pass
        case "imshow":
            pass
        case _:
            pass
        
    if info.title:
        ax.set_title(info.title)
    ax.set_xlabel(info.x_label)
    ax.set_ylabel(info.y_label)
    ax.set_xlim(info.x_lim)
    ax.set_ylim(info.y_lim)
    ax.set_aspect(info.aspect)
    
    if info.invert_xaxis:
        ax.invert_xaxis()
    if info.invert_yaxis:
        ax.invert_yaxis()
        
    ax.legend()
    
#=======================================================================

if __name__ == "__main__":
    
    data = np.random.rand(30)