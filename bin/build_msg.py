from build import genutil
import os,sys,env


if __name__ == '__main__':
    genutil.genmain(sys.argv+["..//demo//custom"], 'msg')
