#ifndef _FIELDPART_REPR_H_
#define _FIELDPART_REPR_H_

#include <Python.h>
    
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#include <structmember.h>
#include "fieldpart.h"


#ifdef	__cplusplus
extern "C" {
#endif

extern PyTypeObject FieldPart_Repr_Type;

#ifdef	__cplusplus
}
#endif

typedef struct {
    PyObject_HEAD // Макрос объявления нового типа, объекта фиксированного размера
    FieldPart fieldpart;
    //UnitVarStruct unitvarstruct;
    
} FieldPart_Repr;

#endif
