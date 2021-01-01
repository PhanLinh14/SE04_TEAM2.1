import ezdxf
from ezdxf.entities.spline import Spline
# Create a new DXF document.
doc = ezdxf.new(dxfversion='R2010')
# paperspace layout or block definition).  
fit_points = [(0, 0, 0), (750, 500, 0), (1750, 500, 0), (2250, 1250, 0)]
msp = doc.modelspace()
spline = msp.add_spline(fit_points)
doc.saveas('demo_spline.dxf')