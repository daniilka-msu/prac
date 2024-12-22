import asyncio
from asyncio import Event
from math import ceil
import random

def merge_lists(A1, start, middle, finish):
    merged = []
    i, j = start, middle
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            merged.append(A1[i])
            i += 1
        else:
            merged.append(A1[j])
            j += 1
    merged.extend(A1[i:middle])
    merged.extend(A1[j:finish])
    return merged

async def merge(A1, A2, start, middle, finish, event_in1: Event, event_in2: Event, event_out: Event):
    if event_in1:
        await event_in1.wait()
    if event_in2:
        await event_in2.wait()
    
    i1, i2 = start, middle
    for i in range(start, finish):
        if i1 < middle and i2 < finish:
            if A1[i1] < A1[i2]:
                A2[i] = A1[i1]
                i1 += 1
            else:
                A2[i] = A1[i2]
                i2 += 1
        else:
            break

    i1 = i1 if i1 < middle else i2
    for i in range(i, finish):
        A2[i] = A1[i1]
        i1 += 1 
    for i in range(start, finish):
        A1[i] = A2[i]

    event_out.set()

async def mtasks(Ain: list):
    events = [None] * len(Ain)
    A = Ain.copy()
    B = A.copy()
    l = 1
    tasks = []
    while l < len(A):
        newevents = []
        num_pairs = (len(A) + 2 * l - 1) // (2 * l)
        if len(events) < 2 * num_pairs:
            events.extend([None] * (2 * num_pairs - len(events)))
        for i in range(num_pairs):
            start = 2 * i * l
            middle = min((2 * i + 1) * l, len(A))
            finish = min((2 * i + 2) * l, len(A))
            newevents.append(Event())
            tasks.append(merge(A, B, start, middle, finish, events[2 * i], events[2 * i + 1], newevents[-1]))
        events = newevents
        l *= 2
    return tasks, B

import sys
exec(sys.stdin.read())
