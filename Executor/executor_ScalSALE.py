import os
import subprocess
from subprocess import Popen, PIPE
from Executor.executor import Executor


class Executor_ScalSALE(Executor):

    def get_module_compiler(self, compiler):
        if compiler == 'GNU':
            return '/home/talkad/LIGHTBITS_SHARE/AutoRunner/ScalSALE_Scripts/set_gnu.sh'
        elif compiler == 'oneAPI':
            return '/home/talkad/LIGHTBITS_SHARE/AutoRunner/ScalSALE_Scripts/set_oneapi.sh'
        else:
            return None

    def compile_project(self, project_path, compiler, opt):
        original_script_dir= 'src/Scripts'

        # set compiler env
        compile_script = self.get_module_compiler(compiler)
        if compile_script is not None:
            p = Popen([f'source {compile_script}'], shell=True)
            _, err = p.communicate()
        else:
            print(f'compiler {compiler} does not exist')
            return

        # print('Loaded modules:')
        # subprocess.run("module list", shell=True)

        # change dir to compile script
        compile_script_path = self.metadata['compile_script_path']
        idx = compile_script_path.rfind('/')
        script_dir, script_name = compile_script_path[:idx], compile_script_path[idx+1:]
        os.chdir(script_dir)

        # update optimization in cmake file
        cmake_path = self.metadata['cmake_list_path']
        with open(os.path.join(project_path, cmake_path), 'r+') as f:
            content = f.read()
            content = content.replace(f'<OPTIMIZATION>', str(opt))

            f.seek(0)
            f.write(content)
            f.truncate()

        # compile code
        self.execute_script('./'+script_name, os.path.join(project_path, original_script_dir), compiler, sync=True)

    def execute_project(self, project_path, compiler):

        # change dir to execute script
        execution_script_path = self.metadata['execution_script_path']
        idx = execution_script_path.rfind('/')
        script_dir, script_name = execution_script_path[:idx], execution_script_path[idx+1:]
        
        script_path = os.path.join(project_path, script_dir)
        os.chdir(script_path)

        # insert patch of the module loading
        compile_script = self.get_module_compiler(compiler)
        with open(script_name, 'r+') as script_file, open(compile_script, 'r') as compile_file:
            patch = compile_file.read()
            script = script_file.read()

            script = script.replace('<LOAD_MODULES>', patch)
            script_file.seek(0)
            script_file.write(script)
            script_file.truncate()

        # self.execute_script('./'+script_name, os.path.join(project_path, original_script_dir), compiler, sync=True)
        self.execute_script('sbatch', script_name, sync=False)

    


