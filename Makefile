.PHONY: inventory workflow-spec-check workflow-preflight docs-build validate

inventory:
	python3.11 tools/generate_inventory.py

workflow-spec-check: inventory
	python3.11 tools/preflight_workflow_specs.py

workflow-preflight: inventory
	python3.11 tools/preflight_workflow_specs.py --strict-placeholders

docs-build:
	cd warehouse-architecture-docs && mdbook build

validate: workflow-spec-check docs-build
