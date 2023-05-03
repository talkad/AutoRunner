from Injector.injector import Injector
from Configurator.configurator import Configurator
from EnvCreator.env_creator import EnvironmentCreator
from Executor.executor_ScalSALE import Executor_ScalSALE
from Configurator.configurator_ScalSALE import Configurator_ScalSALE



if __name__ == '__main__':
    configurator = Configurator_ScalSALE()
    injector = Injector()

    runner = Executor_ScalSALE('ScaleSALE', '/home/talkad/LIGHTBITS_SHARE/AutoRunner/env.json', configurator, injector)
    runner.execute()


