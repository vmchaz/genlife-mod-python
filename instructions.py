from enum import IntEnum, auto

class InstructionSet(IntEnum):
    cmdNOP = auto()
        
    cmdMOV_RR = auto()
    cmdMOV_RI = auto()
    cmdMOV_RA = auto()
    cmdMOV_AR = auto()
    cmdMOV_AI = auto()

    cmdADD_RR = auto()
    cmdADD_RI = auto()
    cmdADD_AR = auto()
    cmdADD_RA = auto()
    cmdADD_AI = auto()

    cmdSUB_RR = auto()
    cmdSUB_RI = auto()
    cmdSUB_AR = auto()
    cmdSUB_RA = auto()
    cmdSUB_AI = auto()

    cmdINC_R = auto()
    cmdINC_A = auto()

    cmdDEC_R = auto()
    cmdDEC_A = auto()

    cmdEQUALS_RR = auto()
    cmdEQUALS_RI = auto()
    cmdEQUALS_RA = auto()
    cmdEQUALS_AR = auto()
    cmdEQUALS_AI = auto()

    cmdNEQUALS_RR = auto()
    cmdNEQUALS_RI = auto()
    cmdNEQUALS_AR = auto()
    cmdNEQUALS_RA = auto()
    cmdNEQUALS_AI = auto()

    cmdGREATER_RR = auto()
    cmdGREATER_RI = auto()
    cmdGREATER_RA = auto()
    cmdGREATER_AR = auto()
    cmdGREATER_AI = auto()

    cmdLESS_RR = auto()
    cmdLESS_RI = auto()
    cmdLESS_RA = auto()
    cmdLESS_AR = auto()
    cmdLESS_AI = auto()

    cmdSET_ACTION_STAND = auto()
    cmdSET_ACTION_EAT = auto()
    cmdSET_ACTION_FORWARD = auto()    
    cmdSET_ACTION_TURN_LEFT = auto()
    cmdSET_ACTION_TURN_RIGHT = auto()
    cmdSET_ACTION_TURN_BACKWARD = auto()
    cmdSET_ACTION_TURN_MOVE_LEFT = auto()
    cmdSET_ACTION_TURN_MOVE_RIGHT = auto()
    cmdSET_ACTION_TURN_MOVE_BACKWARD = auto()


    cmdDETECT_OBSTACLE = auto()
    cmdDETECT_FOOD = auto()
    cmdDETECT_HAZARD = auto()
    cmdDETECT_PREDATOR = auto()
    cmdDETECT_PREY = auto()

    cmdDETECT_OBSTACLE_FAR = auto()
    cmdDETECT_FOOD_FAR = auto()
    cmdDETECT_HAZARD_FAR = auto()
    cmdDETECT_PREDATOR_FAR = auto()
    cmdDETECT_PREY_FAR = auto()

    cmdSET_FLAG = auto()
    cmdRESET_FLAG = auto()

    cmdJMP_REL_R = auto()
    cmdJMP_REL_I = auto()
    cmdJMP_REL_A = auto()
    cmdJMP_ABS_R = auto()
    cmdJMP_ABS_I = auto()
    cmdJMP_ABS_A = auto()
    
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
    
cFlagNames = [str(i) for i in range(16)] + ["F", "R", "B", "L"]
    
def flags_to_str(f):
    return ",".join(cFlagNames[z[0]] for z in enumerate(f) if z[1] == 1)

class Instruction:
    def __init__(self):
        self.cmd = 0
        self.reg_src = None
        self.reg_dest = None
        self.imm = 0
        self.flags_target = [0]*16
        self.flags_allow = [0]*20
        self.flags_deny = [0]*20
        
    def __str__(self):
        return "COMMAND:"+str(self.cmd)+" REGDEST:"+str(self.reg_dest)+" REGSRC:"+str(self.reg_src)+" IMM:"+str(self.imm)+\
        " TARGETFLAGS:"+flags_to_str(self.flags_target)+\
        " FA:"+flags_to_str(self.flags_allow)+\
        " FD:"+flags_to_str(self.flags_deny)

