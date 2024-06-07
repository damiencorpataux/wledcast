from wledcast.wled.pixel_writer import PixelWriter
import numpy as np
import time
import sys

pw = PixelWriter('ring.local')

from wledcast.mapper import LEDMapper, generator
mapping = generator.matrix(width=0, height=0)
for (l, d) in ((60, 16.6), (48, 14.8), (40, 12.6), (32, 10.2), (24, 8.6), (16, 6.6), (12, 4.6), (8, 2.6), (1, 0)):
    mapping += generator.ring(
        length = l,
        diameter = d,
        angle = -90)
mapping = generator.translate(mapping, x=16.6/2, y=16.6/2)
print('Mapping', mapping)
led_mapper = LEDMapper(mapping)
print('Length', len(led_mapper.mapping))
print('Bbox', led_mapper.get_bbox())
print('Size', led_mapper.get_size())
print(led_mapper.render_ascii())
# led_mapper.display_svg(scale=1); import sys; sys.exit(0)

while True:
    for j in range(3):
        color = [255, 255, 255]
        color[j] = 0
        for i in range(0, 18):
            start = time.time()
            array_size = (i, i, 3)
            # print(i, array_size)
            rgb_array = np.full(array_size, color, dtype=np.uint8)
            rgb_array = led_mapper.map_pixels(rgb_array)
            print(led_mapper.render_ascii(rgb_array=rgb_array))
            pw.update_pixels(np.array(rgb_array))
            time.sleep(max(0, 1/20-(time.time()-start)))
            spent = time.time()-start
            print(f'{1/spent:.1f} fps | {spent:.3f} s')
