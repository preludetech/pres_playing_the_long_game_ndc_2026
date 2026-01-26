import random 

chance_of_success = [
    0.55, 0.65, 0.85
]

for chance in chance_of_success:
    success = int(chance*100)
    tasks = ['1']*success + ['0']*(100-success)
    tasks.sort(key=lambda x:random.random())
    tasks = ''.join(tasks)

    chains = tasks.split('0')
    chains = [c for c in chains if len(c)>0]
    chains.sort(key=len)

    lengths = {}
    for c in chains:
        lengths[len(c)] = lengths.get(len(c),0)+1
    
    print(f"Chance of success: {chance}")
    print(f"{tasks}")
    for length, count in lengths.items():
        print(f"{length}:{count}")
    print()