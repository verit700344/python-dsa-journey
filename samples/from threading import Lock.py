from threading import Lock
class trafic_signal:
    def __init__(self):
        self.lock=Lock()
        self.cgr=1
    def carArraived(self,roadid,carid,crosscar,direction ,turngreen):
        with self.lock:
            target_road=1 if roadid in [1,3] else 2
            if self.cgr != target_road:
                turngreen()
                self.cgr = target_road
            crosscar


