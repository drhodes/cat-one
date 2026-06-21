'''
main spec
'''

from libspec import Spec
from . import app
from . import course
from . import link_checker
from . import makefile

class MainSpec(Spec):
    def modules(self):
        return [app, course, link_checker, makefile]



