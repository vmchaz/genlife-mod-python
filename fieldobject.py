from directions import AbsoluteDirections

class FieldObjectTypes:
    NONE = 0
    OBSTACLE = 1
    HAZARD = 2
    FOOD = 3
    UNIT = 4
    PREDATOR = 5


cFieldMapUp = [
    [0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 1],
    [3, 3, 0, 0, 0, 1, 1],
    [3, 3, 3, 9, 1, 1, 1],
    [3, 3, 2, 2, 2, 1, 1],
    [3, 2, 2, 2, 2, 2, 1],
    [2, 2, 2, 2, 2, 2, 2]]

cFieldMapRight = [
    [3, 3, 3, 3, 3, 3, 3],
    [2, 3, 3, 3, 3, 3, 0],
    [2, 2, 3, 3, 3, 0, 0],
    [2, 2, 2, 9, 0, 0, 0],
    [2, 2, 1, 1, 1, 0, 0],
    [2, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1]]

cFieldMapDown = [
    [2, 2, 2, 2, 2, 2, 2],
    [1, 2, 2, 2, 2, 2, 3],
    [1, 1, 2, 2, 2, 3, 3],
    [1, 1, 1, 9, 3, 3, 3],
    [1, 1, 0, 0, 0, 3, 3],
    [1, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0]]

cFieldMapLeft = [
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 2],
    [0, 0, 1, 1, 1, 2, 2],
    [0, 0, 0, 9, 2, 2, 2],
    [0, 0, 3, 3, 3, 2, 2],
    [0, 3, 3, 3, 3, 3, 2],
    [3, 3, 3, 3, 3, 3, 3]]


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width*height
        self.cells = [FieldObjectTypes.NONE] * self.size
        self.obj_cells = [[]] * self.size
        
    def move_object(self, obj, x, y, new_x, new_y):
        obj_cell = self.obj_cells[y * self.width + x]
        i = obj_cell.index(obj)        
        if i >= 0:
            obj_cell.pop(i)
            new_obj_cell = self.obj_cells[new_y * self.width + new_x]
            
    def is_obstacle(self, x, y):
        obj_cell = self.obj_cells[y * self.width + x]
        for obj in obj_cell:
            if obj.obstacle_level >= 1:
                return True
        return False
        

def get_field_cell(field:Field, x:int, y:int):
    if (x >= 0) and (x < field.width) and (y >= 0) and (y < field.height):
        return field.cells[y*field.width + x]
    else:
        return FieldObjectTypes.NONE

def scan_for_specific_object(field:Field, x:int, y:int, direction):
    square_size = 7
    for tmpy in range(0, 7):
        for tmpx in range(0, 7):
            local_x = x + tmpx - square_size // 2
            local_y = y + tmpy - square_size // 2
            obj_type = get_field_cell(field, local_x, local_y)
