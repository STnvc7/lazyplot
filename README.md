# lazyplot

Module for using matplotlib easily.

## install
```
pip install lazyplot
```

## usage
### lazy_plot
Draw graphs by entering only data.
```
from lazyplot import lazy_plot
x = np.random.rand(3, 30)
lazy_plot(x)

# Simple customization
lazy_plot(x, figure_config={"figsize"=(8,20), "colmuns"=2, "plot_type_2d"="plot"})
```

### custom plot
Draw more detailed graph by using user-specified DrawConfig
```
from lazyplot import DrawConfig, custom_plot
draw_info = DrawConfig(y=np.random.rand(2,30), title="random value", plot_type="scatter", color="blue")
custom_plot(draw_info)
```

### FigureConfig
FigreConfig can be overridden by giving a dictionary-type configuration item to the figure_config of lazy_plot and custom_plot.

- figsize (tuple[int, int])figsize of matplotlib.Figure (default= (5, 4))
- layout ("tight" | "constrained") : layout of matplotlib.Figure (default= "constrained")
- linewidth (float) : linewidth of graph (default= 2.0)
- columns (int) : number of columns in graph display.  (default= 1)
    
- plot_type_1d ("plot" | "hist" | "bar"): default plot type of 1 demensional array. (default= "plot")
- plot_type_1d ("plot" | "scatter" | "imshow" | "boxplot"): default plot type of 2 demensional array. (default= "imshow")
- plot_type_3d ("scatter"): default plot type of 3 demensional array. (default= "scatter")
    
- dpi (float) : dpi of matplotlib.Figure (default= 100)