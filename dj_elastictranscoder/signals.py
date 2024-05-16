from django.dispatch import Signal

transcode_onprogress = Signal()
transcode_onerror = Signal()
transcode_oncomplete = Signal()
