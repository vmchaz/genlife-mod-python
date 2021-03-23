#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import time

# пути до модуля virtanimal
#sys.path.append('.')
#sys.path.append('lib/')
#sys.path.append('.')
#sys.path.append('../')
#sys.path.append('../../')
sys.path.append('./virtanimal/lib')

import virtanimal


class Field:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.size = self.width * self.height
        self.field = [None] * self.size
        
    def get_line(self, start_x, l, y):
        if (y < 0) or (y >= self.height):
            return [None] * l
        else:
            if (start_x >= 0) and (start_x + l < self.width):
                i1 = self.width * y + start_x
                return self.field[i1:i1+l]
                
            if (start_x < 0) and (start_x + l > 0) and (start_x + l <= self.width):
                i1 = self.width * y
                return [None] * (-start_x) + self.field[i1:i1 + start_x + l]
                
            if (start_x >= 0) and (start_x + l > self.width):
                i1 = self.width * y
                return self.field[i1 + start_x:i1 + self.width] + [None] * (start_x + l - self.width)
                
            if (start_x < 0) and (start_x + l > self.width):
                i1 = self.width * y
                return [None] * (-start_x) + self.field[i1:i1+self.width] + [None] * (start_x + l - self.width)

    def set_item(self, x, y, item):
        if (x >= 0) and (x < self.width) and (y >= 0) and (y < self.height):
            self.field[self.width * y + x] = item
            
    def get_item(self, x, y):
        if (x >= 0) and (x < self.width) and (y >= 0) and (y < self.height):
            return self.field[self.width * y + x]
        return None


def f1():
    print("f1")
    

def field_callback(field, obj_type, obj_subtype, x, y, direction, shape, distance, fill_flags, fieldpart):
    print("f2")
    print(obj_type, obj_subtype, x, y, direction, shape, distance, fill_flags);
    print("field:", type(field))
    print("fieldpart:", type(fieldpart))
    fieldpart.f_forward = 1
    fieldpart.f_back = 1
    fieldpart.flags_filled = 1
    


fp = virtanimal.FieldPart()
print(type(fp), dir(fp))

fld1 = Field(10, 10)
for i in range(10):
    for j in range(10):
        fld1.set_item(i, j, i*100+j)
        
l1 = fld1.get_line(-5, 20, 0)
print(l1)
exit()
 
#virtanimal.test_callback(f2, l1, "qqqq")

#print("Dir:")
#print(dir(virtanimal))

#exit()
    

c = virtanimal.VCPU(1)
u = virtanimal.UnitVarStruct(1, 1000, 0, 0, 0)
s = virtanimal.InstructionSequence(0)
s1 = virtanimal.InstructionSequence(0)

a = virtanimal.Animal()

print("adding instructions...")

virtanimal.add_instruction(s, 3, 0, 0, 200, 0, 0, 0)
virtanimal.add_instruction(s, 3, 1, 0, 50,  0, 0, 0)
virtanimal.add_instruction(s, 7, 0, 1, 0,   0, 0, 0)
virtanimal.add_instruction(s, 5, 0, 0, 0,   0, 0, 0)
virtanimal.add_instruction(s, 50, 0, 0, 0,   0, 0, 0)


virtanimal.animal_set_instruction_seq(a, 0, s)

virtanimal.animal_run_tick(a, f2, field0, fp)


#def run_and_print(vcpu, sequence, unitvarstruct):
#    virtanimal.vcpu_run(vcpu, sequence, unitvarstruct, 1)
#    print(vcpu.ip, "    ", vcpu.accumulator, "[", vcpu.r0, vcpu.r1, vcpu.r2, vcpu.r3, vcpu.r4, vcpu.r5, vcpu.r6, vcpu.r7, vcpu.stop_flag, "]")
    
#def run_until_stop_and_print(vcpu, sequence, unitvarstruct):
    #print(vcpu.ip, "    ", vcpu.accumulator, "[", vcpu.r0, vcpu.r1, vcpu.r2, vcpu.r3, vcpu.r4, vcpu.r5, vcpu.r6, vcpu.r7, vcpu.stop_flag, "]")
#    print(virtanimal.vcpu_get_state(vcpu))
#    virtanimal.vcpu_run(vcpu, sequence, unitvarstruct, 0)
    #print(vcpu.ip, "    ", vcpu.accumulator, "[", vcpu.r0, vcpu.r1, vcpu.r2, vcpu.r3, vcpu.r4, vcpu.r5, vcpu.r6, vcpu.r7, vcpu.stop_flag, "]")
#    print(virtanimal.vcpu_get_state(vcpu))


#run_until_stop_and_print(c, s, u)
