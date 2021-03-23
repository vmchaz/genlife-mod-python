from enum import IntEnum, auto
from functools import reduce

class InstructionSet(IntEnum):
    cmdNOP = auto()
        
    cmdMOV_RR = auto()
    cmdMOV_RI = auto()
    cmdMOV_RA = auto()
    cmdMOV_AR = auto()
    cmdMOV_AI = auto()

    cmdADD_RR = auto()
    cmdADD_RI = auto()
    cmdADD_RA = auto()
    cmdADD_AR = auto()
    cmdADD_AI = auto()

    cmdSUB_RR = auto()
    cmdSUB_RI = auto()
    cmdSUB_RA = auto()
    cmdSUB_AR = auto()
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
    cmdNEQUALS_RA = auto()
    cmdNEQUALS_AR = auto()
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


class ArgumentTypes():
    NONE = 0
    IMM = 1
    REG_SRC = 2
    REG_DEST = 3


cInstructionArguments = {
    InstructionSet.cmdNOP: [],

    InstructionSet.cmdMOV_RR: [ArgumentTypes.REG_DEST, ArgumentTypes.REG_SRC],
    InstructionSet.cmdMOV_RI: [ArgumentTypes.REG_DEST, ArgumentTypes.IMM],
    InstructionSet.cmdMOV_RA: [ArgumentTypes.REG_DEST],
    InstructionSet.cmdMOV_AR: [ArgumentTypes.REG_SRC],
    InstructionSet.cmdMOV_AI: [ArgumentTypes.IMM],

    InstructionSet.cmdADD_RR: [ArgumentTypes.REG_DEST, ArgumentTypes.REG_SRC],
    InstructionSet.cmdADD_RI: [ArgumentTypes.REG_DEST, ArgumentTypes.IMM],
    InstructionSet.cmdADD_AR: [ArgumentTypes.REG_DEST],
    InstructionSet.cmdADD_RA: [ArgumentTypes.REG_SRC],
    InstructionSet.cmdADD_AI: [ArgumentTypes.IMM],

    InstructionSet.cmdSUB_RR: [ArgumentTypes.REG_DEST, ArgumentTypes.REG_SRC],
    InstructionSet.cmdSUB_RI: [ArgumentTypes.REG_DEST, ArgumentTypes.IMM],
    InstructionSet.cmdSUB_RA: [ArgumentTypes.REG_DEST],
    InstructionSet.cmdSUB_AR: [ArgumentTypes.REG_SRC],
    InstructionSet.cmdSUB_AI: [ArgumentTypes.IMM],

    InstructionSet.cmdINC_R: [ArgumentTypes.REG_DEST],
    InstructionSet.cmdINC_A: [],

    InstructionSet.cmdDEC_R: [ArgumentTypes.REG_DEST],
    InstructionSet.cmdDEC_A: [],

    InstructionSet.cmdEQUALS_RR: [ArgumentTypes.REG_DEST, ArgumentTypes.REG_SRC],
    InstructionSet.cmdEQUALS_RI: [ArgumentTypes.REG_DEST, ArgumentTypes.IMM],
    InstructionSet.cmdEQUALS_RA: [ArgumentTypes.REG_DEST],
    InstructionSet.cmdEQUALS_AR: [ArgumentTypes.REG_SRC],
    InstructionSet.cmdEQUALS_AI: [ArgumentTypes.IMM],

    InstructionSet.cmdNEQUALS_RR: [ArgumentTypes.REG_DEST, ArgumentTypes.REG_SRC],
    InstructionSet.cmdNEQUALS_RI: [ArgumentTypes.REG_DEST, ArgumentTypes.IMM],
    InstructionSet.cmdNEQUALS_RA: [ArgumentTypes.REG_DEST],
    InstructionSet.cmdNEQUALS_AR: [ArgumentTypes.REG_SRC],
    InstructionSet.cmdNEQUALS_AI: [ArgumentTypes.IMM],

    InstructionSet.cmdGREATER_RR: [ArgumentTypes.REG_DEST, ArgumentTypes.REG_SRC],
    InstructionSet.cmdGREATER_RI: [ArgumentTypes.REG_DEST, ArgumentTypes.IMM],
    InstructionSet.cmdGREATER_RA: [ArgumentTypes.REG_DEST],
    InstructionSet.cmdGREATER_AR: [ArgumentTypes.REG_SRC],
    InstructionSet.cmdGREATER_AI: [ArgumentTypes.IMM],

    InstructionSet.cmdLESS_RR: [ArgumentTypes.REG_DEST, ArgumentTypes.REG_SRC],
    InstructionSet.cmdLESS_RI: [ArgumentTypes.REG_DEST, ArgumentTypes.IMM],
    InstructionSet.cmdLESS_RA: [ArgumentTypes.REG_DEST],
    InstructionSet.cmdLESS_AR: [ArgumentTypes.REG_SRC],
    InstructionSet.cmdLESS_AI: [ArgumentTypes.IMM],

    InstructionSet.cmdSET_ACTION_STAND: [],
    InstructionSet.cmdSET_ACTION_EAT: [],
    InstructionSet.cmdSET_ACTION_FORWARD: [],
    InstructionSet.cmdSET_ACTION_TURN_LEFT: [],
    InstructionSet.cmdSET_ACTION_TURN_RIGHT: [],
    InstructionSet.cmdSET_ACTION_TURN_BACKWARD: [],
    InstructionSet.cmdSET_ACTION_TURN_MOVE_LEFT: [],
    InstructionSet.cmdSET_ACTION_TURN_MOVE_RIGHT: [],
    InstructionSet.cmdSET_ACTION_TURN_MOVE_BACKWARD: [],

    InstructionSet.cmdDETECT_OBSTACLE: [],
    InstructionSet.cmdDETECT_FOOD: [],
    InstructionSet.cmdDETECT_HAZARD: [],
    InstructionSet.cmdDETECT_PREDATOR: [],
    InstructionSet.cmdDETECT_PREY: [],

    InstructionSet.cmdDETECT_OBSTACLE_FAR: [],
    InstructionSet.cmdDETECT_FOOD_FAR: [],
    InstructionSet.cmdDETECT_HAZARD_FAR: [],
    InstructionSet.cmdDETECT_PREDATOR_FAR: [],
    InstructionSet.cmdDETECT_PREY_FAR: [],

    InstructionSet.cmdSET_FLAG: [],
    InstructionSet.cmdRESET_FLAG: [],

    InstructionSet.cmdJMP_REL_R: [ArgumentTypes.REG_SRC],
    InstructionSet.cmdJMP_REL_I: [ArgumentTypes.IMM],
    InstructionSet.cmdJMP_REL_A: [],
    InstructionSet.cmdJMP_ABS_R: [ArgumentTypes.REG_SRC],
    InstructionSet.cmdJMP_ABS_I: [ArgumentTypes.IMM],
    InstructionSet.cmdJMP_ABS_A: [],
}



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
    



    
cFlagNames = [str(i) for i in range(16)] + ["F", "R", "B", "L"]
    
def flags_to_str(f):
    return ",".join(cFlagNames[z[0]] for z in enumerate(f) if z[1] == 1)
    
def flags_to_int(f):
    r = 0
    for bn, fv in enumerate(f):
        if fv == 1:
            r = r | (1 << bn)
    return r

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
        
    def to_code_named(self):
        cmd = self.cmd
        reg_dest = self.reg_dest if self.reg_dest else 0
        reg_src = self.reg_src if self.reg_src else 0
        imm = self.imm if self.imm else 0
        flags_allow = flags_to_int(self.flags_allow)
        flags_deny = flags_to_int(self.flags_deny)
        flags_target = flags_to_int(self.flags_target)

        return f"cmd={cmd}, reg_dest={reg_dest}, reg_src={reg_src}, imm={imm}, flags_allow={flags_allow}, flags_deny={flags_deny}, flags_target={flags_target}"
        
    def to_code(self):
        cmd = self.cmd
        reg_dest = self.reg_dest if self.reg_dest else 0
        reg_src = self.reg_src if self.reg_src else 0
        imm = self.imm if self.imm else 0
        flags_allow = flags_to_int(self.flags_allow)
        flags_deny = flags_to_int(self.flags_deny)
        flags_target = flags_to_int(self.flags_target)

        return f"{cmd}, {reg_dest}, {reg_src}, {imm}, {flags_allow}, {flags_deny}, {flags_target}"        
        
    def to_tuple(self):
        return (int(self.cmd), self.reg_dest if self.reg_dest else 0, self.reg_src if self.reg_src else 0, self.imm if self.imm else 0, reduce(lambda p,c:p*2+c,reversed(self.flags_allow)), reduce(lambda p,c:p*2+c,reversed(self.flags_deny)), reduce(lambda p,c:p*2+c,reversed(self.flags_target)))

