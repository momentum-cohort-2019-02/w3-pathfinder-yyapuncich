from PIL import ImageColor, ImageDraw, Image

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
        # Creating my 2D list- understanding it: https://snakify.org/de/lessons/two_dimensional_lists_arrays/
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


class MapImage:
    """
    Generates output of elevation by color variation in image file.
    """
    def __init__(self, my_map):
        self.my_map = my_map
        # had to add len() to list info here so it would return a number for creating size on new image.
        self.im = Image.new('RGBA', (len(self.my_map.elevations[0]), len(self.my_map.elevations)))
        # self.new_image = draw_map()
    def get_current_elevation(self, x, y):
        return self.my_map.elevations[y][x]

    def get_color_value(self, x, y):
        """Assigns color value to coordinate based on current elevation"""
        return int((self.get_current_elevation(x, y) - self.my_map.min_elevation) / (self.my_map.max_elevation - self.my_map.min_elevation) * 255)

    def draw_map(self):
        """For elevations listed in elevation list use the color value to draw the map."""
        # What is Numpy? Saw it in my searches about putpixel...
        # automate boring stuff- putpixel step 3.
        for x in range(len(self.my_map.elevations[0])):
            for y in range(len(self.my_map.elevations)):
                self.im.putpixel((x, y), ((self.get_color_value(x, y)), (self.get_color_value(x, y)), (self.get_color_value(x, y))))
        return self.im.save('new_map.png')


class Pathfinder:
    """
    Draws a path from a westernmost axis on the map to a destination on the easternmost axis. Looks for next step by searching for elevation value closest to current elevation value, with 3 Elevations, always moving east.
    """
    def __init__(self, my_map, filename):
        # self.path_it_out = path_it_out
        self.my_map = my_map
        self.draw_line = Image.open(filename)

    def get_route(self):
        """Creates list of potential next steps based on current location. Also creates diff_list that will be used to find min difference for next step"""
        # couldn't get this to work when I broke up this method into smaller parts, but it works right now
        cur_x = 0
        cur_y = 350
        # not sure why -1 is needed below?
        while cur_x < len(self.my_map.elevations[0]) - 1:
            potential_ys = [cur_y]
            if cur_y - 1 >= 0:
                potential_ys.append(cur_y - 1)
            if cur_y + 1 < len(self.my_map.elevations):
                potential_ys.append(cur_y + 1)
        # diff_list get's list of difference in elevation values from (next column potenial steps) - (current column location/elevation)  
            self.diff_list = [abs(self.my_map.elevations[pot_y][cur_x + 1] - self.my_map.elevations[cur_y][cur_x]) for pot_y in potential_ys]
        # bear with me: the min_diff gets the value from next potential_y that is best, the min_diff_index saves that location on the diff_list, the next_y selects the potenial_y that matches that same location of the min_diff_index...
            min_diff = min(self.diff_list)
            min_diff_index = self.diff_list.index(min_diff)
            next_y = potential_ys[min_diff_index]
            #create my list of coordinates for the path 
            line_creator = ImageDraw.Draw(self.draw_line)
            line_creator.point((cur_x, cur_y), (240, 255, 140))
        # getting all the points that we'll need to draw the dang route
            cur_x += 1
            cur_y = next_y
        return self.draw_line.save('drawn_line.png')

if __name__ == "__main__":
# instantiate (def: represent as or by an instance)
    my_map = MapInfo('elevation_small.txt')
    my_map_image = MapImage(my_map)
    my_map_image.draw_map()
    path_it_out = Pathfinder(my_map, 'new_map.png')
    path_it_out.get_route()
