from assembler import Assembler
from instructions import InstructionSet
from datatypes import *

def _nvmod(v, v_limit):
    if v >= 0:
        return v % v_limit
    else:
        return (v + (-v // v_limit + 1) * v_limit) % v_limit

def flags_to_int(flags):
    i = 0
    m = 1
    for f in flags:
        if f == 1:
            i = i | m
        m = m * 2
    return i



class Instruction:
    def __init__(self):
        self.cmd = 0
        self.reg_src = 0
        self.reg_dest = 0
        self.flags_dest = [0]*16
        self.flags_allow = [0]*16
        self.flags_deny = [0]*16


class Registers:
    VALUE_LIMIT = 256
    REGISTERS_COUNT = 16
    def __init__(self):
        self._registers = [0]*Registers.REGISTERS_COUNT
        
    def __getitem__(self, key):
        if (key < 0) or (key > Registers.REGISTERS_COUNT-1):
            raise Exception("Register index is out of bounds")
        else:
            return self._registers[key]
            
    def __setitem__(self, key, value):
        
        if (key < 0) or (key > Registers.REGISTERS_COUNT-1):
            raise Exception("Register index is out of bounds")
        else:
            if value >= 0:
                self._registers[key] = value % Registers.VALUE_LIMIT
            else:
                self._registers[key] = (value + (-value // Registers.VALUE_LIMIT + 1) * Registers.VALUE_LIMIT) % Registers.VALUE_LIMIT

    def __str__(self):
        return "[" + ", ".join([str(r) for r in self._registers]) + "]"
                
class VCPU:
    VALUE_LIMIT = 256
    def __init__(self):
        self.accumulator = 0
        self.registers = Registers()
        self.flags = [0] * 20
        self.always_active = True
        self.activation_timer = 0
        self.instructions_sequence = None
        self.ip = 0
        self.ip_mod_flag = False
        self.instruction_handlers_map = None
        self.stop_flag = False
        
        
    def init_instruction_handlers(self, handlers):
        self.instruction_handlers_map = handlers
        
    def init_instructions_sequence(self, sequence):
        self.instructions_sequence = sequence
        
    def set_acc(self, value):
        if value >= 0:
            self.accumulator = value % VCPU.VALUE_LIMIT
        else:
            self.accumulator = (value + (-value // VCPU.VALUE_LIMIT + 1) * VCPU.VALUE_LIMIT) % VCPU.VALUE_LIMIT
            
    def flags_to_int(self):
        i = 0
        m = 1
        for f in self.flags:
            if f == 1:
                i = i | m
            m = m * 2
        return i
            
    def get_acc(self):
        return self.accumulator        
        
    def step(self):
        self.ip_mod_flag = False
        if (self.ip >= 0) and (self.ip < len(self.instructions_sequence)):
            ci = self.instructions_sequence[self.ip]

            if check_flags(self, ci):
                instruction_function = self.instruction_handlers_map[ci.cmd]
                instruction_function(self, None, ci, None)
            if not self.ip_mod_flag:
                self.ip += 1
        else:
            self.stop_flag = True
            

cALLOW_FLAG_MODE_OR = 0
cALLOW_FLAG_MODE_AND = 1
cALLOW_FLAG_MODE_MOST = 2
    
def check_allow_flags(vcpu, instruction):
    #afm = instruction.allow_flag_mode    
    flags1 = vcpu.flags_to_int()
    flags2 = flags_to_int(instruction.flags_allow)
    return ((flags1 & flags2) != 0) or (flags2 == 0)
    
def check_deny_flags(vcpu, instruction):
    flags1 = vcpu.flags_to_int()
    flags2 = flags_to_int(instruction.flags_allow)
    return (flags1 & flags2) != 0

def check_flags(vcpu, instruction):
    return check_allow_flags(vcpu, instruction) and not check_deny_flags(vcpu, instruction)
    
    
def set_flags(vcpu, flag_list, v):    
    for e in enumerate(flag_list):
        if e[1] == 1:
            vcpu.flags[e[0]] = v
            
            
def set_ip(vcpu, new_ip):
    if new_ip < 0:
        vcpu.ip = 0
    elif new_ip >= len(vcpu.instructions_sequence):
        vcpu.ip = len(vcpu.instructions_sequence)
    else:
        vcpu.ip = new_ip
    vcpu.ip_mod_flag = True
        
        

def lfNOP(vcpu, g, instruction, fieldpart):
    pass    


def lfMOV_RI(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] = instruction.imm
    
def lfMOV_RR(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] = vcpu.registers[instruction.reg_src]
    
def lfMOV_RA(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] = vcpu.accumulator
    
def lfMOV_AR(vcpu, g, instruction, fieldpart):
    vcpu.accumulator = vcpu.registers[instruction.reg_src]
    
def lfMOV_AI(vcpu, g, instruction, fieldpart):
    vcpu.accumulator = instruction.imm
    

    


def lfADD_RI(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] += instruction.imm
    
def lfADD_RR(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] += vcpu.registers[instruction.reg_src]
    
def lfADD_RA(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] += vcpu.accumulator
    
def lfADD_AR(vcpu, g, instruction, fieldpart):
    vcpu.accumulator += vcpu.registers[instruction.reg_src]
    
def lfADD_AI(vcpu, g, instruction, fieldpart):
    vcpu.accumulator += instruction.imm
    
    
    


def lfSUB_RI(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] -= instruction.imm;
    
def lfSUB_RR(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] -= vcpu.registers[instruction.reg_src]
    
def lfSUB_RA(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] -= vcpu.accumulator
    
def lfSUB_AR(vcpu, g, instruction, fieldpart):
    vcpu.accumulator -= vcpu.registers[instruction.reg_src]
    
def lfSUB_AI(vcpu, g, instruction, fieldpart):
    vcpu.accumulator -= instruction.imm;
    



def lfINC_R(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] += 1
    
def lfINC_A(vcpu, g, instruction, fieldpart):
    vcpu.accumulator += 1

def lfDEC_R(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] -= 1
    
def lfDEC_A(vcpu, g, instruction, fieldpart):
    vcpu.accumulator -= 1
    





def lfEQUALS_RR(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] == vcpu.registers[instruction.reg_src]
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfEQUALS_RI(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] == instruction.imm
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfEQUALS_RA(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] == vcpu.accumulator
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfEQUALS_AR(vcpu, g, instruction, fieldpart):
    v = vcpu.accumulator == vcpu.registers[instruction.reg_src]
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfEQUALS_AI(vcpu, g, instruction, fieldpart):
    v = vcpu.accumulator == instruction.imm
    set_flags(vcpu, instruction.flags_target, ord(v))






def lfNEQUALS_RR(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] != vcpu.registers[instruction.reg_src]
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfNEQUALS_RI(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] != instruction.imm
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfNEQUALS_RA(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] != vcpu.accumulator
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfNEQUALS_AR(vcpu, g, instruction, fieldpart):
    v = vcpu.accumulator != vcpu.registers[instruction.reg_src]
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfNEQUALS_AI(vcpu, g, instruction, fieldpart):
    v = vcpu.accumulator != instruction.imm
    set_flags(vcpu, instruction.flags_target, ord(v))
        
        
        
        
def lfGREATER_RR(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] > vcpu.registers[instruction.reg_src]
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfGREATER_RI(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] > instruction.imm
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfGREATER_RA(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] > vcpu.accumulator
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfGREATER_AR(vcpu, g, instruction, fieldpart):
    v = vcpu.accumulator > vcpu.registers[instruction.reg_src]
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfGREATER_AI(vcpu, g, instruction, fieldpart):
    v = vcpu.accumulator > instruction.imm
    set_flags(vcpu, instruction.flags_target, ord(v))
        
        
        
        
        
def lfLESS_RR(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] < vcpu.registers[instruction.reg_src]
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfLESS_RI(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] < instruction.imm
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfLESS_RA(vcpu, g, instruction, fieldpart):
    v = vcpu.registers[instruction.reg_dest] < vcpu.accumulator
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfLESS_AR(vcpu, g, instruction, fieldpart):
    v = vcpu.accumulator < vcpu.registers[instruction.reg_src]
    set_flags(vcpu, instruction.flags_target, ord(v))
        
def lfLESS_AI(vcpu, g, instruction, fieldpart):
    v = vcpu.accumulator < instruction.imm
    set_flags(vcpu, instruction.flags_target, ord(v))

                
    
def lfSET_ACTION_STAND(vcpu, g, instruction, fieldpart):    
    g.action = Actions.STAND
    
def lfSET_ACTION_EAT(vcpu, g, instruction, fieldpart):    
    g.action = Actions.EAT
    
def lfSET_ACTION_FORWARD(vcpu, g, instruction, fieldpart):    
    g.action = Actions.FORWARD
    
def lfSET_ACTION_TURN_RIGHT(vcpu, g, instruction, fieldpart):    
    g.action = Actions.STAND
    
def lfSET_ACTION_TURN_BACKWARD(vcpu, g, instruction, fieldpart):    
    g.action = Actions.STAND
    
def lfSET_ACTION_TURN_LEFT(vcpu, g, instruction, fieldpart):    
    g.action = Actions.STAND
    
def lfSET_ACTION_TURN_MOVE_RIGHT(vcpu, g, instruction, fieldpart):    
    g.action = Actions.STAND
    
def lfSET_ACTION_TURN_MOVE_BACKWARD(vcpu, g, instruction, fieldpart):    
    g.action = Actions.STAND
    
def lfSET_ACTION_TURN_MOVE_LEFT(vcpu, g, instruction, fieldpart):    
    g.action = Actions.STAND
    
    
    
def lfDETECT_OBSTACLE(vcpu, g, instruction, fieldpart):
    raise NotImplementedError
    
def lfDETECT_FOOD(vcpu, g, instruction, fieldpart):
    raise NotImplementedError    
    
def lfDETECT_HAZARD(vcpu, g, instruction, fieldpart):
    raise NotImplementedError
    
def lfDETECT_PREDATOR(vcpu, g, instruction, fieldpart):
    raise NotImplementedError
    
def lfDETECT_PREY(vcpu, g, instruction, fieldpart):
    raise NotImplementedError
    
    
    
def lfDETECT_OBSTACLE_FAR(vcpu, g, instruction, fieldpart):
    raise NotImplementedError
    
def lfDETECT_FOOD_FAR(vcpu, g, instruction, fieldpart):
    raise NotImplementedError    
    
def lfDETECT_HAZARD_FAR(vcpu, g, instruction, fieldpart):
    raise NotImplementedError
    
def lfDETECT_PREDATOR_FAR(vcpu, g, instruction, fieldpart):
    raise NotImplementedError
    
def lfDETECT_PREY_FAR(vcpu, g, instruction, fieldpart):
    raise NotImplementedError
    
    


def lfSET_FLAG(vcpu, g, instruction, fieldpart):
    set_flags(vcpu, instruction.flags_target, 1)
    
def lfRESET_FLAG(vcpu, g, instruction, fieldpart):
    set_flags(vcpu, instruction.flags_target, 0)
    

def lfJMP_REL_R(vcpu, g, instruction, fieldpart):
    ip_ofs = vcpu.registers[instruction.reg_dest]
    new_ip = vcpu.ip + ( (ip_ofs + 128) % 256 - 128 )
    set_ip(vcpu, new_ip)
    
def lfJMP_REL_I(vcpu, g, instruction, fieldpart):
    ip_ofs = instruction.imm
    new_ip = vcpu.ip + ( (ip_ofs + 128) % 256 - 128 )
    set_ip(vcpu, new_ip)
    
def lfJMP_REL_A(vcpu, g, instruction, fieldpart):
    ip_ofs = vcpu.accumulator
    new_ip = vcpu.ip + ( (ip_ofs + 128) % 256 - 128 )
    set_ip(vcpu, new_ip)
    
    
def lfJMP_ABS_R(vcpu, g, instruction, fieldpart):
    new_ip = vcpu.registers[instruction.reg_dest]
    set_ip(vcpu, new_ip)
    
def lfJMP_ABS_I(vcpu, g, instruction, fieldpart):
    new_ip = instruction.imm
    set_ip(vcpu, new_ip)
    
def lfJMP_ABS_A(vcpu, g, instruction, fieldpart):
    new_ip = vcpu.accumulator
    set_ip(vcpu, new_ip)



cInstructionHandlersMap = {
    InstructionSet.cmdNOP:lfNOP,
    
    InstructionSet.cmdMOV_RR:lfMOV_RR,
    InstructionSet.cmdMOV_RI:lfMOV_RI,
    InstructionSet.cmdMOV_RA:lfMOV_RA,
    InstructionSet.cmdMOV_AR:lfMOV_AR,
    InstructionSet.cmdMOV_AI:lfMOV_AI,
    
    InstructionSet.cmdADD_RR:lfADD_RR,
    InstructionSet.cmdADD_RI:lfADD_RI,
    InstructionSet.cmdADD_AR:lfADD_AR,
    InstructionSet.cmdADD_RA:lfADD_RA,
    InstructionSet.cmdADD_AI:lfADD_AI,
    
    InstructionSet.cmdSUB_RR:lfSUB_RR,
    InstructionSet.cmdSUB_RI:lfSUB_RI,
    InstructionSet.cmdSUB_AR:lfSUB_AR,
    InstructionSet.cmdSUB_RA:lfSUB_RA,
    InstructionSet.cmdSUB_AI:lfSUB_AI,
    
    InstructionSet.cmdINC_R:lfINC_R,
    InstructionSet.cmdINC_A:lfINC_A,
    InstructionSet.cmdDEC_R:lfDEC_R,
    InstructionSet.cmdDEC_A:lfDEC_A,

    InstructionSet.cmdEQUALS_RR:lfEQUALS_RR,
    InstructionSet.cmdEQUALS_RI:lfEQUALS_RI,
    InstructionSet.cmdEQUALS_RA:lfEQUALS_RA,
    InstructionSet.cmdEQUALS_AR:lfEQUALS_AR,
    InstructionSet.cmdEQUALS_AI:lfEQUALS_AI,
    
    InstructionSet.cmdNEQUALS_RR:lfNEQUALS_RR,
    InstructionSet.cmdNEQUALS_RI:lfNEQUALS_RI,
    InstructionSet.cmdNEQUALS_AR:lfNEQUALS_AR,
    InstructionSet.cmdNEQUALS_RA:lfNEQUALS_RA,
    InstructionSet.cmdNEQUALS_AI:lfNEQUALS_AI,
    
    InstructionSet.cmdGREATER_RR:lfGREATER_RR,
    InstructionSet.cmdGREATER_RI:lfGREATER_RI,
    InstructionSet.cmdGREATER_RA:lfGREATER_RA,
    InstructionSet.cmdGREATER_AR:lfGREATER_AR,
    InstructionSet.cmdGREATER_AI:lfGREATER_AI,
    
    InstructionSet.cmdLESS_RR:lfLESS_RR,
    InstructionSet.cmdLESS_RI:lfLESS_RI,
    InstructionSet.cmdLESS_RA:lfLESS_RA,
    InstructionSet.cmdLESS_AR:lfLESS_AR,
    InstructionSet.cmdLESS_AI:lfLESS_AI,
    
    InstructionSet.cmdSET_ACTION_STAND:lfSET_ACTION_STAND,
    InstructionSet.cmdSET_ACTION_EAT:lfSET_ACTION_EAT,
    InstructionSet.cmdSET_ACTION_FORWARD:lfSET_ACTION_FORWARD,
    InstructionSet.cmdSET_ACTION_TURN_BACKWARD:lfSET_ACTION_TURN_BACKWARD,
    InstructionSet.cmdSET_ACTION_TURN_LEFT:lfSET_ACTION_TURN_LEFT,
    InstructionSet.cmdSET_ACTION_TURN_RIGHT:lfSET_ACTION_TURN_RIGHT,
    InstructionSet.cmdSET_ACTION_TURN_MOVE_LEFT:lfSET_ACTION_TURN_MOVE_LEFT,
    InstructionSet.cmdSET_ACTION_TURN_MOVE_RIGHT:lfSET_ACTION_TURN_MOVE_RIGHT,
    
    InstructionSet.cmdDETECT_OBSTACLE:lfDETECT_OBSTACLE,
    InstructionSet.cmdDETECT_FOOD:lfDETECT_FOOD,
    InstructionSet.cmdDETECT_HAZARD:lfDETECT_HAZARD,
    InstructionSet.cmdDETECT_PREDATOR:lfDETECT_PREDATOR,
    InstructionSet.cmdDETECT_PREY:lfDETECT_PREY,
    
    InstructionSet.cmdDETECT_OBSTACLE_FAR:lfDETECT_OBSTACLE_FAR,
    InstructionSet.cmdDETECT_FOOD_FAR:lfDETECT_FOOD_FAR,
    InstructionSet.cmdDETECT_HAZARD_FAR:lfDETECT_HAZARD_FAR,
    InstructionSet.cmdDETECT_PREDATOR_FAR:lfDETECT_PREDATOR_FAR,
    InstructionSet.cmdDETECT_PREY_FAR:lfDETECT_PREY_FAR,
    
    InstructionSet.cmdSET_FLAG:lfSET_FLAG,
    InstructionSet.cmdRESET_FLAG:lfRESET_FLAG,
    
    InstructionSet.cmdJMP_REL_R:lfJMP_REL_R,
    InstructionSet.cmdJMP_REL_I:lfJMP_REL_I,
    InstructionSet.cmdJMP_REL_A:lfJMP_REL_A,
    
    InstructionSet.cmdJMP_ABS_R:lfJMP_ABS_R,
    InstructionSet.cmdJMP_ABS_I:lfJMP_ABS_I,
    InstructionSet.cmdJMP_ABS_A:lfJMP_ABS_A
}
