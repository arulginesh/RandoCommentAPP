from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("blog", __name__, url_prefix="/blog")


@bp.route("/")
def index():
    """Show all the topic"""
    allcomments = get_comments()        
    return render_template("blog/index.html", allcomments=allcomments)

def get_comments():
    """Show all the topic"""
    db = get_db()
    allcomments = (
        db.execute(
            "SELECT u.username, c.comments, c.user_id"
            " FROM comments c JOIN user u ON c.user_id = u.id"
            " ORDER BY created DESC"
        ).fetchall()
    )

    return allcomments

@bp.route("/comments", methods=("GET", "POST"))
@login_required
def comments():
    """Create a new Topic for the current user."""
    if request.method == "POST":
        comments = request.form["comments"]
        error = None

        if not comments:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
               "INSERT INTO comments (topic_id, user_id, comments) VALUES (?, ?, ?)",
                (1, g.user["id"], comments),
            )
            db.commit()
            return redirect(url_for("blog.comments"))
    allcomments = get_comments()        
    return render_template("blog/create.html", allcomments=allcomments)

