import pandas as pd 
from queue import PriorityQueue 
from main import src,dest 

'''src_name = None
dest_name = None
def process_data(src, dest):
    print(src, dest)
    src_name=src
    dest_name = dest'''

graph = {
  
    'A1': {'A3', 'A23',  'A39',  'A13','A10','A39'},
    'A2': {'A39', 'A14',  'A26',  'A38', 'A39', 'A41'},
    'A3': {'A1', 'A6',  'A1',  'A13',  'A24', 'A5'},
    'A4': {'A15', 'A5',  'A35','A7'},
    'A5': {'A7',  'A4',  'A35','A3'},
    'A6': {'A45', 'A15', 'A13','A3'},
    'A7': {'A5',  'A4', 'A31', 'A32'},
    'A8': {'A11', 'A27', 'A35'},
    'A9': {'A40', 'A32', 'A30', 'A11'},
    'A10': {'A29', 'A42', 'A46', 'A1', 'A23'},
    'A11': {'A8', 'A30', 'A12', 'A27'},
    'A12': {'A33', 'A27', 'A38','A11'},
    'A13': {'A34', 'A3', 'A1','A6'},
    'A14': {'A16', 'A2'},
    'A15': {'A6', 'A45', 'A4'},
    'A16': {'A14', 'A36'},
    'A17': {'A37', 'A45'},
    'A18': {'A48', 'A49', 'A31'},
    'A19': {'A43'},
    'A20': {'A31'},
    'A21': {'A37', 'A34'},
    'A22': {'A25'},
    'A23': {'A1', 'A46','A10'},
    'A24': {'A42', 'A3'},
    'A25': {'A22', 'A46'},
    'A26': {'A33', 'A2'},
    'A27': {'A8', 'A11','A12','A35'},
    'A28': {'A36', 'A39','A41'},
    'A29': {'A10', 'A42'},
    'A30': {'A44', 'A11', 'A9'},
    'A31': {'A18', 'A20', 'A7'},
    'A32': {'A40', 'A7','A9'},
    'A33': {'A44', 'A12', 'A26'},
    'A34': {'A13', 'A2', 'A21','A38'},
    'A35': {'A27', 'A8', 'A5'},
    'A36': {'A16', 'A28','A41'},
    'A37': {'A21', 'A17'},
    'A38': {'A34', 'A12', 'A2'},
    'A39': {'A2', 'A1', 'A28'},
    'A40': {'A9', 'A32'},
    'A41': {'A28', 'A36', 'A39','A2'},
    'A42': {'A24', 'A10', 'A29'},
    'A43': {'A19', 'A49'},
    'A44': {'A30', 'A12', 'A33'},
    'A45': {'A6', 'A17', 'A35', 'A15'},
    'A46': {'A10', 'A23', 'A25'},
    'A48': {'A43', 'A9', 'A18', 'A31'},
    'A49': {'A18', 'A43'}
}

h = {
    'A1': 50,
    'A2': 50,
    'A3': 10,
    'A4': 50,
    'A5': 30,
    'A6': 10,
    'A7': 10,
    'A8': 10,
    'A9': 80,
    'A10': 50,
    'A11': 10,
    'A12': 10,
    'A13': 10,
    'A14': 80,
    'A15': 30,
    'A16': 20,
    'A17': 10,
    'A18': 20,
    'A19': 20,
    'A20': 50,
    'A21': 50,
    'A22': 30,
    'A23': 20,
    'A24': 10,
    'A25': 20,
    'A26': 20,
    'A27': 10,
    'A28': 10,
    'A29': 10,
    'A30': 40,
    'A31': 40,
    'A32': 20,
    'A33': 10,
    'A34': 50,
    'A35': 40,
    'A36': 50,
    'A37': 20,
    'A38': 20,
    'A39': 10,
    'A40': 50,
    'A41': 20,
    'A42': 30,
    'A43': 20,
    'A44': 50,
    'A45': 20,
    'A46': 30,
    'A48': 10,
    'A49': 10,

}

def best_first_search(graph, start, goal, h):
    visited = set()
    queue = PriorityQueue()
    queue.put((h[start], [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][-1]

        if current == goal:
            return node[1]

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    path = node[1][:]
                    path.append(neighbor)
                    queue.put((h[neighbor], path))

    return None



df = pd.read_excel('first.xlsx')
src='Mannivakkam, Tamil Nadu'
dest='Tondiarpet, Chennai, Tamil Nadu'

ID1 = df.loc[df['Place'] == src]['KeyID'].values[0]
ID2 = df.loc[df['Place'] == dest]['KeyID'].values[0]

path = best_first_search(graph, ID1,ID2, h) 






places = []
for id in path:
    addpoint = df.loc[df['KeyID'] == id]['Place'].values[0] 
    places.append(addpoint)
