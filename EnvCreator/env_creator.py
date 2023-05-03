import os
import shutil


class EnvironmentCreator:
    """
    Creates a duplicate of the original program to be executed
    """

    def __init__(self, hard_copy_files):
        self.hard_copy_files = hard_copy_files

    def create_folder(self, folder_name):
        if os.path.exists(folder_name):
            shutil.rmtree(folder_name, ignore_errors=True)

        os.makedirs(folder_name)

    def create_env(self, src_dir, dest_dir, env_name, is_hard_copy=False):
        '''
        Create the environment to new duplicate of the original project

        Parameters:
            env_name: the duplicate name
        '''
        dest_dir = os.path.join(dest_dir, env_name)
        self.create_folder(dest_dir)

        for root, directories, filenames  in os.walk(src_dir):

            relative_path = root[len(src_dir)+1:]
            
            # dont copy build stuff
            # if 'build' in root:
            #     continue

            for directory in directories:
                self.create_folder(os.path.join(dest_dir, relative_path, directory))

            for filename in filenames:

                if is_hard_copy or os.path.join(relative_path, filename) in self.hard_copy_files:
                    shutil.copyfile(os.path.join(root, filename), os.path.join(dest_dir, relative_path, filename))
                else:
                    os.symlink(os.path.join(root, filename), os.path.join(dest_dir, relative_path, filename))

