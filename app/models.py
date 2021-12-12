from datetime import datetime
from app import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=True, default='lol_google_login')
    playlist = db.relationship('Playlist', backref='user')

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}','{self.image_file}','{self.password}')"


class Music(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    music_name = db.Column(db.String(60))
    artist_name = db.Column(db.String(60))
    url = db.Column(db.String(200))
    icon_url = db.Column(db.String(200))
    playlist_music = db.relationship('Playlist', backref='music')

    def __repr__(self):
        return f"Music('{self.song_id}', '{self.music_name}', '{self.artist_name}','{self.url}','{self.icon_url}')"


class Playlist(db.Model):
    playlist_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    music_id = db.Column(db.Integer, db.ForeignKey('music.song_id'))

    # def __repr__(self):
    #     return f"playlist('{self.playlist_id}', '{self.user_id}', '{self.music_id}')"
