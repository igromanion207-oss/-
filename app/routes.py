from flask import Blueprint, Response, abort, current_app, render_template, url_for

from .content import get_all_tags, get_post, get_posts, get_project, get_projects

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    featured = [p for p in get_projects() if p.get("featured")]
    return render_template("index.html", projects=featured, posts=get_posts()[:3])


@bp.route("/projects/")
def projects():
    return render_template("projects.html", projects=get_projects(), tags=get_all_tags())


@bp.route("/projects/<slug>/")
def project(slug):
    item = get_project(slug) or abort(404)
    return render_template("project.html", project=item)


@bp.route("/blog/")
def blog():
    return render_template("blog.html", posts=get_posts())


@bp.route("/blog/<slug>/")
def post(slug):
    item = get_post(slug) or abort(404)
    return render_template("post.html", post=item)


@bp.route("/about/")
def about():
    return render_template("about.html", skills=current_app.config["SKILLS"])


@bp.route("/contact/")
def contact():
    return render_template("contact.html")


@bp.route("/sitemap.xml")
def sitemap():
    base = current_app.config["SITE_URL"].rstrip("/")
    urls = [url_for("main.index"), url_for("main.projects"), url_for("main.blog"),
            url_for("main.about"), url_for("main.contact")]
    urls += [url_for("main.project", slug=p["slug"]) for p in get_projects()]
    urls += [url_for("main.post", slug=p["slug"]) for p in get_posts()]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [f"  <url><loc>{base}{u}</loc></url>" for u in urls]
    xml.append("</urlset>")
    return Response("\n".join(xml), mimetype="text/xml")


@bp.route("/robots.txt")
def robots():
    base = current_app.config["SITE_URL"].rstrip("/")
    return Response(f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n",
                    mimetype="text/plain")
