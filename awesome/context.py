import os
import sys
from contextlib import contextmanager
from cStringIO import StringIO


@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


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