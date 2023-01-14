
events = [
    [1, 1435459573, "Close"], [1, 1435456566, "Open"],
    [1, 1435462567, "Open"], [1, 1435462584, "Close"],
    [1, 1435462567, "Open"], [1, 1435462584, "Close"],
    [2, 1435462567, "Open"], [2, 1435462584, "Close"],
    [3, 1435459573, "Close"], [1, 1435456566, "Open"],
    [3, 1435459521, "Close"], [1, 1435456566, "Open"],

]

def calculate_timestamps(timestamps_list, divider=1):
    full_time = [abs(timestamps_list[(i-1)]-timestamps_list[i]) for i in range(1, len(timestamps_list), 2)]
    return sum(full_time)/divider

def timestamp_list(events_list):
    timestamp = list()
    for event in events_list:
        timestamp.append(event[1])
    return timestamp
 
def portion_list(events_list):
    userids = list()
    timestamps = list() 
    returned_data = list()
    final_list = dict()
    user_counter = 0
    for event in events_list:
        if event[0] not in userids:
            userids.append(event[0])
            final_list[event[0]] = event[1]
            if userids[user_counter-1] is not event[0]:
                returned_data.append(timestamps) 
                timestamps = list()
            returned_data.append(event[0])  
            user_counter+=1
        final_list[event[0]] = timestamps
        timestamps.append(event[1])
    returned_data.append(timestamps)
    # print(final_list)
    return final_list

def get_avarage_time_across_all_users(events, userid):
    avarage = calculate_timestamps(portion_list(events)[userid], len(portion_list(events)[userid])/2)
    return avarage

print(portion_list(events)[3])
print(get_avarage_time_across_all_users(events, 2))
# print(calculate_timestamps(timestamps2, len(timestamps2)/2))
# print(timestamp_list(events))
# print(calculate_timestamps(portion_list(events)[1], len(portion_list(events)[1])/2))
# print(calculate_timestamps(portion_list(events)[2], len(portion_list(events)[2])/2))

