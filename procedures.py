# JSON
import json
import json_stream
#import csv
from Tree import Tree


def extract_trees_bcn(filename):
    """
  Input: Barcelona trees File
  Output: List of Trees in Barcelona
  """
    with open("data/Trees_Barcelona.json") as fil:
        json_trees = json.load(fil)
        tree_list = []
        i = 0
        for tree in json_trees:
            i = i + 1
            t = Tree(ident=i,
                     address=tree['adreca'],
                     coordinates=(tree['latitud'], tree['longitud']),
                     species=tree['nom_cientific'])
            tree_list.append(t)
    return tree_list





  

def extract_trees_bcn_stream(filename):
  bcn_trees = []
  with open(filename) as trees_json:
    record_list = json_stream.load(trees_json)
    i = 0
    for record in record_list.persistent():
      i = i+1
      params_dict = get_input_params(record)
      bcn_trees.append(Tree(ident=i,
                            address=params_dict['address'],
                            species=params_dict['species'],
                            coordinates=params_dict['coordinates']))     
  return bcn_trees
        






def get_input_params(recs):
    if 'nom_cientific' in recs.keys():
        species = recs['nom_cientific']
    else:
        species = ''
    if 'adreca' in recs.keys():
        address = recs['adreca']
    else:
        address = ''
    if 'latitud' in recs.keys() and 'longitud' in recs.keys():
        coords = (recs['latitud'], recs['longitud'])
    else:
        coords = (0, 0)
    return {'species': species, 'address': address, 'coordinates': coords}
