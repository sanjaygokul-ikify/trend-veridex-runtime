SHELL := /bin/bash
.DEFAULT_GOAL := help

dev:
	cargo run --bin veridex

test:
	rust test

clean:
	docker system prune -af
	cargo clean
	help:
	@echo 'Makefile targets: dev test clean'