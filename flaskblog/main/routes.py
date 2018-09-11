from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flaskblog.main.forms import TemperatureForm
import requests,json
from urllib.request import urlopen

from geopy.geocoders import GoogleV3
main = Blueprint('main', __name__)



@main.route("/",methods=['GET','POST'])
@main.route("/home",methods=['GET','POST'])
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    tmp = TemperatureForm()
    curr_temp = "--"
    print( tmp.city.data)
    # if tmp.validate_on_submit():
    data = index()
    tmp.city.data = data['city']
    curr_temp,icon = tmp.fetch_temp_data(tmp.city.data)
    return render_template('home.html',posts=posts,form=tmp,temp = curr_temp,icon=icon,country = data['country'],ip = data['ip'])


@main.route("/about")
def about():
    return render_template('about.html', title='About')


def index():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']
    print('Your IP detail\n ')
    print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org, region, country, city, IP))
    print(city)
    return data