   
class Directions:
    FORWARD = 0
    RIGHT = 1
    BACK = 2
    LEFT = 3
    
class DirectionFlags:
    FORWARD = 16
    RIGHT = 17
    BACK = 18
    LEFT = 19
    
    
class Actions:
    NONE = 0
    
    STAND = 1
    EAT = 2
    FORWARD = 3
    
    TURN_RIGHT = 4    
    TURN_BACKWARD = 5
    TURN_LEFT = 6
    
    TURN_MOVE_RIGHT = 7
    TURN_MOVE_BACKWARD = 8
    TURN_MOVE_LEFT = 9
    

class ArgumentTypes():
    IMM = 0
    REG = 1
