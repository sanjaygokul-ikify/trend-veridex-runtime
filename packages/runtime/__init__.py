from .executor import RuntimeExecutor


class Runtime:
    def __init__(self, engine: 'VeridexEngine'):
        self.engine = engine
        self.executor = RuntimeExecutor(engine)

    def execute(self) -> None:
        self.executor.execute()

