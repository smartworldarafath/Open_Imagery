# AGENTS.md

## Project

Open Imagery is a Python CLI and Web Dashboard for capturing Google Street View photos, high-resolution satellite imagery, 3D meshes, digital elevation models, and OpenStreetMap data for AI agents and developers. It requires no browser or API key.

- `open_imagery.py` (and alias `aleph.py`): command-line entry points
- `src/`: capture, networking, geometry, Street View, mesh, terrain, and web dashboard code
- `tests/`: unit tests
- `README.md`: setup, usage, architectural diagrams, and troubleshooting.
- `resources/`: assets, diagrams, and resources

## Changes

- Keep the CLI minimal, fast, and simple
- Maintain zero-API-key accessibility
- Run the offline tests with `python -m unittest discover -v`
