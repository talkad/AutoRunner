import matplotlib.pyplot as plt
import os
import re
from math import ceil


def find_run_time(dir_path):
    regex = re.compile('runtime_*')

    for root, dirs, files in os.walk(os.path.join(dir_path, 'src', 'Scripts')):
        for file in files:
            if regex.match(file):

                with open(os.path.join(root, file), 'r') as f:
                    time = float(f.read()[13:])
                    return time

directory = '/home/talkad/LIGHTBITS_SHARE/ScalSALE_permutations_strong/GNU/O0'
# print(os.listdir(directory))
# strong
configurations = [(i, i**3) for i in range(1,7)]
# configurations = [(np_axis, n_cores, ceil(n_cores/32)) for np_axis, n_cores in configurations]

# weak
configurations = [(np_axis, n_cores, ceil(n_cores/32), (np_axis*120 -1)) for np_axis, n_cores in configurations]

configurations = ['_'.join(['ScaleSALE'] + [str(conf) for conf in configuration]) for configuration in configurations]
run_times = []

for configuration in configurations:
    run_time = find_run_time(os.path.join(directory, configuration))
    run_times.append(run_time)

print(run_times)


def get_effeciency(runtime):
    eff = []

    # for time, cores in zip(runtime, [1,8,27,64,125,216]):
    #     eff.append((runtime[0]/time)/cores)

    for time in runtime:
        eff.append(runtime[0]/time)

    return eff

# plt.title('Weak Scaling - Runtime')
# plt.xlabel('# cores')
# plt.ylabel('Runtime (sec)')

# plt.plot([1,8,27,64,125,216], [289.09449337702245, 380.7502974020317, 411.25228592701023, 430.9407107739826, 435.29127876693383, 436.5052798502147])
# plt.savefig('runtime_weak_o0_gnu_.png')



# First Attempt
# strong 30+

# GNU
# O0 [26343.619778902037, 3029.5413677440956, 960.9267051350325, 660.503250145819, 221.22190010400027, 218.5880979320009]
# O2 [11348.275887318001, 1325.4852111078799, 645.6437680800445, 237.88306507499965, 123.65402609500052, 117.76403685985133]


# weak 026-028, 030-034

# GNU 
# O0 [378.9017255420331, 383.2317148389993, 406.98557765595615, 657.4525901251473, 439.2358488220052, 639.3577225629997]
# O2 [168.6805979711935, 176.00965653400635, 221.75665827002376, 319.8690561801195, 235.15330879902467, 343.4685866991058]



# weak mantis

# GNU 
# O0 [363.8694168240181, 415.2569464079861, 428.2805393029994, 439.66777928199735, 571.0349934850237, 612.131957295991]
# O2 [164.45178800498252, 191.28173422798864, 208.95022530399729, 218.4658514749899, 349.14212909099297, 389.9383723390056]





# Second Attempt
# weak 026-028, 030-034

# GNU 
# O0 [289.09449337702245, 380.7502974020317, 411.25228592701023, 430.9407107739826, 435.29127876693383, 436.5052798502147]
# O2 [168.63940536836162, 149.89526488201227, 223.65992407203885, 242.5333136897534, 243.97028823196888, 244.35906281229109]

# weak mantis

# GNU 
# O0 [364.3744572320138, 414.9064832389704, 428.98428574897116, 437.64571919001173, 571.7307328499737, 613.0585176369641]
# O2 [164.34637699800078, 191.46119917999022, 209.187645833008, 219.6428085959633, 347.90703346504597, 388.81863062496996]


# for a in get_effeciency([164.34637699800078, 191.46119917999022, 209.187645833008, 219.6428085959633, 347.90703346504597, 388.81863062496996]):
#     print(a)
