# YAML mapping declaration
from wledcast.mapper import Mapping, source
mapping = Mapping.load('dev-mapping.yaml')
mapping.display(scale=2)
print(mapping)
# mapping.display('svg')
# import sys; sys.exit()

# Some source mapped to mapping
source.run(
    fps=12,
    mapping=mapping,
    # display={'scale': 0.5},
    generator=source.filter(
        sharpen=.75,
        contrast=4, # 1.75,
        saturation=1.5,
        # balance_r=0.9,
        # balance_g=1.0,
        # balance_b=0.9,
        # generator=source.growing_square(side_size=max(mapping.size))))
        # generator=source.image_zoom('/Users/damien/Downloads/rubik-rotating.gif', size=mapping.size)))
        generator=source.screen(to_size=mapping.size)))

# Growing square mapped to mapping (deprecated)
# from wledcast.mapper import test
# test.growing_square(mapping)
# # test.image_zoom(mapping, '/Users/damien/Downloads/rubik-rotating.gif')
