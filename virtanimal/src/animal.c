#include "animal.h"
#include "callbackinfo.h"
#include <stdbool.h>

void animal_init(Animal * animal)
{
    memset(animal, 0, sizeof(Animal));
}

void animal_run_tick(Animal * animal, CallBackInfo * cb)
{
    animal_run_tick_adv(animal, cb, animal->stop_on_action==1, animal->one_thread_per_tick==1, animal->maxsteps);
}

void animal_run_tick_adv(Animal * animal, CallBackInfo * cb, bool stop_on_action, bool one_thread_per_tick, int maxsteps)
{
    if (animal->thread_count == 0)
        return;
        
    if (one_thread_per_tick)
    {
        int t = animal->next_thread;
        vcpu_reset(&animal->vcpus[t]);
        vcpu_run(&animal->vcpus[t], &animal->sequences[t], &animal->unitvarstruct, cb, stop_on_action, maxsteps);
        animal->next_thread = (animal->next_thread + 1) % animal->thread_count;
    }
    else
    {
        for(int i=0; i<animal->thread_count; i++)
        {
            vcpu_reset(&animal->vcpus[i]);
            vcpu_run(&animal->vcpus[i], &animal->sequences[i], &animal->unitvarstruct, cb, stop_on_action, maxsteps);
        }
    }
}
