import re
import json


class Injector:
    def __init__(self):
        pass

    def update_script(self, files, configurations):
        '''
        Inject into each wild-card the given configuration
        '''
        for file in files:

            with open(file, 'r+') as f:
                content = f.read()

                for conf_idx, configuraion in enumerate(configurations):
                    content = content.replace(f'${conf_idx+1}', str(configuraion))

                f.seek(0)
                f.write(content)
                f.truncate()
