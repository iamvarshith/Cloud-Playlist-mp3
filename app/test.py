from app import app
from app import db

import pandas as pd
import xlrd

from app.models import Music
from app.upload_s3 import upload_file_s3

from app.presigned_url import create_presigned_url

df = pd.read_excel('C:\\Users\\varsh\\Downloads\\music_xl.xlsx', sheet_name='Sheet1')

for i in range(1, 100):
    print(df.iloc[i][0], df.iloc[i][1], df.iloc[i][2], df.iloc[i][3])

    upload_file_s3(f'C:\\Users\\varsh\\Downloads\\music\\music\\{i}.mp3', str(i))
    generated_signed_url = create_presigned_url('cloud-niit-project', str(i), 6000, 's3v4')
    song = Music(music_name=df.iloc[i][0], artist_name=df.iloc[i][1], url=generated_signed_url, icon_url=df.iloc[i][3])
    print(generated_signed_url)
    db.session.add(song)
    db.session.commit()
