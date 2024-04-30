from app import create_app

app = create_app()

from werkzeug.debug import DebuggedApplication

application = DebuggedApplication(app, evalex=True)
