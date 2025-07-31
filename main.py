#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import needed libraries
import glob
import json
import pandas
import ray
import time

# import module
from pkt_kg.downloads import OntData, LinkedData
from pkt_kg.edge_list import CreatesEdgeList
from pkt_kg.knowledge_graph import FullBuild, PartialBuild, PostClosureBuild


# In[ ]:


ont = OntData('resources/ontology_source_list.txt', 'resources/resource_info.txt')

ont.parses_resource_file()


# In[ ]:


ont.data_files = ont.source_list
ont.generates_source_metadata()


# In[ ]:


ont._writes_source_metadata_locally()


# In[ ]:


ont.resource_info


# In[ ]:


edges = LinkedData('resources/edge_source_list.txt', 'resources/resource_info.txt')

edges.parses_resource_file()


# In[ ]:


edges.data_files = edges.source_list
edges.generates_source_metadata()


# In[ ]:


edges._writes_source_metadata_locally()


# In[ ]:


edges.source_list.keys()


# In[ ]:


import psutil
# set-up environment for parallel processing -- even if running program serially these steps are needed
cpus = 1#psutil.cpu_count(logical=True)
#ray.shutdown()
ray.init()


# In[ ]:


# combine data sources
combined_edges = dict(edges.data_files, **ont.data_files)
resource_info_loc = './resources/resource_info.txt'

# initialize edge dictionary class
master_edges = CreatesEdgeList(data_files=combined_edges, source_file=resource_info_loc)
master_edges.runs_creates_knowledge_graph_edges(source_file=resource_info_loc, data_files=combined_edges, cpus=cpus)


# In[ ]:


master_edges = json.load(open('resources/Master_Edge_List_Dict.json', 'r'))


# In[ ]:


# <br><br>

# In[ ]:


# specify input arguments
build = 'full'
construction_approach = 'subclass'
add_node_data_to_kg = 'no'
add_inverse_relations_to_kg = 'yes'
decode_owl_semantics = 'yes'
kg_directory_location = './resources/knowledge_graphs'


# In[ ]:


# construct knowledge graphs
if build == 'partial':
    kg = PartialBuild(construction=construction_approach,
                      node_data=add_node_data_to_kg,
                      inverse_relations=add_inverse_relations_to_kg,
                      decode_owl=decode_owl_semantics,
                      cpus=cpus,
                      write_location=kg_directory_location)
elif build == 'post-closure':
    kg = PostClosureBuild(construction=construction_approach,
                          node_data=add_node_data_to_kg,
                          inverse_relations=add_inverse_relations_to_kg,
                          decode_owl=decode_owl_semantics,
                          cpus=cpus,
                          write_location=kg_directory_location)
else:
    kg = FullBuild(construction=construction_approach,
                   node_data=add_node_data_to_kg,
                   inverse_relations=add_inverse_relations_to_kg,
                   decode_owl=decode_owl_semantics,
                   cpus=cpus,
                   write_location=kg_directory_location)

kg.construct_knowledge_graph()
ray.shutdown()

