from flask import Blueprint, render_template

ui_bp = Blueprint("ui", __name__)


@ui_bp.get("/")
def index():
    return render_template("index.html")


@ui_bp.get("/results/<eval_id>")
def results(eval_id: str):
    # In a full implementation this would fetch stored results
    return render_template("results.html", eval_id=eval_id)
