//#include "test.h"
#include <stdio.h>
#include <Python.h>
#include "fieldobjecttypes.h"
#include "hazard_repr.h"

// Создание структуры
static PyObject * Hazard_Repr_new(PyTypeObject *type, PyObject *args, PyObject *kwds) 
{
    Hazard_Repr *self;

    self = (Hazard_Repr *)type->tp_alloc(type, 0);
    if (self != NULL) 
    {
        self->hazard.damage = 0;
    }

    return (PyObject *)self;
}


// Освобождение структуры
static void Hazard_Repr_dealloc(Hazard_Repr * self) 
{
    Py_TYPE(self)->tp_free((PyObject*)self);
}


// Инициализация структуры, заполняем её переданными значениями
static int Hazard_Repr_init(Hazard_Repr *self, PyObject *args, PyObject *kwds) 
{
    self->local_type = ftHAZARD;
    self->local_subtype = fstDEFAULT;
    self->hazard.damage = 1000;
    return 0;
}


// Описываем аттрибуты из которых состоит структура
static PyMemberDef Hazard_Repr_members[] = 
{
    {"local_type", T_INT, offsetof(Hazard_Repr, local_type), 0, "int"},
    {"local_subtype", T_INT, offsetof(Hazard_Repr, local_subtype), 0, "int"},
    {"damage", T_INT, offsetof(Hazard_Repr, hazard.damage), 0, "int"},
    {NULL}
};


// Описание методов стрктуры, но у классической структуры не может быть методов!
static PyMethodDef Hazard_Repr_methods[] = 
{
    {NULL}  /* Sentinel */
};


// Структура описывающая нашу структуру. Какие атрибуты, методы, конструкторы, деструкторы и т.д. и т.п.
PyTypeObject Hazard_Repr_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "testmod.Hazard_Repr",                  /* tp_name */
    sizeof(Hazard_Repr),                    /* tp_basicsize */
    0,                                  /* tp_itemsize */
    (destructor) Hazard_Repr_dealloc,       /* tp_dealloc */
    0,                                  /* tp_print */
    0,                                  /* tp_getattr */
    0,                                  /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "Hazard_Repr objects",         /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Hazard_Repr_methods,           /* tp_methods */
    Hazard_Repr_members,           /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc) Hazard_Repr_init,   /* tp_init */
    0,                         /* tp_alloc */
    Hazard_Repr_new,               /* tp_new */
};
