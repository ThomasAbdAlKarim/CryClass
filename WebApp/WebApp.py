from flask import Flask, render_template, request,redirect,url_for
import os
import librosa
from time import sleep
import numpy as np
import librosa.display
import Ai
import time


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Rec'

Signal = []
Sr = 0


@app.route('/')
def home():
    return  render_template("Main.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save('Rec/A.wav')
    return  render_template("Out.html")

@app.route('/Out')
def Out():
    while(not os.path.exists('Rec/A.wav')) : 
        time.sleep(1)
    Signal,Sr = librosa.load('Rec/A.wav',sr=22050)
    print(os.stat('Rec/A.wav').st_size)
    Trimed = Ai.Trim(Ai.Pad(Signal,5),Sr)
    MFCC = Ai.Save_MFCC(Trimed,Sr)
    print(MFCC.shape)
    RSLT = Ai.Pred(MFCC)
    print(RSLT)
    Ind = np.where(RSLT[0]==max(RSLT[0]))
    if Ind[0][0] == 0 :
        RSLT_TXT = 'Hungry'
        Img = "static/Hungry.PNG"
    elif Ind[0][0] == 1 :
        RSLT_TXT = 'Pain'
        Img = "static/Pain.PNG"
    elif Ind[0][0] == 2:
        RSLT_TXT = 'UnComfortable\n'
        Img = "static/Uncom.PNG"
    else:
        RSLT = 'Unknown'
    print(Ind[0][0])
    RSLT_TXT += str(int(RSLT[0][Ind[0][0]])) + '%'
    return render_template("Out.html",Image = Img,Result = RSLT_TXT)



if __name__ == "__main__":
    os.environ['DEBUG'] = "1"
    app.run(host='#your local ip',debug=True,ssl_context='adhoc')




        
