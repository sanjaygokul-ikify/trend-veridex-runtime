# Contributing to Veridex

## Prerequisites
- Rust 1.70+, Cargo, LLVM 16
- SGX SDK 2.16
- Docker 25.0.0+

## Workflow
1. Run `make dev` in new branch
2. Execute `cargo test --all-features`
3. Submit PR with performance benchmarks

## Style Guide
- Follow RFC-001 architecture
- Add tests for all public APIs
- Update docs/rfcs/001-architecture.md for major changes