
# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from squats.camera import VideoCamera_squats
# Create your views here.
def index(request):
    return render(request, 'squats.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
                
def squats(request):
    return StreamingHttpResponse(gen(VideoCamera_squats()),
                    content_type='multipart/x-mixed-replace; boundary=frame')