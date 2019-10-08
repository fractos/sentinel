# Sentinel

This script detects Unix signals and if received will perform an action, e.g. touch a file.

The use-case for this is in ECS where the containers of a Task need to know that they have been requested to stop and they should exit gracefully. This fills a gap where .Net Core has issues with receiving signals when run in daemon mode.

## Environment variables

| Name                          | Description                                                 | Default                |
|-------------------------------|-------------------------------------------------------------|------------------------|
| DEBUG                         | Show debug logging messages                                 | True                   |
| USE_SEMAPHORE_FILE_STRATEGY   | Use the strategy of touching a semaphore file               | True                   |
| SEMAPHORE_FILE                | Full path of the file to use as a semaphore                 | /semaphore/sigterm.txt |
| SEMAPHORE_FILE_ENSURE_REMOVED | Ensure that the semaphore file has been removed at startup  | True                   |
| SLEEP_SECONDS                 | Delay between lifecycle processing                          | 0.5                    |
| SAY_HELLO_SECONDS             | Delay between logging a "running" message to show its alive | 30                     |
