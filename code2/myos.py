import os 
import shutil


def createEmptyDir(path_dir):
    if os.path.isdir(path_dir):
        shutil.rmtree(path_dir) 
    else:
        os.mkdir(path_dir)
    
    
def getPathAll(path_dir):
    paths = []
    path_list = os.walk(path_dir)
    for i, item in enumerate(path_list):
        print(item)
        paths_t = []
        if len(item[2]) > 0:
            for pth in item[2]:
                pth_t = os.path.join(item[0], pth)
                paths_t.append(pth_t)
            paths.append(paths_t)
    return paths


if __name__=="__main__":
    pths = getPathAll("./../")
    print(pths)
    os.system("python ./../code/class.py")

