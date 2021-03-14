def lfNOP(vcpu, g, instruction, fieldpart):
    pass
    

def nvmod(v, v_limit):
    if v >= 0:
        return v % v_limit
    else:
        return (v + (-v // v_limit + 1) * v_limit) % v_limit


def lfMOV_RI(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] = instruction.imm;
    
def lfMOV_RR(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] = vcpu.registers[instruction.reg_src]
    
def lfMOV_RA(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] = vcpu.accumulator
    
def lfMOV_AR(vcpu, g, instruction, fieldpart):
    vcpu.accumulator = vcpu.registers[instruction.reg_dest]
    
def lfMOV_AI(vcpu, g, instruction, fieldpart):
    vcpu.accumulator = instruction.imm;
    
    


def lfADD_RI(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] += instruction.imm;
    
def lfADD_RR(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] += vcpu.registers[instruction.reg_src]
    
def lfADD_RA(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] += vcpu.accumulator
    
def lfADD_AR(vcpu, g, instruction, fieldpart):
    vcpu.accumulator += vcpu.registers[instruction.reg_dest]
    
def lfADD_AI(vcpu, g, instruction, fieldpart):
    vcpu.accumulator += instruction.imm;
    
    
    
def lfSUB_RI(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] -= instruction.imm;
    
def lfSUB_RR(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] -= vcpu.registers[instruction.reg_src]
    
def lfSUB_RA(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] -= vcpu.accumulator
    
def lfSUB_AR(vcpu, g, instruction, fieldpart):
    vcpu.accumulator -= vcpu.registers[instruction.reg_dest]
    
def lfSUB_AI(vcpu, g, instruction, fieldpart):
    vcpu.accumulator -= instruction.imm;
    



def lfINC_R(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] += 1
    
def lfDEC_R(vcpu, g, instruction, fieldpart):
    vcpu.registers[instruction.reg_dest] -= 1
    
def lfINC_A(vcpu, g, instruction, fieldpart):
    vcpu.accumulator += 1
    
def lfDEC_A(vcpu, g, instruction, fieldpart):
    vcpu.accumulator -= 1
    


