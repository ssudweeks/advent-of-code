from os import ctermid
import helpers.input as input

scott_input = input.read_input(6)
scott_input = [int(n) for n in scott_input[0].split(',')]
sample_input = [ 3,4,3,1,2 ]

def progress(n):
    if n == 0:
        return 6
    else:
        return n - 1

def brute_force(input):
    days = 80
    ct = 0
    while (ct < days):
        new_fish = input.count(0)
        #print(f'Day {ct} {scott_input}')
        input = [progress(n) for n in input]
        for _ in range(new_fish):
            input.append(8)
        ct = ct + 1
    return input

print(len(brute_force(sample_input)))


def bulk_process(input):
    ct_0_fish = 0
    ct_1_fish = 0
    ct_2_fish = 0
    ct_3_fish = 0
    ct_4_fish = 0
    ct_5_fish = 0
    ct_6_fish = 0
    ct_7_fish = 0
    ct_8_fish = 0
    for fish in input:
        if fish == 0:
            ct_0_fish = ct_0_fish + 1
        if fish == 1:
            ct_1_fish = ct_1_fish + 1
        if fish == 2:
            ct_2_fish = ct_2_fish + 1
        if fish == 3:
            ct_3_fish = ct_3_fish + 1
        if fish == 4:
            ct_4_fish = ct_4_fish + 1
        if fish == 5:
            ct_5_fish = ct_5_fish + 1
        if fish == 6:
            ct_6_fish = ct_6_fish + 1
        if fish == 7:
            ct_7_fish = ct_7_fish + 1
        if fish == 8:
            ct_8_fish = ct_8_fish + 1

    days = 256
    ct = 0
    while (ct < days):
        ct_new_fish = ct_0_fish
        ct_0_fish = ct_1_fish
        ct_1_fish = ct_2_fish
        ct_2_fish = ct_3_fish
        ct_3_fish = ct_4_fish
        ct_4_fish = ct_5_fish
        ct_5_fish = ct_6_fish
        ct_6_fish = ct_7_fish + ct_new_fish
        ct_7_fish = ct_8_fish
        ct_8_fish = ct_new_fish

        ct = ct + 1
    
    print(ct_0_fish + ct_1_fish + ct_2_fish + ct_3_fish + ct_4_fish + ct_5_fish + ct_6_fish + ct_7_fish + ct_8_fish)
    
bulk_process(scott_input)
