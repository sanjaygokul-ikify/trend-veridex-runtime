import logging
from typing import List, Tuple, Dict
from .types import AgentState, ExecutionResult, Action
from .exceptions import VeridexError, EngineError


class VeridexEngine:
    def __init__(self, agents: List[AgentState], max_steps: int):
        self.agents = agents
        self.max_steps = max_steps
        self.step_count = 0
        self.logger = logging.getLogger(__name__)

    def execute_step(self, agent_state: AgentState, action: Action) -> ExecutionResult:
        try:
            execution_result = self._execute_step(agent_state, action)
            return execution_result
        except EngineError as e:
            self.logger.error(f"Engine error: {e}")
            raise VeridexError(f"Engine error: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            raise VeridexError(f"Unexpected error: {e}")

    def _execute_step(self, agent_state: AgentState, action: Action) -> ExecutionResult:
        # execute the action on the agent state
        new_agent_state = self._apply_action(agent_state, action)
        # verify the execution result using hardware attestation
        verification_result = self._verify_execution(new_agent_state, action)
        # update the agent state and step count
        self.agents.append(new_agent_state)
        self.step_count += 1
        # log the execution result
        self.logger.info(f"Executed step {self.step_count}: {action}")
        return ExecutionResult(new_agent_state, verification_result)

    def _apply_action(self, agent_state: AgentState, action: Action) -> AgentState:
        # apply the action to the agent state
        new_agent_state = AgentState(
            agent_state.id,
            agent_state.state,
            agent_state.actions + [action]
        )
        return new_agent_state

    def _verify_execution(self, agent_state: AgentState, action: Action) -> Dict[str, str]:
        # verify the execution result using hardware attestation
        verification_result = {}
        # simulate hardware attestation
        verification_result["result"] = "success"
        verification_result["message"] = "Execution verified"
        return verification_result

    def has_reached_max_steps(self) -> bool:
        return self.step_count >= self.max_steps

    def get_agents(self) -> List[AgentState]:
        return self.agents

    def get_step_count(self) -> int:
        return self.step_count

    def get_execution_results(self) -> List[ExecutionResult]:
        execution_results = []
        for agent_state in self.agents:
            execution_results.append(ExecutionResult(agent_state, {}))
        return execution_results


class Action:
    def __init__(self, id: str, type: str, data: str):
        self.id = id
        self.type = type
        self.data = data


class AgentState:
    def __init__(self, id: str, state: str, actions: List[Action]):
        self.id = id
        self.state = state
        self.actions = actions


class ExecutionResult:
    def __init__(self, agent_state: AgentState, verification_result: Dict[str, str]):
        self.agent_state = agent_state
        self.verification_result = verification_result

