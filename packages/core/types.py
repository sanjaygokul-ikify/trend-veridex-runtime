from typing import List, Dict
from dataclasses import dataclass

@dataclass
class AgentState:
    id: str
    state: str
    actions: List['Action']

@dataclass
class Action:
    id: str
    type: str
    data: str

@dataclass
class ExecutionResult:
    agent_state: AgentState
    verification_result: Dict[str, str]

