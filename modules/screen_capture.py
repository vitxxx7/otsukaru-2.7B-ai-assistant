from mss import mss
import configparser

class ScreenCapturer:
    def __init__(self):
        self.cfg = self._load_config()
        
    def _load_config(self):
        # Load screen_config.yaml
        ...