from logzero import logger
import logging
import logzero
import signal
import os
import os.path
import time
import requests
import json
import settings

requested_to_quit = False


def main():
    logger.info("starting...")

    setup_signal_handling()

    last_hello_emitted = time.time()

    semaphore_file = settings.SEMAPHORE_FILE

    if settings.USE_ECS_TASK_STRATEGY:
        logger.info("using ECS Task strategy for semaphore token")

        if len(settings.ECS_TASK_STRATEGY_ENDPOINT) is None:
            logger.fatal("ECS_TASK_STRATEGY_ENDPOINT was empty")
            return

        r = requests.get(settings.ECS_TASK_STRATEGY_ENDPOINT)
        metadata = r.json()
        logger.debug("metadata was: " + json.dumps(metadata))
        task_id = metadata["Labels"]["com.amazonaws.ecs.task-arn"].split("/")[-1]
        logger.debug("task_id: " + task_id)
        semaphore_file = settings.ECS_TASK_STRATEGY_SEMAPHORE_FILE_TEMPLATE.replace("##task_id##", task_id)
        logger.info("semaphore file set to " + semaphore_file)

    if settings.USE_SEMAPHORE_FILE_STRATEGY:
        if settings.SEMAPHORE_FILE_ENSURE_REMOVED:
            logger.info("ensuring semaphore file at " + semaphore_file + " is removed")

            if os.path.isfile(semaphore_file):
                logger.info("semaphore file exists, removing")
                os.unlink(semaphore_file)

    while not requested_to_quit:
        age = int(time.time() - last_hello_emitted)
        if age > settings.SAY_HELLO_SECONDS:
            logger.info("running...")
            last_hello_emitted = time.time()

        time.sleep(settings.SLEEP_SECONDS)

    if requested_to_quit:
        if settings.USE_SEMAPHORE_FILE_STRATEGY:
            logger.info("touching semaphore file at " + semaphore_file)
            open(semaphore_file, 'a').close()

    logger.info("done")


def signal_handler(signum, frame):
    logger.info("Caught signal " + str(signum))
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
