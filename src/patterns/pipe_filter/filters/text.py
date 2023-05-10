from patterns.pipe_filter.filter import Filter


class UppercaseFilter(Filter):
    def process(self, data):
        return data.upper()


class ReverseFilter(Filter):
    def process(self, data):
        return data[::-1]
