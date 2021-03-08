var PP = false;

URL = window.URL || window.webkitURL;
var gumStream;

var rec;

var input;
 
var AudioContext = window.AudioContext || window.webkitAudioContext;


var recordButton = document.getElementById("rec");
Bar = document.getElementById("Bar");

recordButton.addEventListener("click", BUT,false);

var circle = document.querySelector('circle');
var radius = circle.r.baseVal.value;
var circumference = radius * 2 * Math.PI;

circle.style.strokeDasharray = `${circumference} ${circumference}`;
circle.style.strokeDashoffset = `${circumference}`;

function setProgress(percent) {
    const offset = circumference - percent / 100 * circumference;
    circle.style.strokeDashoffset = offset;
  }




function resolveAfter2Seconds(x) {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve(x);
      }, 11);
    });
  }

async function BUT()
{
    console.log('start');
    startRecording();
    var Count = 0;
    while(Count <= 400)
    {
    setProgress((Count*100.0)/400.0);
    await resolveAfter2Seconds(10);
    Count += 1
    }
    stopRecording();
    window.location.replace('/Out')
}



function startRecording() { 
    var audioContext = new AudioContext;
    var constraints = {
    audio: true,
    video: false
    } 
    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
        console.log("getUserMedia() success, stream created, initializing Recorder.js ..."); 

        gumStream = stream;

        
        input = audioContext.createMediaStreamSource(stream);
 
        rec = new Recorder(input, {
            numChannels: 1
        }) 

        rec.record()
        console.log("Recording started");
    }).catch(function(err) {

    });
}
    

function stopRecording() {
    console.log("stopButton clicked");

    rec.stop(); 
    gumStream.getAudioTracks()[0].stop();

    rec.exportWAV(createDownloadLink);
}


function createDownloadLink(blob) {
    var url = URL.createObjectURL(blob);
    var au = document.createElement('audio');
    var li = document.createElement('li');
    var link = document.createElement('a');

    au.controls = true;
    au.src = url;

    console.log(url);
    Upload(blob);


}


function Upload(blob)
{
    var form = new FormData();
    form.append('file', blob, 'test.wav');
    $.ajax({
        type: 'POST',
        url: '/upload',
        data: form,
        cache: false,
        processData: false,
        contentType: false
      }).done(function(data) {
        console.log('data');
      });
    
}