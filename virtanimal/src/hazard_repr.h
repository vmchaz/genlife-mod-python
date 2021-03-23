#ifndef _HAZARD_REPR_H_
#define _HAZARD_REPR_H_

#include <Python.h>
    
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#include <structmember.h>
#include "hazard.h"


#ifdef	__cplusplus
extern "C" {
#endif

extern PyTypeObject Hazard_Repr_Type;

#ifdef	__cplusplus
}
#endif

typedef struct {
    PyObject_HEAD // Макрос объявления нового типа, объекта фиксированного размера
    int local_type;
    int local_subtype;
    Hazard hazard;
} Hazard_Repr;

#endif
