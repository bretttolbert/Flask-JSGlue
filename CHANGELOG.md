# 2026-09-12 [2.1.0]

Changed
- Layout to src layout

Added
- GitHub CI config
- requirements.txt
- Type hints
- Type stubs

# 2025-12-06 [2.0.0] (first bretttolbert forked version)

Changed
- Fixed issue `ImportError: cannot import name 'Markup' from 'jinja2'` by updating to use `markupsafe`
- Converted from older `setup.py` project to modern `pyproject.toml` project
- Modified to use `pytest` instead of `unittest
- Modified to Flask Blueprints instead of the main app (consequently now using `app_context_processor` instead of `context_processor` for `JSGlue`)
- Removed initialization logic from `JSGlue` class, replaced it with `flask_jsglue.init` method and added optional `url_prefix` param.
