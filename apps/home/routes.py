from apps import db
from apps.home import blueprint
from apps.home.models import Booking
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound
from datetime import datetime


@blueprint.route('/')
def index():
    return render_template('home/index.html', segment='index')

@blueprint.route('/contact_us')
def contact_us():
    return render_template('home/contact_us.html', segment='index')

@blueprint.route('/galery')
def galery():
    return render_template('home/galery.html', segment='index')

@blueprint.route('/<template>')
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'
        segment = get_segment(request)
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

@blueprint.route('/bookings', methods=['POST'])
def create_booking():
    data = request.json
    try:
        new_booking = Booking(
            group_name=data['group_name'],
            member_name=data['member_name'],
            member_email=data['member_email'],
            nationality=data.get('nationality', ''),
            age=data.get('age'),
            phone=data.get('phone'),
            emergency_phone=data.get('emergency_phone'),
            identity_type=data.get('identity_type'),
            identity_number=data.get('identity_number'),
            identity_file=data.get('identity_file'),
            mountain_name=data.get('mountain_name'),
            climb_date=datetime.strptime(data['climb_date'], '%Y-%m-%d') if 'climb_date' in data else None,
            province=data.get('province'),
            city=data.get('city'),
            addr=data.get('addr')
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking created successfully", "id": new_booking.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

