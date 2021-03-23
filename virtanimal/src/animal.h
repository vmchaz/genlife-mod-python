#ifndef _ANIMAL_H_
#define _ANIMAL_H_

#include <stdbool.h>
#include "vcpu.h"
#include "callbackinfo.h"
#include "instructionsequence.h"
#include "unitvarstruct.h"

typedef struct {
    int id;
    int next_thread;
    int thread_count;
    int one_thread_per_tick;
    int stop_on_action;
    int maxsteps;
    VCPU vcpus[16];
    InstructionSequence sequences[16];
    UnitVarStruct unitvarstruct;
} Animal;

void animal_init(Animal * animal);
void animal_run_tick(Animal * animal, CallBackInfo * cb);
void animal_run_tick_adv(Animal * animal, CallBackInfo * cb, bool stop_on_action, bool one_thread_per_tick, int maxsteps);

#endif
