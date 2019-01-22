import os

class Config:

    def __init__(self):
        self.server = os.environ.get('NATLAS_SERVER_ADDRESS') or 'http://127.0.0.1:5000'
        self.max_threads = os.environ.get('NATLAS_MAX_THREADS') or 3
        self.scan_timeout = os.environ.get('NATLAS_SCAN_TIMEOUT') or 360 # seconds, 6 minutes default
        self.scan_local = os.environ.get('NATLAS_SCAN_LOCAL') or False
        self.request_timeout = os.environ.get('NATLAS_REQUEST_TIMEOUT') or 15 # seconds
        self.backoff_max = os.environ.get('NATLAS_BACKOFF_MAX') or 300 # seconds, 5 minutes default
        self.backoff_base = os.environ.get('NATLAS_BACKOFF_BASE') or 1 # seconds