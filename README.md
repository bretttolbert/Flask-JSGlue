# Flask-JSGlue

Flask-JSGlue helps hook up your Flask application nicely with the front end.

Usage Example:

```python
import flask_jsglue

app = Flask(__name__, root_path=root_path)
flask_jsglue.init(app)
```

```html
<head>
    <meta charset="UTF-8">
    <title>application</title>
    {{ JSGlue.include() }}
...
    <script>
    $("#linkAlbum").prop("href", Flask.url_for("main.tracks", artist=track.artist, album=track.album));
```

Forked from: http://stewartpark.github.io/Flask-JSGlue/ (no longer maintained)

Changes in this fork:
- Fixed issue `ImportError: cannot import name 'Markup' from 'jinja2'` by updating to use `markupsafe`
- Converted from older `setup.py` project to modern `pyproject.toml` project
- Modified to use pytest instead of unittest
- Modified to Flask Blueprints instead of the main app (consequently now using `app_context_processor` instead of `context_processor` for `JSGlue`)
- Removed initialization logic from `JSGlue` class, replaced it with `flask_jsglue.init` method and added optional `url_prefix` param.

Note: In order to get it working, I had to resort to copying [templates/js_bridge.js](./flask_jsglue/main/templates/js_bridge.js) into the templates folder of my application. TODO: Figure out how to avoid this. This shouldn't be necessary, but I don't have time to figure it out right now.
