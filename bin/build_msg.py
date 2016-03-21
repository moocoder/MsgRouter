from build import genutil
import os,sys,env

import genmsg.template_tools

msg_template_map = {'msg.h.template': '@NAME@.h'}
srv_template_map = {'srv.h.template': '@NAME@.h'}

if __name__ == "__main__":
    genmsg.template_tools.generate_from_command_line_options(sys.argv + ["../demo/custom/user.msg"],
                                                             msg_template_map,
                                                             srv_template_map)

if __name__ == '__main__s':
    genutil.genmain(sys.argv+["..//demo//custom"], 'msg')
