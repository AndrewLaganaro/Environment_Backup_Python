import subprocess
"""A file to automatically backup python environments and it's packages specifications"""
class folder:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def execOrder(to_order):
    ordered = []
    for execution in range(len(to_order.keys())):
        ordered.append(execution)
    return ordered

Environment = "Data_Science"
Environment_file = "Data_Science"
Packages_file = "Data_Science"
Save_to = "A:\Andrew\Desenvolvimento\Environment"

execute = {"Turn env ON:":          f"conda activate {Environment}",
           "Generate env specs:":   f"conda env export > {Environment_file}.yml",
           "Generate packs specs:": f"pip freeze > {Packages_file}.txt"}

order = execOrder(execute)

with folder(Save_to):
        
    for execution, current in zip(execute.values(), order):
        try:
            subprocess.run(execution, shell=True)
            
            if order.index(current) == 0:
                print("Backup folder found")
            elif order.index(current) == 1:
                print("Enviroment file generated")
            elif order.index(current) == 2:
                print("Packages file generated")
                print("All done!")
        except:
            if order.index(current) == 0:
                print("Couldn't find backup folder")
            elif order.index(current) == 1:
                print("Couldn't generate enviroment file")
            elif order.index(current) == 2:
                print("Couldn't generate any file!")