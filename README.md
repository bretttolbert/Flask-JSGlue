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
- Use pytest instead of unittest
- Use Flask Blueprint instead of the main app
