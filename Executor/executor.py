import os
import json
import subprocess
import itertools
from abc import ABC, abstractmethod
from subprocess import Popen, PIPE
from EnvCreator.env_creator import EnvironmentCreator


class Executor(ABC):
    def __init__(self, project_name, metadata_file, configurator, injector):
        self.project_name = project_name
        self.metadata = self.read_metadata(metadata_file)

        self.env_creator = EnvironmentCreator(self.metadata['hardcopy_files'])
        self.configurator = configurator
        self.injector = injector

    def read_metadata(self, metadata_file):
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)

        return metadata

    def execute_script(self, *args, sync=True):
        '''
        Execute a given script

        Parameters:
            sync - whether to execute the run synchronously or not
            args - script parameters
        '''

        p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)

        if sync:
            _, err = p.communicate()                      # communicate waits for the proccess to terminate

    @abstractmethod
    def compile_project(self, project_path, compiler, opt):
        '''
        Compile the project with a given compiler and optimization

        Parameters:
            project_path: path to the base directory of the project
            compiler: compiler name
            opt: the optimization flag (O0/O2/...)
        '''
        pass

    @abstractmethod
    def execute_project(self, project_path, compiler):
        '''
        Execture the project 

        Parameters:
            project_path: path to the base directory of the project
            compiler: compiler name
        '''
        pass

    def execute(self):
        '''
            for each configuration:
                1. create environment
                2. update code according the current configuration
                3. execute script
        '''
        for compiler, optimization in itertools.product(self.configurator.compilers, self.configurator.optimizations):

            # create hard copy and compile it according to given compiler and optimization
            dest_dir = os.path.join(self.metadata['dest_path'], compiler, optimization)
            self.env_creator.create_env(self.metadata['base_path'], dest_dir, self.project_name, is_hard_copy=True)
            self.compile_project(os.path.join(dest_dir, self.project_name), compiler, optimization) 

            print(f' - Create Copy: {compiler} {optimization}')

            # create configuration and execute
            self.configurator.initiate()
            for configuration in self.configurator:
                
                print(f' - Configuration: {configuration}')
                copy_folder_name = '_'.join([self.project_name] + [str(conf) for conf in configuration])
                self.env_creator.create_env(os.path.join(dest_dir, self.project_name), dest_dir, copy_folder_name)
                
                self.injector.update_script([os.path.join(dest_dir, copy_folder_name,file_path) for file_path in self.metadata['updated_files']], configuration)
                self.compile_project(os.path.join(dest_dir, copy_folder_name), compiler, optimization) 
               
                self.execute_project(os.path.join(dest_dir, copy_folder_name), compiler)


