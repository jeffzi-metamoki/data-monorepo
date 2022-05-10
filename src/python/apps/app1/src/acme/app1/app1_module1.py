from .app1_subpackage1.app1_module2 import app1_func2
from acme.lib1 import lib1_func1
from acme.lib1.lib1_module2 import lib1_func3


def app1_func1():
    print("app1_func1")
    app1_func2()
    lib1_func1()
    lib1_func3()
