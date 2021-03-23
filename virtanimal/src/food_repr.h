#ifndef _FOOD_REPR_H_
#define _FOOD_REPR_H_

#include <Python.h>
    
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#include <structmember.h>
#include "food.h"


#ifdef	__cplusplus
extern "C" {
#endif

extern PyTypeObject Food_Repr_Type;

#ifdef	__cplusplus
}
#endif

typedef struct {
    PyObject_HEAD // Макрос объявления нового типа, объекта фиксированного размера
    int local_type;
    int local_subtype;
    Food food;
    
} Food_Repr;

#endif
