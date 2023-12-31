from flask import Flask, render_template, Response
from libs.camera import Camera
import time

call_camera = Camera()

app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")

def gen(camera):
    while True:
        frame = camera.start_capture()
        if frame != "":
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @app.route('/video_feed')
# def video_feed():
#     id = 0
#     return Response(gen(ObjectDetection(id)), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_stream')
def get_stream():
    return Response(gen(call_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Serve the app with gevent
    app.run(host='0.0.0.0', threaded=True, debug = True, port='5001')
