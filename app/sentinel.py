from logzero import logger
import logging
import logzero
import signal
import os
import time
from pathlib import Path
import settings

requested_to_quit = False


def main():
    logger.info("starting...")

    setup_signal_handling()

    last_hello_emitted = time.time()

    if settings.USE_SEMAPHORE_FILE_STRATEGY:
        if settings.SEMAPHORE_FILE_ENSURE_REMOVED:
            logger.info("ensuring semaphore file at " + settings.SEMAPHORE_FILE + " is removed")
            semaphore_file = Path(settings.SEMAPHORE_FILE)
            if semaphore_file.exists():
                logger.info("semaphore file exists, removing")
                semaphore_file.unlink()

    while not requested_to_quit:
        age = int(time.time() - last_hello_emitted)
        if age > settings.SAY_HELLO_SECONDS:
            logger.info("running...")
            last_hello_emitted = time.time()

        time.sleep(settings.SLEEP_SECONDS)

    if requested_to_quit:
        if settings.USE_SEMAPHORE_FILE_STRATEGY:
            logger.info("touching semaphore file at " + settings.SEMAPHORE_FILE})
            Path(settings.SEMAPHORE_FILE).touch()

    logger.info("done")


def signal_handler(signum, frame):
    logger.info("Caught signal " + str(signum)")
    global requested_to_quit
    requested_to_quit = True


def setup_signal_handling():
    logger.info("setting up signal handling")
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    if settings.DEBUG:
        logzero.loglevel(logging.DEBUG)
    else:
        logzero.loglevel(logging.INFO)

    main()
