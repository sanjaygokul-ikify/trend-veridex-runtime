import unittest
from packages.core import VeridexEngine, AgentState, Action, ExecutionResult

class TestCore(unittest.TestCase):
    def test_veridex_engine(self):
        agents = [AgentState('agent1', 'initial', [])]
        engine = VeridexEngine(agents, 10)
        action = Action('action1', 'type1', 'data1')
        execution_result = engine.execute_step(agents[0], action)
        self.assertIsInstance(execution_result, ExecutionResult)
    
    def test_agent_state(self):
        agent_state = AgentState('agent1', 'initial', [])
        self.assertEqual(agent_state.id, 'agent1')
        self.assertEqual(agent_state.state, 'initial')
        self.assertEqual(agent_state.actions, [])
