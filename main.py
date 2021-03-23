#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import time

from functools import reduce
import field
import assembler

# пути до модуля virtanimal
#sys.path.append('.')
#sys.path.append('lib/')
#sys.path.append('.')
#sys.path.append('../')
#sys.path.append('../../')
sys.path.append('./virtanimal/lib')

import virtanimal

def f1():
    print("f1")
    

cDirectionDX = [0, 1, 0, -1, 0, 1, 0, -1]
cDirectionDY = [-1, 0, 1, 0, -1, 0, 1, 0]
cDirectionNames = ["Fw", "Rt", "Bk", "Lt"]

def field_callback(field_obj, obj_type, obj_subtype, x, y, direction, shape, distance, fill_flags, fieldpart):
    print(f"field callback obj_type:{obj_type} obj_subtype:{obj_subtype} x:{x} y:{y} direction:{direction} shape:{shape} distance:{distance}")
    if shape == 1:
        if distance == 1:
            f_objs = [field_obj.get_item(x + cDirectionDX[direction + i], y + cDirectionDY[direction + i]) for i in range(4)]
            f_flags = [0, 0, 0, 0]            
            for i in range(4):
                obj = f_objs[i]
                print("Object", cDirectionNames[i], obj)
                if obj is not None:
                    ft = obj.local_type
                    print("Type", obj.local_type, "Subtype", obj.local_subtype)
                    if (ft == obj_type) and ((obj_subtype == 0) or ((obj_subtype != 0) and (obj_subtype == obj.local_subtype))):
                        f_flags[i] = 1
                        
            fieldpart.f_forward = f_flags[0]
            fieldpart.f_right = f_flags[1]
            fieldpart.f_back = f_flags[2]
            fieldpart.f_left = f_flags[3]
            fieldpart.flags_filled = 1
            
    #print("f2")
    #print(obj_type, obj_subtype, x, y, direction, shape, distance, fill_flags);
    #print("field:", type(field))
    #print("fieldpart:", type(fieldpart))
    #fieldpart.f_forward = 1
    #fieldpart.f_back = 1
    #fieldpart.flags_filled = 1
    


fp = virtanimal.FieldPart()
#print(type(fp), dir(fp))

fld = field.Field(10, 10)
#for i in range(10):
#    for j in range(10):
#        fld.set_item(i, j, i*100+j)
        



asm = assembler.Assembler()
#instruction = 
#print(*instruction.to_tuple())



c = virtanimal.VCPU(1)
u = virtanimal.UnitVarStruct(1, 1000, 0, 0, 0)
s = virtanimal.InstructionSequence(0)
s1 = virtanimal.InstructionSequence(0)

a = virtanimal.Animal()


o1 = virtanimal.Obstacle()
fld.set_item(1, 1, o1)
a.x = 2
a.y = 1
a.direction = 0
#print(a.x, a.y)
fld.set_item(a.x, a.y, a)
#obj1 = fld.get_item(2, 1)
#print(fld.field)
#print(type(obj1))

#exit()

def print_vcpu(vcpu):
#    virtanimal.vcpu_run(vcpu, sequence, unitvarstruct, 1)
    flags_str = ("{0:b}".format(vcpu.flags)).zfill(20)
    print(vcpu.ip, "    ", vcpu.accumulator, flags_str, "[", str(vcpu.r0).zfill(3), vcpu.r1, vcpu.r2, vcpu.r3, vcpu.r4, vcpu.r5, vcpu.r6, vcpu.r7, vcpu.stop_flag, "]")


print("adding instructions...")

#virtanimal.add_instruction(s, *asm.AssembleInstruction("mov_ri r0, 200").to_tuple())
#virtanimal.add_instruction(s, *asm.AssembleInstruction("mov_ri r1, 50").to_tuple())
#virtanimal.add_instruction(s, *asm.AssembleInstruction("add_rr r0, r1").to_tuple())
#virtanimal.add_instruction(s, *asm.AssembleInstruction("mov_ar r0").to_tuple())
virtanimal.add_instruction(s, *asm.AssembleInstruction("detect_food").to_tuple())
virtanimal.animal_set_instruction_seq(a, 0, s)
virtanimal.animal_run_tick(a, field_callback, fld, fp)
virtanimal.animal_get_vcpu(a, 0, c)
print_vcpu(c)


#virtanimal.animal_set_instruction_seq(a, 0, s)

#virtanimal.animal_run_tick(a, f2, field0, fp)


#a = [0, 1, 0, 0, 0, 0, 0, 1]
#print()


    
#def run_until_stop_and_print(vcpu, sequence, unitvarstruct):
    #print(vcpu.ip, "    ", vcpu.accumulator, "[", vcpu.r0, vcpu.r1, vcpu.r2, vcpu.r3, vcpu.r4, vcpu.r5, vcpu.r6, vcpu.r7, vcpu.stop_flag, "]")
#    print(virtanimal.vcpu_get_state(vcpu))
#    virtanimal.vcpu_run(vcpu, sequence, unitvarstruct, 0)
    #print(vcpu.ip, "    ", vcpu.accumulator, "[", vcpu.r0, vcpu.r1, vcpu.r2, vcpu.r3, vcpu.r4, vcpu.r5, vcpu.r6, vcpu.r7, vcpu.stop_flag, "]")
#    print(virtanimal.vcpu_get_state(vcpu))


#run_until_stop_and_print(c, s, u)
