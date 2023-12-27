import cv2


class Sight:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"Sight started on camera {self.camera_index}")

    def stop(self):
        self.is_running = False
        self.cap.release()
        print(f"Sight stopped on camera {self.camera_index}")

    def process_frame(self):
        if not self.is_running:
            raise RuntimeError("Cannot process frame, Sight is not running")
        ret, frame = self.cap.read() 
        if not ret:
            raise RuntimeError("Could not capture frame")

        processed_frame = frame
        return processed_frame
