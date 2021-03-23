#ifndef _CALLBACKINFO_H_
#define _CALLBACKINFO_H_

#include <Python.h>
#include "fieldpart.h"

typedef struct {
    PyObject * cb_function;
    PyObject * cb_argument;
    PyObject * cb_fieldpart;
} CallBackInfo;

int execute_callback(CallBackInfo * info, int obj_type, int obj_subtype, int x, int y, int direction, int shape, int distance, int fill_flags, FieldPart * fp);

#endif
