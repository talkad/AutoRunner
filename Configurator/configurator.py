from abc import ABC, abstractmethod


class Configurator(ABC):
    '''
    Configurator creates all the configurations that will be used to update the files given in the ENV VARIABLES.

    '''

    def __init__(self):
        self.configurations = []
        self.optimizations = ['O0', 'O2']
        # self.compilers = ['gnu', 'intel', 'oneAPI']
        self.compilers = ['GNU']
        self.curr_idx = 0

    def initiate(self):
        self.curr_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_idx >= len(self.configurations):
            raise StopIteration

        configuration = self.configurations[self.curr_idx]
        self.curr_idx += 1

        return configuration