import matplotlib.pyplot as plt
import os
import re
import pandas as pd
from math import ceil

num_cores = [i**3 for i in range(1,7)]

def find_run_time(dir_path):
    regex = re.compile('runtime_*')

    for root, dirs, files in os.walk(os.path.join(dir_path, 'src', 'Scripts')):
        for file in files:
            if regex.match(file):

                with open(os.path.join(root, file), 'r') as f:
                    time = float(f.read()[13:])
                    return time

def get_runtimes(directory):  #directory = '/home/talkad/LIGHTBITS_SHARE/ScalSALE_permutations_strong/GNU/O0'
    # strong
    configurations = [(i, i**3) for i in range(1,7)]
    # configurations = [(np_axis, n_cores, ceil(n_cores/32), 479) for np_axis, n_cores in configurations]

    # weak
    configurations = [(np_axis, n_cores, ceil(n_cores/32), (np_axis*160 -1)) for np_axis, n_cores in configurations]

    configurations = ['_'.join(['ScaleSALE'] + [str(conf) for conf in configuration]) for configuration in configurations]
    run_times = []
    print(configurations)

    for configuration in configurations:
        run_time = find_run_time(os.path.join(directory, configuration))
        run_times.append(run_time)

    print(run_times)
    return run_times


def get_effeciency(runtime,strong=True):
    eff = []

    for time, cores in zip(runtime, num_cores):
        if strong:
            eff.append((runtime[0]/time)/cores)
        else:
            eff.append(runtime[0]/time)

    return eff


def get_speedup(runtime):
    speedup = []

    for time in runtime:
        speedup.append(runtime[0]/time)

    return speedup


def main(directory, strong=True):
    res = {}
    runtimes = get_runtimes(directory)
    # print(runtimes)

    res['runtime'] = runtimes

    if strong:
        res['speedup'] = get_speedup(runtimes)

    res['efficiency'] = get_effeciency(runtimes, strong=strong)

    df = pd.DataFrame.from_dict(res)

    return df

df = main('/home/talkad/LIGHTBITS_SHARE/ScalSALE_permutations_20/ScalSALE_permutations_weak_160/GNU/O0', strong=False)

print(df)
df.to_csv("ScalSALE_permutations_weak_120.csv")

