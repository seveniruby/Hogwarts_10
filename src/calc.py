
class Calc:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b==0:
            return None
        else:
            return a/b

    def above(self, a, b):
        if(a>b):
            return True
        else:
            return False