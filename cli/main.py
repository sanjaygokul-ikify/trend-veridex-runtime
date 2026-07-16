import argparse
from services.orchestrator import Orchestrator
from packages.core import AgentState, Action

def main():
    parser = argparse.ArgumentParser(description='Veridex CLI')
    parser.add_argument('--agents', type=int, help='Number of agents')
    parser.add_argument('--max-steps', type=int, help='Maximum number of steps')
    args = parser.parse_args()
    agents = [AgentState(str(i), 'initial', []) for i in range(args.agents)]
    orchestrator = Orchestrator(agents, args.max_steps)
    orchestrator.run()

def run():
    main()