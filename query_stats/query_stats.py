import pandas as pd

events = [
  {"id": 2, "partial_execution_time": 10},
  {"id": 1, "partial_execution_time": 15},
  {"id": 1, "partial_execution_time": 12},
  {"id": 3, "partial_execution_time": 25},
  {"id": 3, "partial_execution_time": 10},
  {"id": 4, "partial_execution_time": 15},
]

def calculate_execution_time(events):

    total_time = [event['partial_execution_time'] for event in events]
    print(sum(total_time))
    return sum(total_time)

class Record:
    total_partial_execution_time = 0
    def __init__(self, id, partial) -> None:
        self.id = id
        self.partial_execution_time = partial
        self.new_dict = dict()
        Record.total_partial_execution_time += partial
    

    def get_top_k_records(self, query, k):
        for event in query:
            # print(f"{event['id']} {event['partial_execution_time']}")     
            if event['id'] in self.new_dict:
                self.new_dict[event['id']] += event['partial_execution_time']
            else:
                self.new_dict[event['id']] = event['partial_execution_time']
        
        sorted_dict = dict(sorted(self.new_dict.items(), key=lambda x:x[1], reverse=True))
        first_k_values = {item: sorted_dict[k] for item in list(sorted_dict)[:k]}
        return first_k_values
    # sorted_query = query.sort(key='partial_execution_time')
    # print(sorted_query)



record1 = Record(2, 10)


print(record1.get_top_k_records(events, 4))

# print(Events(events).df)

# print(pd.Series(events))

# print(record2.total_partial_execution_time)
# calculate_execution_time(events)