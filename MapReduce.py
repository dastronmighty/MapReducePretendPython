class MapReduce:
    def __init__(self):
        self.__emits__ = {}

    def emit(self, k, v):
        if k in list(self.__emits__.keys()):
            self.__emits__[k].append(v)
        else:
            self.__emits__[k] = [v]

    def run(self, v):
        for val in v:
            self.Map(val)
        x = self.__emits__.copy()
        self.__emits__ = {}
        for k in list(x.keys()):
            self.Reduce(k, x[k])
        ret = {key: value for key, value in sorted(self.__emits__.items(), key=lambda item: item[1], reverse=True)}
        return ret
