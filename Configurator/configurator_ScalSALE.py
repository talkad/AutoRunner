from Configurator.configurator import Configurator
from math import ceil


class Configurator_ScalSALE(Configurator):
    """
    Configurator creates the different execution configurations.

    A configuration is composed by three hyper-parameters:
        - np_axis: int - num proccess per grid axis
        - n_cores: int - number of cores used in the execution
        - n_nodes: int - number of nodes used in the execution
    """
    def __init__(self):
        super().__init__()

        # self.configurations = [(i, i**3) for i in range(1,7)]
        self.configurations = [(i, i**3) for i in range(4,7)]

        # strong
        # self.configurations = [(np_axis, n_cores, ceil(n_cores/32), 359) for np_axis, n_cores in self.configurations]

        # weak
        self.configurations = [(np_axis, n_cores, ceil(n_cores/32), (np_axis*160 -1)) for np_axis, n_cores in self.configurations]

        
