import os
import distutils.util

DEBUG = bool(distutils.util.strtobool(os.getenv("DEBUG", default="True")))
USE_SEMAPHORE_FILE_STRATEGY = bool(distutils.util.strtobool(os.getenv("USE_SEMAPHORE_FILE_STRATEGY", default="True")))
SEMAPHORE_FILE = os.getenv("SEMAPHORE_FILE", default="/semaphore/sigterm.txt")
SEMAPHORE_FILE_ENSURE_REMOVED = bool(distutils.util.strtobool(os.getenv("DEBUG", default="True")))
SLEEP_SECONDS = float(os.getenv("SLEEP_SECONDS", default="0.5"))
SAY_HELLO_SECONDS = int(os.getenv("SAY_HELLO_SECONDS", default="30"))

USE_ECS_TASK_STRATEGY = bool(distutils.util.strtobool(os.getenv("USE_ECS_TASK_STRATEGY", default="False")))
ECS_TASK_STRATEGY_SEMAPHORE_FILE_TEMPLATE = os.getenv("ECS_TASK_STRATEGY_SEMAPHORE_FILE_TEMPLATE", default="/semaphore/##task_id##")
ECS_TASK_STRATEGY_ENDPOINT = os.getenv("ECS_CONTAINER_METADATA_URI", default=None)
