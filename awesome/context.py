import os
import sys
from contextlib import contextmanager
from cStringIO import StringIO
import time
from .iterator import consume


@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


@contextmanager
def consuming(iterator):
    try:
        yield iterator
    finally:
        consume(iterator, None)


@contextmanager
def calling(callable, *args, **kwargs):
    try:
        yield
    finally:
        callable(*args, **kwargs)


@contextmanager
def change_directory(path):
    original_path = os.getcwdu()

    os.chdir(path)

    try:
        yield

    finally:
        os.chdir(original_path)


@contextmanager
def redirect_stdout(stream=None):
    if stream is None:
        stream = StringIO()

    original_stdout = sys.stdout
    sys.stdout = stream

    try:
        yield stream

    finally:
        sys.stdout = original_stdout


@contextmanager
def redirect_stderr(stream=None):
    if stream is None:
        stream = StringIO()

    original_stderr = sys.stderr
    sys.stderr = stream

    try:
        yield stream

    finally:
        sys.stderr = original_stderr


class Timer(object):
    def __init__(self):
        self._start_time = None
        self._end_time = None

    def __enter__(self):
        self._start_time = time.clock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end_time = time.clock()

    @property
    def running(self):
        return self._end_time is None and self._start_time is not None

    @property
    def terminated(self):
        return self._end_time is not None


    @property
    def elapsed(self):
        if self._end_time is None:
            return time.clock() - self._start_time

        return self._end_time - self._start_time

    def __repr__(self):
        return "Timer(elapsed={}, running={})".format(self.elapsed, self.running)
