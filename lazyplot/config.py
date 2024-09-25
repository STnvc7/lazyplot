from dataclasses import dataclass, field
from typing import Literal, Optional
import numpy as np

FIGURE_LAYOUT = Literal["tight", "constrained"]

PLOT_TYPE_1D = Literal["plot", "hist", "bar"]
PLOT_TYPE_2D = Literal["plot", "scatter", "imshow", "boxplot"]
PLOT_TYPE_3D = Literal["scatter"]

COLOR = Literal['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
MARKER_STYLE = Literal[',', '.', 'o', 'v', '^', '<', '>', 's', 'p', '*', 'D', 'd']
LINE_STYLE = Literal['-', '--', '-.', ':']

#=========================================================================
@dataclass
class PlotConfig:
    figsize: tuple[int, int] = (8,8)
    layout: FIGURE_LAYOUT = "constrained"
    linewidth : float = 2.0
    columns: int = 1
    
    plot_type_1d: PLOT_TYPE_1D = "plot"
    plot_type_2d: PLOT_TYPE_2D = "imshow"
    plot_type_3d: PLOT_TYPE_3D = "scatter"
    
    dpi: float = 100
    
    # validate after initialize--------------------------------
    def __post_init__(self):
        self.validate()
    
    # validate property----------------------------------------
    def validate(self):
        if self.layout not in ["tight", "constrained"]:
            raise ValueError(f"Invalid figure layout: {self.layout}. Must be 'tight' or 'constrained'.")
        if self.columns <= 0:
            raise ValueError(f"Invalid columns: {self.columns}. Must be greater than 0")
    
    # set value by string key ---------------------------------
    def set_by_key(self, key: str, value: any):
        setattr(self, key, value)
        return
        
    # override config------------------------------------------
    def override(self, new_values: dict | None):
        
        if new_values == None:
            return
        for key, value in new_values.items():
            self.set_by_key(key, value)
            
        self.validate()
        return

#======================================================================
@dataclass
class DrawInfo:
    
    y : np.ndarray  # require
    plot_type: PLOT_TYPE_1D | PLOT_TYPE_2D | PLOT_TYPE_3D   #require    
    title: str | None = None    #require
    
    t : np.ndarray | None = None  
    label: list[str] | None = None
    
    x_label: str = "x" 
    y_label: str = "y"
    x_lim: tuple[float|None, float|None] = (None, None)
    y_lim: tuple[float|None, float|None] = (None, None)
    
    color: list[COLOR | tuple[int, int, int]] = field(
        default_factory=lambda: ['royalblue', 'olivedrab', 'firebrick', 'teal', 'slateblue', 'goldenrod', 'dimgray']
    )
    alpha: float = 1
    line_style: list[LINE_STYLE] = field(default_factory=lambda: ['-', '--', '-.', ':'])
    marker_style: list[MARKER_STYLE] = field(default_factory=lambda: ['o', ',', '.', 'v', '^', '<', '>', 's', 'p', '*', 'D', 'd'])
    linewidth: float = 2.0
    
    aspect: float | Literal["auto"] = "auto"
    invert_xaxis: bool = False
    invert_yaxis: bool = False
    
    def __post_init__(self):
        if self.t is not None:
            if self.t.shape != self.y.shape:
                raise ValueError(f"Invalid data. x and y must be same shape")
            
        if self.label is not None:
            if self.y.shape[0] != len(self.label):
                raise ValueError("label must have same length as y")
        
        if isinstance(self.color, list) is False:
            self.color = [self.color]
            
        if isinstance(self.line_style, list) is False:
            self.line_style = [self.line_style]
            
        if isinstance(self.marker_style, list) is False:
            self.marker_style = [self.marker_style]
            