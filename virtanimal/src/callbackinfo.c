#include <Python.h>
#include <stdio.h>
#include "callbackinfo.h"
#include "fieldpart.h"
#include "fieldpart_repr.h"

int execute_callback(CallBackInfo * info, int obj_type, int obj_subtype, int x, int y, int direction, int shape, int distance, int fill_flags, FieldPart * fp)
{
    FieldPart_Repr * fieldpartrepr = (FieldPart_Repr *) info->cb_fieldpart;
    
    //printf("Creating arglist\n");
    PyObject * arglist = Py_BuildValue("(OiiiiiiiiO)", info->cb_argument, obj_type, obj_subtype, x, y, direction, shape, distance, fill_flags, info->cb_fieldpart);
    //printf("Arglist = %p\n", arglist);
    
    
    //printf("Calling cb_func\n");
    PyObject * result = PyObject_CallObject(info->cb_function, arglist);
    if (result)
    {
        memcpy(fp, &fieldpartrepr->fieldpart, sizeof(FieldPart));
        //printf("Result = %p\n", result);
        //printf("Releasing result\n");    
        Py_XDECREF(result);
    }
    else
        printf("Result = null\n");
    
    //printf("Releasing arglist\n");
    Py_XDECREF(arglist);
}
