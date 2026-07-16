import unittest
from services.orchestrator import Orchestrator

class TestRuntime(unittest.TestCase):
    def test_orchestrator(self):
        agents = [{'id': 'agent1', 'state': 'initial', 'actions': []}]
        orchestrator = Orchestrator(agents, 10)
        orchestrator.run()
        self.assertEqual(orchestrator.step_count, 10)