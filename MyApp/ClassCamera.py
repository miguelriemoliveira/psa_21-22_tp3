import cv2

from ClassAbstractHardware import ClassAbstractHardware


class ClassCamera(ClassAbstractHardware):

    def __init__(self):
        super().__init__()
        self.image = None

    def _connect(self, device):
        self.vc = cv2.VideoCapture(device)
        return True

    def _disconnect(self):
        self.vc.release()
        return False

    def _getData(self):
        success, self.image = self.vc.read()  # get new image from camera
        return success

    def _setData(self):
        print('Cannot write tanything to camera!')
        return False
