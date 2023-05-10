class Pipeline:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter_instance):
        self.filters.append(filter_instance)

    def run(self, data):
        for filter_instance in self.filters:
            data = filter_instance.process(data)
        return data
