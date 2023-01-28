# Schedules
It's app for schedules

## Notes
- Local UTC offset: ```int(datetime.datetime.now(datetime.timezone.utc).astimezone().utcoffset().seconds/3600)```
- Local time for logs: ```now = datetime.now() now.strftime("%Y-%m-%d-%H-%M-%S") = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")```