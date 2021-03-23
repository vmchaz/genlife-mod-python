#include <Python.h>
#include "fieldobjecttypes.h"
#include "obstacle_repr.h"

// Создание структуры
static PyObject * Obstacle_Repr_new(PyTypeObject *type, PyObject *args, PyObject *kwds) 
{
    Obstacle_Repr *self;

    self = (Obstacle_Repr *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->obstacle.obstacle_level = 0;
        //self->count = 0;
        //memset(&self->sequence, 0, sizeof(self->sequence));
    }    

    return (PyObject *)self;
}


// Освобождение структуры
static void Obstacle_Repr_dealloc(Obstacle_Repr * self) 
{
    Py_TYPE(self)->tp_free((PyObject*)self);
}


// Инициализация структуры, заполняем её переданными значениями
static int Obstacle_Repr_init(Obstacle_Repr *self, PyObject *args, PyObject *kwds) {
    self->local_type = ftOBSTACLE;
    self->local_subtype = 1;
    self->obstacle.obstacle_level = 1;
    //static char *kwlist[] = {"val1", "val2", "val3", NULL};
    //static char *kwlist[] = {"count", NULL};
    
    //int count;

    //if (! PyArg_ParseTupleAndKeywords(args, kwds, "i", kwlist, &count))
    //    return -1;
        
    //self->sequence.count = count;

    return 0;
}


// Описываем аттрибуты из которых состоит структура
static PyMemberDef Obstacle_Repr_members[] = 
{
    {"local_type", T_INT, offsetof(Obstacle_Repr, local_type), 0, "int"},
    {"local_subtype", T_INT, offsetof(Obstacle_Repr, local_subtype), 0, "int"},
    {"obstacle_level", T_INT, offsetof(Obstacle_Repr, obstacle.obstacle_level), 0, "int"},    
    {NULL}
};


// Описание методов стрктуры, но у классической структуры не может быть методов!
static PyMethodDef Obstacle_Repr_methods[] = 
{
    {NULL}  /* Sentinel */
};


// Структура описывающая нашу структуру. Какие атрибуты, методы, конструкторы, деструкторы и т.д. и т.п.
PyTypeObject Obstacle_Repr_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "testmod.Obstacle_Repr",                  /* tp_name */
    sizeof(Obstacle_Repr),                    /* tp_basicsize */
    0,                                  /* tp_itemsize */
    (destructor) Obstacle_Repr_dealloc,       /* tp_dealloc */
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
    "Obstacle_Repr objects",         /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Obstacle_Repr_methods,           /* tp_methods */
    Obstacle_Repr_members,           /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc) Obstacle_Repr_init,   /* tp_init */
    0,                         /* tp_alloc */
    Obstacle_Repr_new,               /* tp_new */
};
