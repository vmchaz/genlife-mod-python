#include "test.h"
#include "vcpu.h"

// Освобождение структуры
static void
VCPU_dealloc(VCPU* self) {
    Py_TYPE(self)->tp_free((PyObject*)self);
}

// Создание структуры
static PyObject *
VCPU_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    VCPU *self;

    self = (VCPU *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->val1 = 0;
        self->val2 = 0.0;
        self->val3 = 0;
    }

    return (PyObject *)self;
}

// Инициализация структуры, заполняем её переданными значениями
static int
VCPU_init(VCPU *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"val1", "val2", "val3", NULL};

    if (! PyArg_ParseTupleAndKeywords(args, kwds, "|idb", kwlist, &self->val1, &self->val2, &self->val3))
        return -1;

    return 0;
}

// Описываем аттрибуты из которых состоит структура
static PyMemberDef VCPU_members[] = {
    {"r0", T_INT, offsetof(VCPU, r0), 0, "int"},
    {"r1", T_INT, offsetof(VCPU, r1), 0, "int"},
    {"r2", T_INT, offsetof(VCPU, r2), 0, "int"},
    {"r3", T_INT, offsetof(VCPU, r3), 0, "int"},
    
    {"r4", T_INT, offsetof(VCPU, r4), 0, "int"},
    {"r5", T_INT, offsetof(VCPU, r5), 0, "int"},
    {"r6", T_INT, offsetof(VCPU, r6), 0, "int"},
    {"r7", T_INT, offsetof(VCPU, r7), 0, "int"},
    
    {"r8", T_INT, offsetof(VCPU, r8), 0, "int"},
    {"r9", T_INT, offsetof(VCPU, r9), 0, "int"},
    {"r10", T_INT, offsetof(VCPU, r10), 0, "int"},
    {"r11", T_INT, offsetof(VCPU, r11), 0, "int"},
    
    {"r12", T_INT, offsetof(VCPU, r12), 0, "int"},
    {"r13", T_INT, offsetof(VCPU, r13), 0, "int"},
    {"r14", T_INT, offsetof(VCPU, r14), 0, "int"},
    {"r15", T_INT, offsetof(VCPU, r15), 0, "int"},
    
    {"ip", T_DOUBLE, offsetof(VCPU, ip), 0, "int"},
    {"flags", T_CHAR, offsetof(VCPU, flags), 0, "int"},
    {NULL}
};

// Метод структуры, который печатает структуру
static PyObject* test_st_print(PyObject *self, PyObject *args)
{
    VCPU *st;
    
    // Получаем структуру из Python
    if (!PyArg_ParseTuple(args, "O", &st)) // O - объект данных
        Py_RETURN_NONE;
    
    printf("method: val1 - %d, val2 - %f, val3 - %d\n", st->val1++, st->val2++, st->val3++);
    Py_RETURN_NONE;
}

// Описание методов стрктуры, но у классической структуры не может быть методов!
// А здесь может!
static PyMethodDef VCPU_methods[] = {
    {"print", test_st_print, METH_VARARGS, "doc string"},
    {NULL}  /* Sentinel */
};

// Структура описывающая нашу структуру. Какие атрибуты, методы, конструкторы, деструкторы и т.д. и т.п.
PyTypeObject VCPU_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "_test.VCPU",         /* tp_name */
    sizeof(VCPU),         /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor) VCPU_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
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
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "VCPU objects",       /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    VCPU_methods,         /* tp_methods */
    VCPU_members,         /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc) VCPU_init, /* tp_init */
    0,                         /* tp_alloc */
    VCPU_new,             /* tp_new */
};
