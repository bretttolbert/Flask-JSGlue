# Flask-JSGlue

`flask_jsglue` is a Python package providing a `Flask.url_for` method callable from front-end JavaScript.

## Usage Example

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

## About

Forked from: http://stewartpark.github.io/Flask-JSGlue/ (no longer actively maintained, it seems)

### Changes in this fork

See [CHANGELOG](./CHANGELOG.md)

## Issues

Note: In order to get it working, I had to resort to copying [templates/js_bridge.js](./flask_jsglue/main/templates/js_bridge.js) into the templates folder of my application. TODO: Figure out how to avoid this. This shouldn't be necessary, but I don't have time to figure it out right now.
