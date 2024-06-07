from wledcast.wled.pixel_writer import PixelWriter
import numpy as np
import time
import sys

pw = PixelWriter('clock.local')

from wledcast.mapper import LEDMapper, generator
mapping = generator.ring(
    length = 60,
    diameter = 15,
    angle = -90,
    reverse = False,
    crop = 0)
mapping = generator.translate(mapping, x=15/2, y=15/2)
print('Mapping', mapping)
led_mapper = LEDMapper(mapping)
print('Bbox', led_mapper.get_bbox())
print('Size', led_mapper.get_size())
scale = 8
print(led_mapper.render_ascii())

while True:
    for j in range(3):
        color = [255, 255, 255]
        color[j] = 0
        for i in range(0, 18):
            start = time.time()
            array_size = (i, i, 3)
            rgb_array = np.full(array_size, color, dtype=np.uint8)
            rgb_array = led_mapper.map_pixels(rgb_array)
            print(led_mapper.render_ascii(rgb_array=rgb_array))
            pw.update_pixels(np.array(rgb_array))
            time.sleep(max(0, 1/10))
            spent = time.time()-start
            print(f'fps = {1/spent} - {spent}s')
