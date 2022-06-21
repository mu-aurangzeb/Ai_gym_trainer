
# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from butterfly.camera import VideoCamera_butterfly
# Create your views here.

def index(request):
    return render(request, 'butterfly.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
                
def butterfly(request):
    return StreamingHttpResponse(gen(VideoCamera_butterfly()),
                    content_type='multipart/x-mixed-replace; boundary=frame')