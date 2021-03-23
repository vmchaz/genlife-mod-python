//#include "test.h"
#include <Python.h>
#include "fieldpart_repr.h"
#include "actions.h"

// Создание структуры
static PyObject * FieldPart_Repr_new(PyTypeObject *type, PyObject *args, PyObject *kwds) 
{
    FieldPart_Repr *self;

    self = (FieldPart_Repr *)type->tp_alloc(type, 0);
    if (self != NULL) 
    {
        for (int i=0; i<8; i++)
            self->fieldpart.lines[i] = 0;
            self->fieldpart.f_forward = 0;
            self->fieldpart.f_right = 0;
            self->fieldpart.f_back = 0;
            self->fieldpart.f_left = 0;
    }

    return (PyObject *)self;
}


// Освобождение структуры
static void FieldPart_Repr_dealloc(FieldPart_Repr * self) 
{
    Py_TYPE(self)->tp_free((PyObject*)self);
}


// Инициализация структуры, заполняем её переданными значениями
static int FieldPart_Repr_init(FieldPart_Repr *self, PyObject *args, PyObject *kwds) {
    //static char *kwlist[] = {"val1", "val2", "val3", NULL};
    //static char *kwlist[] = {"id", "energy", "x", "y", "direction", NULL};
    
    //int id;
    //int energy;
    //int x;
    //int y;
    //int direction = 0;

    //if (! PyArg_ParseTupleAndKeywords(args, kwds, "iiiii", kwlist, &id, &energy, &x, &y, &direction))
    //    return -1;
        
    for (int i=0; i<8; i++)
        self->fieldpart.lines[i] = 0;
        

    return 0;
}


// Описываем аттрибуты из которых состоит структура
static PyMemberDef FieldPart_Repr_members[] = 
{
    {"line0", T_INT, offsetof(FieldPart_Repr, fieldpart.lines[0]), 0, "int"},
    {"line1", T_INT, offsetof(FieldPart_Repr, fieldpart.lines[1]), 0, "int"},
    {"line2", T_INT, offsetof(FieldPart_Repr, fieldpart.lines[2]), 0, "int"},
    {"line3", T_INT, offsetof(FieldPart_Repr, fieldpart.lines[3]), 0, "int"},
    {"line4", T_INT, offsetof(FieldPart_Repr, fieldpart.lines[4]), 0, "int"},
    {"line5", T_INT, offsetof(FieldPart_Repr, fieldpart.lines[5]), 0, "int"},
    {"line6", T_INT, offsetof(FieldPart_Repr, fieldpart.lines[6]), 0, "int"},
    {"line7", T_INT, offsetof(FieldPart_Repr, fieldpart.lines[7]), 0, "int"},
    {"flags_filled", T_INT, offsetof(FieldPart_Repr, fieldpart.flags_filled), 0, "int"},
    {"f_forward", T_INT, offsetof(FieldPart_Repr, fieldpart.f_forward), 0, "int"},
    {"f_right", T_INT, offsetof(FieldPart_Repr, fieldpart.f_right), 0, "int"},
    {"f_back", T_INT, offsetof(FieldPart_Repr, fieldpart.f_back), 0, "int"},
    {"f_left", T_INT, offsetof(FieldPart_Repr, fieldpart.f_left), 0, "int"},
    {NULL}
};


// Описание методов стрктуры, но у классической структуры не может быть методов!
static PyMethodDef FieldPart_Repr_methods[] = 
{
    {NULL}  /* Sentinel */
};


// Структура описывающая нашу структуру. Какие атрибуты, методы, конструкторы, деструкторы и т.д. и т.п.
PyTypeObject FieldPart_Repr_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "virtanimal.FieldPart_Repr",                  /* tp_name */
    sizeof(FieldPart_Repr),                    /* tp_basicsize */
    0,                                  /* tp_itemsize */
    (destructor) FieldPart_Repr_dealloc,       /* tp_dealloc */
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
    "FieldPart_Repr objects",         /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    FieldPart_Repr_methods,           /* tp_methods */
    FieldPart_Repr_members,           /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc) FieldPart_Repr_init,   /* tp_init */
    0,                         /* tp_alloc */
    FieldPart_Repr_new,               /* tp_new */
};
