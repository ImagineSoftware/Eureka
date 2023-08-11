import imutils, cv2
from imutils.video import VideoStream
import time

class Camera():
    def __init__(self,height = 300, width = 350):
        self.height = height
        self.width = width
        
    def start_capture(self, height=None, width=None, usingPiCamera= None, ):
        resolution = (self.height, self.width)
        if height:
            if width:
                resolution = (height, width)
        # cf = VideoStream(usePiCamera=usingPiCamera,resolution=resolution,framerate=30).start()
        cf = VideoStream(src=0).start()
        self.current_frame = cf
        time.sleep(0.5)

        if not usingPiCamera:
            frame = imutils.resize(self.current_frame.read(), width=resolution[0], height=resolution[1])
            
            ret, jpeg = cv2.imencode('.jpg', frame)
            
            return jpeg.tostring()
            
        # return {}