//#include "test.h"
#include <Python.h>
#include "vcpu.h"
#include "vcpu_repr.h"
#include "unitvarstruct.h"
#include "unitvarstruct_repr.h"
#include "instructionsequence.h"
#include "instructionsequence_repr.h"
#include "animal.h"
#include "animal_repr.h"

#include "callbackinfo.h"


PyObject * testmod_func_get_instruction_count(PyObject *self, PyObject *args) 
{
    InstructionSequence_Repr * sequence_r;
    int ct;
    
    if (!PyArg_ParseTuple(args, "O", &sequence_r))
        Py_RETURN_NONE;
        
    ct = sequence_r->sequence.count;
        
    return Py_BuildValue("i", ct);
}


PyObject * testmod_func_get_instruction(PyObject *self, PyObject *args) 
{
    InstructionSequence_Repr * sequence_r;
    int idx;
    int cmd;
    int reg_dest;
    int reg_src;
    int imm;
    int flags_allow;
    int flags_deny;
    int flags_target;
    
    // Получаем структуру из Python
    if (!PyArg_ParseTuple(args, "Oi", &sequence_r, &idx))
        Py_RETURN_NONE;
        
    if ((idx < 0) || (idx >= sequence_r->sequence.count))
        Py_RETURN_NONE;
    
    cmd = sequence_r->sequence.instructions[idx].cmd;
    reg_dest = sequence_r->sequence.instructions[idx].reg_dest;
    reg_src = sequence_r->sequence.instructions[idx].reg_src;
    imm = sequence_r->sequence.instructions[idx].imm;
    
    flags_allow = sequence_r->sequence.instructions[idx].flags_allow;
    flags_deny = sequence_r->sequence.instructions[idx].flags_deny;
    flags_target = sequence_r->sequence.instructions[idx].flags_target;
    
    return Py_BuildValue("iiiiiii", cmd, reg_dest, reg_src, imm, flags_allow, flags_deny, flags_target);
}


PyObject * testmod_func_set_instruction(PyObject *self, PyObject *args)
{
    InstructionSequence_Repr * sequence_r;
    int idx;
    int cmd;
    int reg_dest;
    int reg_src;
    int imm;
    int flags_allow;
    int flags_deny;
    int flags_target;
    
    memset(&reg_dest, 0, sizeof(reg_dest));
    memset(&reg_src, 0, sizeof(reg_src));
    memset(&imm, 0, sizeof(imm));
    memset(&flags_allow, 0, sizeof(flags_allow));
    memset(&flags_deny, 0, sizeof(flags_deny));
    memset(&flags_target, 0, sizeof(flags_target));
    
    // Получаем структуру из Python
    if (!PyArg_ParseTuple(args, "Oiiiiiiii", &sequence_r, &idx, &cmd, &reg_dest, &reg_src, &imm, &flags_allow, &flags_deny, &flags_target)) // O - объект данных
        Py_RETURN_NONE;
        
    InstructionSequence * sequence = &sequence_r->sequence;
        
    if ((idx < 0) || (idx >= sequence->count))
        Py_RETURN_NONE;
    
    sequence->instructions[idx].cmd = cmd;
    sequence->instructions[idx].reg_dest = reg_dest;
    sequence->instructions[idx].reg_src = reg_src;
    sequence->instructions[idx].imm = imm;
    
    sequence->instructions[idx].flags_allow = flags_allow;
    sequence->instructions[idx].flags_deny = flags_deny;
    sequence->instructions[idx].flags_target = flags_target;
    
    Py_RETURN_NONE;
}

PyObject * testmod_func_add_instruction(PyObject *self, PyObject *args)
{
    InstructionSequence_Repr * sequence_r;
    int idx;
    int cmd;
    int reg_dest;
    int reg_src;
    int imm;
    int flags_allow;
    int flags_deny;
    int flags_target;
    
    memset(&reg_dest, 0, sizeof(reg_dest));
    memset(&reg_src, 0, sizeof(reg_src));
    memset(&imm, 0, sizeof(imm));
    memset(&flags_allow, 0, sizeof(flags_allow));
    memset(&flags_deny, 0, sizeof(flags_deny));
    memset(&flags_target, 0, sizeof(flags_target));
    
    static char *kwlist[] = {"sequence", "cmd", "reg_dest", "reg_src", "flags_allow", "flags_deny", "flags_target", NULL};
    
    // Получаем структуру из Python
    if (!PyArg_ParseTuple(args, "Oiiiiiii", &sequence_r, &cmd, &reg_dest, &reg_src, &imm, &flags_allow, &flags_deny, &flags_target))
        Py_RETURN_NONE;
        
    InstructionSequence * sequence = &sequence_r->sequence;
        
    idx = sequence->count;
    
    if (idx >= 256)
        Py_RETURN_NONE;
    
    sequence->instructions[idx].cmd = cmd;
    sequence->instructions[idx].reg_dest = reg_dest;
    sequence->instructions[idx].reg_src = reg_src;
    sequence->instructions[idx].imm = imm;
    
    sequence->instructions[idx].flags_allow = flags_allow;
    sequence->instructions[idx].flags_deny = flags_deny;
    sequence->instructions[idx].flags_target = flags_target;
    
    sequence->count += 1;
    
    Py_RETURN_NONE;
}



PyObject * testmod_func_animal_get_instruction_seq(PyObject * self, PyObject *args)
{
    Animal_Repr * animal_r = NULL;
    InstructionSequence_Repr * sequence_r = NULL;
    int idx;
    
    if (! PyArg_ParseTuple(args, "OiO", &animal_r, &idx, &sequence_r))
        Py_RETURN_NONE;
        
    Animal * animal = &animal_r->animal;
    if ((idx < 0) || (idx >= animal->thread_count))
        Py_RETURN_NONE;
        
    InstructionSequence * sequence_dest = &sequence_r->sequence;
    InstructionSequence * sequence_src = &animal->sequences[idx];
    memcpy(sequence_dest, sequence_src, sizeof(InstructionSequence));
    
    Py_RETURN_NONE;
}

PyObject * testmod_func_animal_set_instruction_seq(PyObject * self, PyObject *args)
{
    Animal_Repr * animal_r = NULL;
    InstructionSequence_Repr * sequence_r = NULL;
    int idx;
    if (! PyArg_ParseTuple(args, "OiO", &animal_r, &idx, &sequence_r))
        Py_RETURN_NONE;
        
    Animal * animal = &animal_r->animal;
    if ((idx < 0) || (idx >= animal->thread_count))
        Py_RETURN_NONE;
    
    
    InstructionSequence * sequence_src = &sequence_r->sequence;
    InstructionSequence * sequence_dest = &animal->sequences[idx];
    
    memcpy(sequence_dest, sequence_src, sizeof(InstructionSequence));
    Py_RETURN_NONE;
}

PyObject * testmod_func_animal_get_vcpu(PyObject * self, PyObject *args)
{
    Animal_Repr * animal_r = NULL;
    VCPU_Repr * vcpu_r = NULL;
    int idx;
    
    if (! PyArg_ParseTuple(args, "OiO", &animal_r, &idx, &vcpu_r))
        Py_RETURN_NONE;
        
    Animal * animal = &animal_r->animal;
    if ((idx < 0) || (idx >= animal->thread_count))
        Py_RETURN_NONE;
        
    memcpy(&vcpu_r->vcpu, &animal->vcpus[idx], sizeof(VCPU));
    
    Py_RETURN_NONE;
}

PyObject * testmod_func_animal_set_vcpu(PyObject * self, PyObject *args)
{
    Animal_Repr * animal_r = NULL;
    VCPU_Repr * vcpu_r = NULL;
    int idx;
    
    if (! PyArg_ParseTuple(args, "OiO", &animal_r, &idx, &vcpu_r))
        Py_RETURN_NONE;
        
    Animal * animal = &animal_r->animal;
    if ((idx < 0) || (idx >= animal->thread_count))
        Py_RETURN_NONE;
        
    memcpy(&animal->vcpus[idx], &vcpu_r->vcpu, sizeof(VCPU));
    
    Py_RETURN_NONE;
}



PyObject * testmod_animal_run_tick(PyObject *self, PyObject *args)
{
    Animal_Repr * animal_r = NULL;
    PyObject * cb_func = NULL;
    PyObject * cb_argument = NULL;
    PyObject * cb_fieldpart = NULL;
        
    int id;
    int energy;
    int x;
    int y;
    int direction;
    int maxsteps = 1;
    

    if (! PyArg_ParseTuple(args, "OOOO", &animal_r, &cb_func, &cb_argument, &cb_fieldpart))
        Py_RETURN_NONE;
        
    CallBackInfo ci;
    
    ci.cb_function = cb_func;
    ci.cb_argument = cb_argument;
    ci.cb_fieldpart = cb_fieldpart;
    
    Py_XINCREF(cb_func);
    Py_XINCREF(cb_argument);
    Py_XINCREF(cb_fieldpart);
    //printf("cb_func=%p cb_arg=%p cb_fp=%p\n", cb_func, cb_argument, cb_fieldpart);
    
    Animal * animal = &animal_r->animal;
    
    animal_run_tick(animal, &ci);
    
    Py_XDECREF(cb_func);
    Py_XDECREF(cb_argument);
    Py_XDECREF(cb_fieldpart);
    
    Py_RETURN_NONE;
}



PyObject * testmod_vcpu_run(PyObject *self, PyObject *args) 
{
    VCPU_Repr * vcpu_repr = NULL;
    InstructionSequence_Repr * sequence_repr = NULL;
    UnitVarStruct_Repr * u_repr = NULL;
    
    static char *kwlist[] = {"vcpu", "instructionsequence", "unitvarstruct", NULL};
    
    int id;
    int energy;
    int x;
    int y;
    int direction;
    int maxsteps = 1;
    

    if (! PyArg_ParseTuple(args, "OOOi", &vcpu_repr, &sequence_repr, &u_repr, &maxsteps))
        Py_RETURN_NONE;
    
    
    VCPU * vcpu = &vcpu_repr->vcpu;
    InstructionSequence * sequence = &sequence_repr->sequence;
    UnitVarStruct * u = &u_repr->unitvarstruct;
    int res = vcpu_run(vcpu, sequence, u, NULL, false, maxsteps);
    
    return Py_BuildValue("i", res);
}

PyObject * testmod_vcpu_reset(PyObject *self, PyObject *args) 
{
    VCPU_Repr * vcpu_repr = NULL;

    if (! PyArg_ParseTuple(args, "O", &vcpu_repr))
        Py_RETURN_NONE;
    
    
    vcpu_reset(&vcpu_repr->vcpu);
    
    Py_RETURN_NONE;
}

PyObject * testmod_vcpu_get_state(PyObject *self, PyObject *args) 
{
    VCPU_Repr * vcpu_repr = NULL;
    
     
    int id;
    int energy;
    int x;
    int y;
    int direction;
    int maxsteps = 1;
    

    if (! PyArg_ParseTuple(args, "O", &vcpu_repr))
        Py_RETURN_NONE;
        
    VCPU * vcpu = &vcpu_repr->vcpu;
    char buf[2000];
    char f[1000] = "VCPU id:%d ip:%d acc:%d r0:%d r1:%d r2:%d r3:%d r4:%d r5:%d r6:%d r7:%d r8:%d r9:%d r10:%d r11:%d r12:%d r13:%d r14:%d r15:%d flags:%x stop_flag:%d";
    snprintf(buf, sizeof(buf), f, vcpu->id, vcpu->ip, vcpu->accumulator, vcpu->registers[0], vcpu->registers[1], vcpu->registers[2], vcpu->registers[3],
        vcpu->registers[4], vcpu->registers[5], vcpu->registers[6], vcpu->registers[7],
        vcpu->registers[8], vcpu->registers[9], vcpu->registers[10], vcpu->registers[11],
        vcpu->registers[12], vcpu->registers[13], vcpu->registers[14], vcpu->registers[15],
        vcpu->flags, vcpu->stop_flag);
    
    return Py_BuildValue("s", buf);
}


PyObject * testmod_callback(PyObject *self, PyObject *args) 
{
    PyObject * cb_func = NULL;    
    PyObject * cb_argument = NULL;
    PyObject * cb_buffer = NULL;
    char * s0;

    if (! PyArg_ParseTuple(args, "OOO", &cb_func, &cb_argument, &cb_buffer))
        Py_RETURN_NONE;
        
    if (!PyCallable_Check(cb_func)) 
    {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }
    
    printf("String: %s cb_func: %p\n", s0, cb_func);
    
    printf("cb_argument = %p\n", cb_argument);
    
    printf("Increasing refs to cb_func\n");
    Py_XINCREF(cb_func);
    
    printf("Increasing refs to cb_argument\n");
    Py_XINCREF(cb_argument);
    
    printf("Increasing refs to cb_argument\n");
    Py_XINCREF(cb_buffer);    
    
    
    
    PyObject *arglist;
    PyObject *result;
    
    printf("Creating arglist\n");
    int n = 12345;
    arglist = Py_BuildValue("(OO)", cb_argument, cb_buffer);
    printf("Arglist = %p\n", arglist);
    
    
    printf("Calling cb_func\n");
    result = PyObject_CallObject(cb_func, arglist);
    if (result)
    {
        printf("Result = %p\n", result);
        printf("Releasing result\n");    
        Py_XDECREF(result);
    }
    else
        printf("Result = null\n");
    
    printf("Releasing arglist\n");
    Py_XDECREF(arglist);

    //if PyArg_ParseTuple
    
    printf("Decreasing refs to cb_func\n");
    Py_XDECREF(cb_func);
        
    Py_XDECREF(cb_argument);
    printf("Decreasing refs to cb_argument\n");
    
    Py_XDECREF(cb_buffer);
    printf("Decreasing refs to cb_buffer\n");

    Py_RETURN_NONE;
}
