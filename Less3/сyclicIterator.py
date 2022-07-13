class CyclicIterator:

    def __init__(self, obj):
        self.obj = obj
        self.iter_obj = iter(self.obj)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next_obj = next(self.iter_obj)

        except StopIteration:
            self.iter_obj = iter(self.obj)
            next_obj = next(self.iter_obj)

        return next_obj
