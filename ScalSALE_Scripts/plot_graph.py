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

directory = '/home/talkad/LIGHTBITS_SHARE/ScalSALE_permutations_weak/GNU/O2'
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



# strong

# GNU
# O0 [26343.619778902037, 3029.5413677440956, 960.9267051350325, 660.503250145819, 221.22190010400027, 218.5880979320009]
# O2 [11348.275887318001, 1325.4852111078799, 645.6437680800445, 237.88306507499965, 123.65402609500052, 117.76403685985133]

# weak

# GNU
# O0 [378.9017255420331, 383.2317148389993, 406.98557765595615, 657.4525901251473, 439.2358488220052, 639.3577225629997]
# O2 [168.6805979711935, 176.00965653400635, 221.75665827002376, 319.8690561801195, 235.15330879902467, 343.4685866991058]



plt.title('Weak Scaling - efficiency')
plt.ylabel('# cores')
plt.ylabel('efficiency')

plt.plot([1,8,27,64,125,216], [1.0, 0.9573228508446541, 0.7545416225021535, 0.6914594139931981])
plt.savefig('weak_nodes020_efficiency.png')
