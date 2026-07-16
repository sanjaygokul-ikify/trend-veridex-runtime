from typing import List
from .types import AgentState, ExecutionResult
from ..core.engine import VeridexEngine
from ..core.exceptions import VeridexError


class RuntimeExecutor:
    def __init__(self, engine: VeridexEngine):
        self.engine = engine

    def execute(self) -> None:
        try:
            execution_results = self._execute()
            self._handle_execution_results(execution_results)
        except VeridexError as e:
            # handle the error
            print(f"Error: {e}")

    def _execute(self) -> List[ExecutionResult]:
        # execute the engine
        execution_results = self.engine.get_execution_results()
        return execution_results

    def _handle_execution_results(self, execution_results: List[ExecutionResult]) -> None:
        # handle the execution results
        for execution_result in execution_results:
            print(f"Execution result: {execution_result.agent_state.state}")

