from TDSL.TDSLType import *


class META_PERM(META_PERM_Base):
    META_PERM_URL = "http://127.0.0.1:8500/static_metaperm"

    def __init__(self):
        pass

    def pool(self, *args):
        return self

    webTester = pool("webTester")
    bravado = pool("bravado")
    karate = pool("karate")
