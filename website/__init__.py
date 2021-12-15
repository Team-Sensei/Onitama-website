from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'd!~K9TetifJ{t0E3R>AoGS7U>iR,H=Lbots.OeaYMh7;_w/Kv%/eQOi3|ET2Da'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app