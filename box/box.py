class Cuboid(object):
    def __init__(self, x, y, size):
        self.x = x 
        self.y = y
        self.size = size

    def get_surface(self):
        surface = 2 * (self.x * self.y + self.x * self.size + self.y * self.size)
        return surface
        
        
    def get_volume(self):
        
        volume = self.x * self.y * self.size
        return volume
        
        
        
box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000


# Create a class that represents a cuboid:
# It should take its three dimensions as constructor parameters (numbers)
# It should have a method called `get_surface` that returns the cuboid's surface
# It should have a method called `get_volume` that returns the cuboid's volume
