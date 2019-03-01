import PIL

class Coordinates:
    """
    Creates the lists and methods used to generate the map.
    """
    def __init__(self, filename):
        """Sets methods to variables in Coordinates class"""
        self.elevations = self.get_elevations(filename)
        self.max_elevation = self.get_max_elevation()
        self.min_elevation = self.get_min_elevation()
        self.color_value = self.get_color_value()
        
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

    def get_color_value(self):
        """Assigns color value to coordinate based on elevation"""
        # Not sure I'm putting the color_number in the right spot right now... we'll see what colors come out.
        current_elevation = 3500
        color_number = int((current_elevation - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255)
        self.color_value = (color_number, color_number, color_number, 0)
        return self.color_value

    # def draw_map(self, color_values):


class MapImage:
    """
    Reads text file of map. Generates output of elevation by color variation in image file.
    """
    

class Pathfinder:
    """
    Draws a path from the westernmost axis on the map to a destination on the easternmost axis. Looks for next step by searching for elevation value closest to current elevation value, with 3 coordinates, always moving east.
    """

if __name__ == "__main__":

    my_map = Coordinates('elevation_small.txt')

    print(my_map.max_elevation, my_map.min_elevation, my_map.color_value)

