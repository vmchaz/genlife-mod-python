//#include "test.h"
#include <Python.h>
#include "food_repr.h"
#include "actions.h"

// Создание структуры
static PyObject * Food_Repr_new(PyTypeObject *type, PyObject *args, PyObject *kwds) 
{
    Food_Repr *self;

    self = (Food_Repr *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->food.energy = 0;
    }

    return (PyObject *)self;
}


// Освобождение структуры
static void Food_Repr_dealloc(Food_Repr * self) 
{
    Py_TYPE(self)->tp_free((PyObject*)self);
}


// Инициализация структуры, заполняем её переданными значениями
static int Food_Repr_init(Food_Repr *self, PyObject *args, PyObject *kwds) {
    //static char *kwlist[] = {"val1", "val2", "val3", NULL};
    //static char *kwlist[] = {"id", "energy", "x", "y", "direction", NULL};
    
    int energy;

    if (! PyArg_ParseTuple(args, "i", &energy))
        return -1;
        
    //self->Food.x = x;
    //self->Food.y = y;
    self->food.energy = energy;
    //self->Food.direction = direction;
    //self->Food.action = actSTAY;
    //self->Food.action_p = 0;
    //self->Food.use_action_p = 0;

    return 0;
}


// Описываем аттрибуты из которых состоит структура
static PyMemberDef Food_Repr_members[] = 
{
    {"energy", T_INT, offsetof(Food_Repr, food.energy), 0, "int"},
    {"local_type", T_INT, offsetof(Food_Repr, local_type), 0, "int"},
    {"local_subtype", T_INT, offsetof(Food_Repr, local_subtype), 0, "int"},        
    {NULL}
};


// Описание методов стрктуры, но у классической структуры не может быть методов!
static PyMethodDef Food_Repr_methods[] = 
{
    {NULL}  /* Sentinel */
};


// Структура описывающая нашу структуру. Какие атрибуты, методы, конструкторы, деструкторы и т.д. и т.п.
PyTypeObject Food_Repr_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "testmod.Food_Repr",                  /* tp_name */
    sizeof(Food_Repr),                    /* tp_basicsize */
    0,                                  /* tp_itemsize */
    (destructor) Food_Repr_dealloc,       /* tp_dealloc */
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
    "Food_Repr objects",         /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Food_Repr_methods,           /* tp_methods */
    Food_Repr_members,           /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc) Food_Repr_init,   /* tp_init */
    0,                         /* tp_alloc */
    Food_Repr_new,               /* tp_new */
};
