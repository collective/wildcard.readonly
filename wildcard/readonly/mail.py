

def send(self, *args, **kwargs):
    if 'immediate' not in kwargs:
        kwargs['immediate'] = True
    return self._old_send(*args, **kwargs)
