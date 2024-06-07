# Programmatic mapping declaration:
from wledcast.mapper import generator, Mapping
mapping = generator.matrix(
    width = 8,
    height = 8,
    firstled = 'topleft')
mapping = Mapping(mapping)

# YAML mapping declaration
mapping = Mapping.load('dev-mapping-matrix-8x8.yaml')
print('Mapping', mapping)
mapping.display()

# PixelWriter
from wledcast.wled.pixel_writer import PixelWriter
pw = PixelWriter('wled-matrix.local')

# Growing square mapped to mapping
from wledcast.mapper import test
test.growing_square(mapping, pw)
