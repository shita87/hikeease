from apps.admin import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/admin')
@login_required
def index():
    return render_template('admin/admin.html')