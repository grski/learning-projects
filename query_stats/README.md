# Query stats
Create a class that will store total time of execution for a given query. As an input you'll receive records, that will hold time of execution and an id. The records can contain query execution time for only a part of the whole query, meaning one query can have many records. In that case we want to sum these records for that given id.

Let that class have a `get_top_k_records` method that will return a given number of queries that had longest times.

```python
events = [
  {"id": 2, "partial_execution_time": 10},
  {"id": 1, "partial_execution_time": 15},
  {"id": 1, "partial_execution_time": 12},
  {"id": 3, "partial_execution_time": 25},
  {"id": 3, "partial_execution_time": 10},
  {"id": 4, "partial_execution_time": 15},
]
```
