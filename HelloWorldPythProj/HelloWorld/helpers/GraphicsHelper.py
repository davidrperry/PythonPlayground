import imp

class GraphicsHelper(object):
    """description of class"""

    @staticmethod
    def GetGraphicsModule():
        return imp.load_compiled("graphics", "C:/Users/DavidPerry/Source/Repos/PythonPLayGround/HelloWorldPythProj/HelloWorld/_psycache_/graphics.cpython-36.pyc")

