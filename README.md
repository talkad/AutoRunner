# AutoRunner

AutoRunner is a tool designed to accelerate the process of benchmark performance evaluation by automatically creating instances of different configurations of your project. With AutoRunner, you can easily test your project using different data files, compilers, and optimization flags, without having to manually configure, compile, and run each instance.


## Architecture

AutoRunner is built using several key components, each of which plays a critical role in its functionality:

![autoRunner](https://user-images.githubusercontent.com/48416212/236218034-34d3c113-636d-45c3-bded-2dddd1677c46.jpg)

### Configurator
The Configurator is an iterable object that defines the different configurations you want to test. Each configuration is represented as a tuple of length N, where N is the number of parameters in your project that can be changed.

### Injector
The Injector is responsible for injecting the different configuration options into your project. It replaces wildcards ($1, $2, ...) in your project's configuration files with specific configuration values for each configuration being tested.

Each entry in the configuration is represented as $1, $2, $3, and so on, according to the order in which the entries appear. The Injector replaces these wildcards with the specific configuration value for each configuration being tested, ensuring that each configuration is tested with the appropriate settings.

### Environment Creator
The Environment Creator is responsible for creating the environment in which each configuration will be executed.

### Executor
The Executor is an abstract class that defines the interface for executing your project. It provides two abstract methods that must be implemented: 

```
compile_project(project_path:str, compiler:str, opt:str)
execute_project(project_path:str, compiler:str)
```

In addition, the Executor provides an execute method that iterates over all the configurations defined in the Configurator, and creates a dedicated environment for each configuration by injecting the appropriate configuration options using the Injector. It then compiles and executes the program using the compile_project and execute_project methods, respectively.


## Usage
To use AutoRunner, you will need to provide concrete implementations of the Configurator and Executor classes that are specific to your project. In addition, you will also need to provide a JSON file that includes the following parameters:

```
    base_path: str - Path to the original project directory.
    dest_path: str - Path to the directory that will contain the different code permutations.
    execution_script_path: str - Path to where the execution script can be found in the project.
    compile_script_path: str - Path to where the compile script can be found in the project.
    updated_files: list[str] - Which files should be updated by the Injector.
    hardcopy_files: list[str] - Which files should be hard copied instead of symbol-linked.
```
