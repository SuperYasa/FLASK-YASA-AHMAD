from flask import Flask, render_template, url_for
from a2wsgi import WSGIMiddleware

flask_app = Flask(__name__)

Datas = [
    {
        'Nama': 'Yasa Ahmad Aflah Syabil',
        'Umur': '21 tahun',
        'Asal': 'Karanggede',
        'Pekerjaan': 'Mahasiswa',
        'gambar': 'image/yasaimage.jpeg',
        'dataa': 'umur : 21 tahun'
    },

]

@flask_app.route("/")
@flask_app.route("/home")
def home():
    return render_template('home.html', Datas=Datas)

@flask_app.route("/about")
def about():
    return render_template('about.html')

@flask_app.route("/kontak")
def kontak():
    return render_template('kontak.html')

# Wrapper WSGI ke ASGI untuk Uvicorn
app = WSGIMiddleware(flask_app)

if __name__ == '__main__':
    flask_app.run(debug=True)