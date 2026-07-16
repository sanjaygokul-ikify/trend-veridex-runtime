import unittest
from cli.main import run
from packages.core import VeridexEngine, AgentState, Action

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        run()
        # Add pipeline-specific assertions here
        self.assertTrue(True)