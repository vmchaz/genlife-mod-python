from instructions import *
from assembler import Assembler
from vcpu import VCPU, cInstructionHandlersMap

asm_text = """
mov_ri r0, 200
mov_ri r1, 50
add_rr r0, r1
mov_ar r0
"""

def main():
    a = Assembler()
    r = a.AssembleText(asm_text)
    r2 = a.AssembleInstruction("add_rr r0, r1")
    print(r2)
    vcpu = VCPU()
    vcpu.init_instruction_handlers(cInstructionHandlersMap)
    vcpu.init_instructions_sequence(r)
    while not vcpu.stop_flag:
        vcpu.step()

    print(vcpu.registers)
    print(vcpu.accumulator)
    
    print(r)
    

if __name__ == "__main__":
    main()
