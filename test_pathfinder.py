import pytest
import random
from pathfinder import MapInfo, Pathfinder, MapImage


my_map = MapInfo('elevation_small.txt')
my_map_image = MapImage(my_map)
path_it_out = Pathfinder(my_map, 'new_map.png')

def test_get_max_elevation():
    assert my_map.get_max_elevation() == 5648

def test_get_min_elevation():
    assert my_map.get_min_elevation() == 3139

def test_color_value():
    assert my_map_image.get_color_value(3, 6) in range(1, 255)