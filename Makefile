.PHONY: inventory docs-build validate

inventory:
	python3.11 tools/generate_inventory.py

docs-build:
	cd warehouse-architecture-docs && mdbook build

validate: inventory docs-build
