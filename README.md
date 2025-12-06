# Flask-JSGlue

Flask-JSGlue helps hook up your Flask application nicely with the front end.

Usage Example:

```python
from flask_jsglue import JSGlue

app = Flask(__name__, root_path=root_path)
jsglue = JSGlue(app)
```

```html
<head>
    <meta charset="UTF-8">
    <title>application</title>
    {{ jsglue.include() }}
...
    <script>
    $("#linkAlbum").prop("href", Flask.url_for("main.tracks", artist=track.artist, album=track.album));
```

Forked from: http://stewartpark.github.io/Flask-JSGlue/ (no longer maintained)

Changes in this fork:
- Fixed issue `ImportError: cannot import name 'Markup' from 'jinja2'` by updating to use `markupsafe`
- Converted from older `setup.py` project to modern `pyproject.toml` project
