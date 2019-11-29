import json
import sys
print(sys.argv[1])
file_trace = sys.argv[1]#'create_delete_1.json'
with open(str(file_trace)) as trace_file:
    trace_json = json.load(trace_file)

# Trace IDs for create-delete list
for i in range(len(trace_json['tasks'][0]['subtasks'][0]['workloads'][0]['data'])):
    print(trace_json['tasks'][0]['subtasks'][0]['workloads'][0]['data'][i]['output']['complete'][0]['data']['trace_id'])

