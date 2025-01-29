from apps.admin import blueprint
from apps.home.models import Booking
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/admin')
@login_required
def index():
    bookings = Booking.query.all()
    if request.args.get('format') == 'json':
        return jsonify([{
            "id": b.id,
            "group_name": b.group_name,
            "member_name": b.member_name,  # assuming you meant 'name' as 'member_name'
            "member_email": b.member_email,  # assuming you meant 'email' as 'member_email'
            "nationality": b.nationality,
            "age": b.age,
            "phone": b.phone,
            "emergency_phone": b.emergency_phone,
            "identity_type": b.identity_type,
            "identity_number": b.identity_number,
            "identity_file": b.identity_file,
            "mountain_name": b.mountain_name,
            "climb_date": b.climb_date.strftime('%Y-%m-%d') if b.climb_date else None,
            "province": b.province,
            "city": b.city,
            "addr": b.addr
        } for b in bookings])

    # If not 'format=json', render the bookings list in the admin page
    return render_template('admin/admin.html', bookings=bookings)
