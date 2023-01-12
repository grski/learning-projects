# Logs stats
1. You are given a large log file which stores user interactions with an application. The entries in the log file follow the following schema: `{userId, timestamp, actionType}`. Calculate the average session time across all users. Assume that data yet get is valid and not sorted in any way. Assume that number of records that are `opens` will be equal to `closes`.
2. What if we want to modify the code to also calculate average session time per user?

```python
# User level 1 -> 1512, 2-> 17
events = [
    [1, 1435459573, "Close"], [1, 1435456566, "Open"],
    [1, 1435462567, "Open"], [1, 1435462584, "Close"],
    [1, 1435462567, "Open"], [1, 1435462584, "Close"],
    [2, 1435462567, "Open"], [2, 1435462584, "Close"]
]
```

