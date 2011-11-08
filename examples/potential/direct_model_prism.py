"""
Create synthetic data from a right rectangular prism model.
"""
try:
    from mayavi import mlab
except ImportError:
    from enthought.mayavi import mlab
from matplotlib import pyplot
import numpy
from fatiando import potential, gridder, vis, logger
from fatiando.mesher.prism import Prism3D, extract

log = logger.get()
log.info(logger.header())
log.info("Example of direct modelling using right rectangular prisms")

prisms = [Prism3D(-4000,-3000,-4000,-3000,0,2000,{'density':1000}),
          Prism3D(-1000,1000,-1000,1000,0,2000,{'density':-1000}),
          Prism3D(2000,4000,3000,4000,0,2000,{'density':1000})]
shape = (100,100)
xp, yp, zp = gridder.regular((-5000, 5000, -5000, 5000), shape, z=-100)
gz = potential.prism.gz(xp, yp, zp, prisms)

pyplot.axis('scaled')
pyplot.title("gz produced by prism model (mGal)")
vis.pcolor(xp, yp, gz, shape)
pyplot.colorbar()
pyplot.show()

# Avoid importing mlab twice since it's very slow
vis.mlab = mlab
p = vis.prisms3D(prisms, extract('density', prisms))
mlab.outline(p, color=(1,1,1))
mlab.show()