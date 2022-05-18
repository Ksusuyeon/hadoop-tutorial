import os
import sys


def build_image(arg):
    
    if arg == 'base':
        command = "docker build -t hadoop-base ./Dockerfiles/base/"
        os.system(command)

    elif arg == "namenode":
        command = "docker build -t hadoop-namenode ./Dockerfiles/namenode/"
        os.system(command)
    
    elif arg == "datanode":
        command = "docker build -t hadoop-datanode ./Dockerfiles/datanode/"
        os.system(command)

def docker_compose():
    pass


if __name__ == "__main__":
    if sys.argv[1] == '--build':
        build_image(sys.argv[2])
        
    elif sys.argv[1] == '--up':
        pass