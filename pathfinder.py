from PIL import ImageColor, ImageDraw, Image
import random
import pprint

class MapInfo:
    """
    Creates the lists and methods used to generate the map.
    """
    def __init__(self, filename):
        """Sets methods to variables in Elevations class"""
        self.elevations = self.get_elevations(filename)
        self.max_elevation = self.get_max_elevation()
        self.min_elevation = self.get_min_elevation()
        
    def get_elevations(self, filename):
        """Gets total list of elevations from file"""
        with open(filename) as file:
            self.elevations = [[int(e) for e in line.split(" ")] for line in file]
        return self.elevations
    
    def get_max_elevation(self):
        """Gets maximun elevation in from file in get_elevations"""
        self.max_elevation = max([max(row) for row in self.elevations])
        return self.max_elevation

    def get_min_elevation(self):
        """Gets minimum elevation in from file in get_elevations"""
        self.min_elevation = min([min(row) for row in self.elevations])
        return self.min_elevation

    def get_current_elevation(self, x, y):
        """Gets elevation at one point to create color pixel for that coordinate"""
        # figure out how this works ?????
        return self.elevations[y][x]

    def get_color_value(self, x, y):
        """Assigns color value to coordinate based on current elevation"""
        # Not sure I'm putting the color_number in the right spot right now... we'll see what colors come out. Maybe move this to MapImage class
        color_number = int((self.get_current_elevation(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255)
        self.color_value = (color_number, color_number, color_number, 0)
        return self.color_value

class MapImage:
    """
    Generates output of elevation by color variation in image file.
    """
    def __init__(self, my_map):
        self.my_map = my_map
        # had to add len() to list info here so it would return a number for creating size on new image.
        self.im = Image.new('RGBA', (len(self.my_map.elevations[0]), len(self.my_map.elevations)))
        # self.new_image = draw_map()

    def draw_map(self):
        """For elevations listed in elevation list use the color value to draw the map."""
        # What is Numpy? Saw it in my searches about putpixel...
        for y in range(len(self.my_map.elevations)):
            self.im.putpixel((x,y), (self.my_map.color_value(x,y)))
            self.im.save('my_map.png')
        


class Pathfinder:
    """
    Draws a path from the westernmost axis on the map to a destination on the easternmost axis. Looks for next step by searching for elevation value closest to current elevation value, with 3 Elevations, always moving east.
    """

if __name__ == "__main__":

# instantiate (def: represent as or by an instance)
    my_map = MapInfo('elevation_small.txt')
    drawing = MapImage(my_map)
    drawing.draw_map()
    print(my_map.max_elevation, my_map.min_elevation)