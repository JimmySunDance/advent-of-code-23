# Day twenty of the advent of code 2023
#
# Directed graph
from collections import deque # Doubly Ended Queue
import math

class Module:
    def __init__(self, name, m_type, outputs):
        self.name = name
        self.m_type = m_type
        self.outputs = outputs

        if m_type == '%':
            self.memory = 'off'
        else:
            self.memory = {}
    
    # representation function
    def __repr__(self):
        tps = 'type=' + self.m_type
        outs = ', outputs=' + ','.join(self.outputs)
        mems = ', memory=' + str(self.memory)
        return self.name+'{'+tps+outs+mems+'}'
    

def main() -> None:
    print('Day 20!')

    modules = {}
    broadcast_targets = []

    for line in open('data/pulse_broadcast.txt'):
        left, right = line.strip().split(' -> ')
        outputs = right.split(', ')
        if left == 'broadcaster':
            broadcast_targets = outputs
        else:
            m_type = left[0]
            name = left[1:]
            modules[name] = Module(name, m_type, outputs)
    
    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].m_type == '&':
                modules[output].memory[name] = 'low'

    ### Uncomment for part 1 answer
    low_pulse, high_pulse = 0, 0
    for _ in range(1000):
        low_pulse += 1
        # origin, target, pulse
        q = deque([('broadcaster', x, 'low') for x in broadcast_targets])

        while q:
            origin, target, pulse = q.popleft()
            if pulse == 'low':
                low_pulse += 1
            else:
                high_pulse += 1

            if target not in modules:
                continue
                
            module = modules[target]
            if module.m_type == '%':
                if pulse == 'low':
                    module.memory = 'on' if module.memory == 'off' else 'off'
                    outgoing = 'hi' if module.memory == 'on' else 'low'
                    for x in module.outputs:
                        q.append(((module.name, x, outgoing)))
            else:
                module.memory[origin] = pulse
                outgoing = 'low' if all(x == 'hi' for x in module.memory.values()) else 'hi'
                for x in module.outputs:
                    q.append(((module.name, x, outgoing)))

    print(f'Part 1: {low_pulse*high_pulse}')



    # asserts there must be 1 case of rx
    (feed,) = [name for name, module in modules.items() if 'rx' in module.outputs]
    cycle_lengths = {}
    seen = {name: 0 for name, module in modules.items() if feed in module.outputs}
    
    presses = 0
    while True:
        presses += 1
        q = deque([('broadcaster', x, 'low') for x in broadcast_targets])

        while q:
            origin, target, pulse = q.popleft()

            if target not in modules:
                continue
                
            module = modules[target]

            if module.name == feed and pulse == 'hi':
                seen[origin] += 1

                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses
                else:
                    assert presses == seen[origin] * cycle_lengths[origin]

                if all(seen.values()):
                    x = 1
                    for cycle_length in cycle_lengths.values():
                        x = math.lcm(x, cycle_length)
                    print(f'Part 2: {x}')
                    return 

            if module.m_type == '%':
                if pulse == 'low':
                    module.memory = 'on' if module.memory == 'off' else 'off'
                    outgoing = 'hi' if module.memory == 'on' else 'low'
                    for x in module.outputs:
                        q.append(((module.name, x, outgoing)))
            else:
                module.memory[origin] = pulse
                outgoing = 'low' if all(x == 'hi' for x in module.memory.values()) else 'hi'
                for x in module.outputs:
                    q.append(((module.name, x, outgoing)))


if __name__ == '__main__':
    main()