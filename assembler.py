from enum import IntEnum, auto
from instructions import InstructionSet, Instruction, DirectionFlags, cInstructionArguments, ArgumentTypes

def flag_str_to_number(s):
    s = s.upper()
    if s == "F":
        return DirectionFlags.FORWARD
    elif s == "R":
        return DirectionFlags.RIGHT
    elif s == "B":
        return DirectionFlags.BACK
    elif s == "L":
        return DirectionFlags.LEFT
    else:
        return int(s)
        
def is_reg(s):
    s = s.upper()
    if s.startswith("R"):
        if s[1:].isdigit():
            return True
    return False
    
def get_reg(s):
    return int(s[1:])
    
def is_imm(s):
    return s.isdigit()
    
def get_imm(s):
    return int(s)

class Assembler:
    def __init__(self):
        self.command_to_str = {}
        self.str_to_command = {}
        for m in dir(InstructionSet):
            if m.startswith("cmd"):
                cmd_name = m[3:]
                cmd_int = InstructionSet.__members__[m]
                self.command_to_str[cmd_int] = cmd_name
                self.str_to_command[cmd_name] = cmd_int
                

    def AssembleInstruction(self, S):
        S = S.upper()
        S = S.replace(":", ": ")
        S = S.replace(",", " ")
        while "  " in S:
            S = S.replace("  ", " ")
            
        arg_list = S.split(" ")
        if len(arg_list) > 0:
            cMAIN = 0
            cFLAG_ALLOW = 1
            cFLAG_DENY = 2
            cFLAG_TARGET = 3
            
            cFlagNames = ["C:", "A:", "D:", "T:"]
            
            st = cMAIN
            cmd = arg_list.pop(0)
            main_args = []
            allow_flags = []
            deny_flags = []
            target_flags = []
            
            
            for arg in arg_list:
                if arg not in cFlagNames:
                    if st == cMAIN:
                        main_args.append(arg)
                    
                    elif st == cFLAG_ALLOW:
                        allow_flags.append(arg)
                    
                    elif st == cFLAG_DENY:
                        deny_flags.append(arg)
                        
                    elif st == cFLAG_TARGET:
                        target_flags.append(arg)
                else:
                    st = cFlagNames.index(arg)
            
                    
            instruction = Instruction()
            instruction.cmd = self.str_to_command[cmd]

            if len(arg_list) < len(cInstructionArguments[instruction.cmd]):
                raise Exception("Too few arguments")

            if len(arg_list) > len(cInstructionArguments[instruction.cmd]):
                raise Exception("Too many arguments")
            
            for arg_type, arg_in_command in zip(cInstructionArguments[instruction.cmd], arg_list):
                if arg_type == ArgumentTypes.REG_DEST:
                    instruction.reg_dest = get_reg(arg_in_command)
                elif arg_type == ArgumentTypes.REG_SRC:
                    instruction.reg_src = get_reg(arg_in_command)
                elif arg_type == ArgumentTypes.IMM:
                    instruction.imm = get_imm(arg_in_command)
            
            for f in allow_flags:                
                fn = flag_str_to_number(f)
                instruction.flags_allow[fn] = 1
                
            for f in deny_flags:                
                fn = flag_str_to_number(f)
                instruction.flags_deny[fn] = 1
                
            for f in target_flags:                
                fn = flag_str_to_number(f)
                instruction.flags_target[fn] = 1
                
            
            return instruction


    def AssembleText(self, t):
        lines = t.split("\n")
        instructions = []
        for line in lines:
            s2 = line.strip(" "+chr(9))
            if s2:
                instructions.append(self.AssembleInstruction(s2))
        return instructions
