import os
import distutils.util

DEBUG = bool(distutils.util.strtobool(os.getenv("DEBUG", default="True")))
USE_SEMAPHORE_FILE_STRATEGY = os.getenv("USE_SEMAPHORE_FILE_STRATEGY", default="True")
SEMAPHORE_FILE = os.getenv("SEMAPHORE_FILE", default="/semaphore/sigterm.txt")
SEMAPHORE_FILE_ENSURE_REMOVED = bool(distutils.util.strtobool(os.getenv("DEBUG", default="True")))
SLEEP_SECONDS = float(os.getenv("SLEEP_SECONDS", default="0.5"))
SAY_HELLO_SECONDS = int(os.getenv("SAY_HELLO_SECONDS", default="30"))
