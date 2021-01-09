from time import perf_counter


class PerformanceHandler:
    def __init__(self, string_to_format: str):
        self.string_to_format = string_to_format

    def __enter__(self):
        self.start_time = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = perf_counter()
        self.__print()

    def __print(self):
        elapsed_time = self.end_time - self.start_time
        print(self.string_to_format.format(elapsed_time))
