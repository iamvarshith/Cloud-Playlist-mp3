from app import app, bcrypt
from app.forms import LoginForm, RegistrationForm
from app.presigned_url import create_presigned_url
import boto3

import pandas as pd
import hashlib
import json
import random

import requests
from flask import render_template, url_for, redirect, request, jsonify, session, flash
from flask_login import login_user, current_user, login_required, logout_user
from app import app, db, login_manager

from app.models import User, Music, Playlist


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@app.route("/")
@login_required
def home():
    songs = Music.query.limit(20).all()
    first_song = songs[0]
    first_url = create_presigned_url('cloud-niit-project', str(songs[0].song_id), 6000, 's3v4')
    return render_template("index.html", songs=songs, first_url=first_url)


@app.route("/song/<token>")
@login_required
def song_find(token):
    song = Music.query.filter_by(song_id=token).first()
    songs = Music.query.limit(20).all()
    first_url = create_presigned_url('cloud-niit-project', str(song.song_id), 6000, 's3v4')
    return render_template("song.html", songs=songs, song=song, first_url=first_url)


@app.route("/all_songs")
@login_required
def all_songs():
    songs = Music.query.limit(100).all()
    return render_template("all_songs.html", songs=songs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):

            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))

        else:
            flash("unsucessful login", 'danger')

    return render_template('login.html', title='login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    else:

        return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/add_playlist', methods=['POST'])
def add_playlist():
    if request.method == "POST":
        song_id = request.form['song_id']
        playlist = Playlist(user_id=current_user.id, music_id=song_id)
        db.session.add(playlist)
        db.session.commit()
    return '200'


@app.route('/your_playlist')
@login_required
def your_play_list():
    songs_obj = current_user.playlist

    songs = []
    for i in songs_obj:
        songs.append(Music.query.filter_by(song_id=i.music_id).first())

    return render_template('playlist.html', songs=songs)
