class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.arg = (msg)

try:
    raise Ex("ex")
except Ex as e:
    print(e.arg)
except Exception as e:
    print(e)