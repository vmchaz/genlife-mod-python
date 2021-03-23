/*
 * gcc -fPIC -shared -o libtest.so test.c
 */

#include <Python.h>


#include "test.h"

#include "vcpu_repr.h"
#include "instructionsequence_repr.h"
#include "unitvarstruct_repr.h"
#include "animal_repr.h"
#include "fieldpart_repr.h"

#include "advanced_func.h"



// Список функций модуля
static PyMethodDef methods[] = {
    {"get_instruction", testmod_func_get_instruction, METH_VARARGS , "Function get_instruction"},
    {"set_instruction", testmod_func_set_instruction, METH_VARARGS, "Function set_instruction"},
    {"add_instruction", testmod_func_add_instruction, METH_VARARGS, "Function add_instruction"},
    
    {"animal_get_instruction_seq", testmod_func_animal_get_instruction_seq, METH_VARARGS , "Function animal_get_instruction_seq"},
    {"animal_set_instruction_seq", testmod_func_animal_set_instruction_seq, METH_VARARGS , "Function animal_set_instruction_seq"},
    
    {"animal_run_tick", testmod_animal_run_tick, METH_VARARGS, "Function animal_run_tick"},
    
    {"vcpu_run", testmod_vcpu_run, METH_VARARGS, "Function vcpu_step"},
    {"vcpu_get_state", testmod_vcpu_get_state, METH_VARARGS, "Function vcpu_get_state"},
    {"vcpu_reset", testmod_vcpu_reset, METH_VARARGS, "Function vcpu_reset"},
    
    {"test_callback", testmod_callback, METH_VARARGS, "Function test+callback"},

    
    {NULL, NULL, 0, NULL}
};

// Описание модуля
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "virtanimal", "Test module", -1, methods
};

// Инициализация модуля
PyMODINIT_FUNC PyInit_virtanimal(void)
{
    PyObject *mod = PyModule_Create(&module);

    // Добавляем глобальные переменные
    
    PyModule_AddObject(mod, "ModuleVarA", PyLong_FromLong(ModuleVarA)); // int
    PyModule_AddObject(mod, "ModuleVarB", PyFloat_FromDouble(ModuleVarB)); // double
    PyModule_AddObject(mod, "ModuleVarC", Py_BuildValue("b", ModuleVarC)); // char

    // Добавляем структуру
    
    
    // Завершение инициализации структуры
    if (PyType_Ready(&VCPU_Repr_Type) < 0)
        return NULL;
    if (PyType_Ready(&InstructionSequence_Repr_Type) < 0)
        return NULL;
    if (PyType_Ready(&UnitVarStruct_Repr_Type) < 0)
        return NULL;
    if (PyType_Ready(&Animal_Repr_Type) < 0)
        return NULL;
    if (PyType_Ready(&FieldPart_Repr_Type) < 0)
        return NULL;

    
    Py_INCREF(&VCPU_Repr_Type);
    Py_INCREF(&InstructionSequence_Repr_Type);
    Py_INCREF(&UnitVarStruct_Repr_Type);
    Py_INCREF(&Animal_Repr_Type);
    Py_INCREF(&FieldPart_Repr_Type);
    
    PyModule_AddObject(mod, "VCPU", (PyObject *) &VCPU_Repr_Type);
    PyModule_AddObject(mod, "InstructionSequence", (PyObject *) &InstructionSequence_Repr_Type);
    PyModule_AddObject(mod, "UnitVarStruct", (PyObject *) &UnitVarStruct_Repr_Type);
    PyModule_AddObject(mod, "Animal", (PyObject *) &Animal_Repr_Type);
    PyModule_AddObject(mod, "FieldPart", (PyObject *) &FieldPart_Repr_Type);
    
    return mod;
}

/**
 * Тестовые функции, тестовые переменные.
 */

int ModuleVarA = 5;
double ModuleVarB = 5.12345;
char ModuleVarC = 'X'; // 88

