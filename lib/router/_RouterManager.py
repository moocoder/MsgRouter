import re
from xmlrpc.client import ServerProxy
from rosgraph import names


class RouterManager:
    """
        RouterManager :create a multi-master nodes server
        @author       :erow
    """
    """
        @param parent: send msg to parent when regex are unmatched
        @type  parent: str host:port
    """

    def __init__(self, local="http://localhost:11311"):
        self.local = local
        self.map = {}
        self.add_node('/s1', '*', "http://localhost:11411")

    """
        add_node    : add child master node
        @param ns   : namespace
        @type  ns   : str
        @param regex: regular expression
        @type  regex: str
        @param uri  : send msg to uri when match
        @type  uri  : str host:port
    """

    def add_node(self, ns, regex, uri):
        if names.is_legal_name(ns):
            str = names.canonicalize_name(ns)
            self.map[str + '/' + regex] = uri
        else:
            raise NameError

    """
        match       : add child master node
        @param regex: regular expression
        @type  regex: str
        @param uri  : send msg to uri when match
        @type  uri  : str host:port
    """

    def match(self, name):
        if not names.is_legal_name(name):
            raise NameError

        for regex in self.map:
            ex = re.compile(regex)
            if ex.match(name):
                self.last_uri = self.map[regex]
                return self.map[regex]
        return None

    def call(self, fun, *args, **kwargs):
        try:
            s = ServerProxy(self.last_uri)

        except EOFError:
            pass


if __name__ == "__main__":
    import env, rospy

    rospy.init_node("test")
    rospy.set_param("s1/rg", 13)
    rospy.get_param("s1/rg")
