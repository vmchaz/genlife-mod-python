#ifndef _FIELDPART_H_
#define _FIELDPART_H_

typedef struct {
    int lines[8];
    int flags_filled;
    int f_forward;
    int f_right;
    int f_back;
    int f_left;
} FieldPart;

#endif
