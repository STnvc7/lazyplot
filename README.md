# lazyplot

Module for plotting graphs easily

## install
"""
pip install lazyplot
"""

## usage
### easy plot
```
from lazyplot import lazy_plot
x = np.random.rand(3, 30)
lazy_plot(x, out_path=None, user_config={"figsize"=(8,20), "colmuns"=2, "plot_type_2d"="plot"})
```

### custom plot
```
from lazyplot import DrawConfig, custom_plot
draw_info = DrawConfig(y=np.random.rand(2,30), plot_type="scatter")
custom_plot(draw_info)
```