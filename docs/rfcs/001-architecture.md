# Architecture RFC

## Overview

The system utilizes four core patterns:

1. **Worker Pool Pattern**: Adaptive scaling of compute resources
2. **Execution Containerization**: SGX-verified execution sandboxes
3. **Verification Layer**: Cryptographically signed execution proofs
4. **Global Snapshot Engine**: Merkle-tree-based state synchronization

## Verification Flow

Request -> Orchestrator -> Worker Pool -> Execution Container -> Verification Engine -> Global State

Each stage cryptographically signs its processing. Verification requires quorum across 3+ verification nodes in distinct trust domains.