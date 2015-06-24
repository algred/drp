import json
from subprocess import call

data = json.loads(open('activity_net.json').read())
data = data['database']

## Collects the list of action classes.
ind = 0
action_class = dict()
for k in data:
  annot = data[k]['annotations']
  for a in annot:
    if not a in action_class.keys():
      action_class[a] = ind
      ind = ind + 1


