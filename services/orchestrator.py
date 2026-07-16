from packages.core import VeridexEngine

class Orchestrator:
    def __init__(self, agents, max_steps):
        self.engine = VeridexEngine(agents, max_steps)
        self.step_count = 0
    
    def run(self):
        while not self.engine.has_reached_max_steps():
            for agent in self.engine.get_agents():
                action = agent.actions[0]
                execution_result = self.engine.execute_step(agent, action)
                self.step_count += 1
                print(f'Step {self.step_count}: {action.id}')