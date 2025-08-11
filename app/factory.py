from flask import Flask


def create_app():
    """Application factory."""
    app = Flask(__name__)

    from .blueprints.api.routes import api_bp
    from .blueprints.ui.routes import ui_bp

    app.register_blueprint(ui_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
