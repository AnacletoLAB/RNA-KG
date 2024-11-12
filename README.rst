***********************************************************************************
RNA-KG: An ontology-based KG for representing interactions involving RNA molecules
***********************************************************************************

RNA-KG is a knowledge graph encompassing biological knowledge about RNAs gathered from `more than 60 public databases`_, integrating functional relationships with genes, proteins, and chemicals and ontologically grounded biomedical concepts. RNA-KG can be both used by directly exploring and visualizing the KG, and by applying computational methods to analyze and infer bio-medical knowledge. RNA-KG is constantly maintained and updated with new experimental data. 

|metagraph|

What Does This Repository Provide?
===================================
Notebooks and pointers to (processed) data and ontologies to build the current release of RNA-KG.

Releases
========= 
  - `RNA-KG's website is available at the following link: https://RNA-KG.anacleto.di.unimi.it. The list of RNA-KG nodes is stored in https://RNA-KG.anacleto.di.unimi.it/nodes.csv; the list of RNA-KG edges is stored in https://RNA-KG.anacleto.di.unimi.it/edges.csv`
  - `Public SPARQL endpoint is available at the following link: https://blazegraph-RNA-KG.anacleto.di.unimi.it`
  - Please see our paper: https://www.nature.com/articles/s41597-024-03673-7
  - `Data Access: https://doi.org/10.5281/zenodo.10078877`

|

---------------------------------

********************************
Generate RNA-KG current release
********************************


Download Data
=============
RNA-KG is built and maintained using `PheKnowLator <https://github.com/callahantiff/PheKnowLator>`_. PheKnowLator requires three documents within the ``resources`` directory to run successfully. Please make sure the documents listed below are present in the specified location prior to constructing RNA-KG. They can all be accessed at the following link: https://doi.org/10.5281/zenodo.10078877.


* `resources/resource_info.txt`_
* `resources/ontology_source_list.txt`_
* `resources/edge_source_list.txt`_
* `resources/construction_approach/subclass_construction_map.pkl`
* `resources/knowledge_graphs/PheKnowLator_MergedOntologies.owl`
* `resources/relations_data/RELATIONS_LABELS.txt`
* `resources/relations_data/INVERSE_RELATIONS.txt`

To generate these data yourself, please see the `RNA-KG_Preparation.ipynb`_ and `inteRNA-KG_Preparation.ipynb`_ Jupyter Notebooks.


Construct RNA-KG
================

RNA-KG current release can be generated via the provided `main.ipynb`_ Jupyter Notebook. The adopted PheKnowLator's KG build model is shown below.

.. code:: python

 # PheKnowLator's full build, instance construction approach, with inverse relations, no node metadata, and decode owl (OWL-NETS)
 kg = FullBuild(construction='instance',
                node_data='no',
                inverse_relations='yes',
                decode_owl='yes',
                cpus=psutil.cpu_count(logical=True),
                write_location='./resources/knowledge_graphs')

 kg.construct_knowledge_graph()

******************************
Get In Touch or Get Involved
******************************

Contact Us
==========
Don't hesitate to contact us, especially if you believe a new data source should be integrated into RNA-KG. To get in touch with us, please `create an issue`_ or `send us an email`_ 📩. 

***********
Future work
***********

We are currently working on enhancing the proposed KG in different directions.

- Application of Graph Representation Learning methods to analyze RNA-KG.
- Identification of key (nodes and edges') properties associated with RNA molecules and their interactors ➞ ⚠️experimental⚠️ Neo4j endpoint available at http://fievel.anacleto.di.unimi.it:7474 (usr: anacleto; pwd: anacleto). The list of RNA-KG nodes including properties is stored in https://RNA-KG.anacleto.di.unimi.it/nodes_with_properties.csv; the list of RNA-KG edges including properties is stored in https://RNA-KG.anacleto.di.unimi.it/edges_with_properties.csv
- Development of an RNA Ontology with a particular emphasis on non-coding RNA molecules.
- Specification of our meta-graph in terms of LinkML ➞ `SPIRES engine (OntoGPT) <https://github.com/monarch-initiative/ontogpt>`_.
- Development of graphical facilities for supporting the user in the data acquisition process and thus reducing the manual effort required for mapping the data available in the different data sources into RNA-KG.

***********
Attribution
***********

Licensing
==========
This project is licensed under Apache License 2.0 - see the `LICENSE.md`_ file for details.

Citing RNA-KG
=================
Please cite the following paper if it was useful for your research:

.. code:: bib

  @article{Cavalleri2024rnakg,
      title="An ontology-based knowledge graph for representing interactions involving RNA molecules", 
      author="Emanuele Cavalleri and Alberto Cabri and Mauricio Soto-Gomez and Sara Bonfitto and Paolo Perlasca and Jessica Gliozzo and Tiffany J. Callahan and Justin Reese and Peter N Robinson and Elena Casiraghi and Giorgio Valentini and Marco Mesiti",
      year="2024",
      journal="Sci. Data",
      publisher="Springer Science and Business Media LLC",
      volume=11,
      number=1,
      pages="906",
      month=aug,
      year=2024,
      copyright="https://creativecommons.org/licenses/by-nc-nd/4.0",
      language="en"
  }

.. |metagraph| image:: images/metagraph.png
    :target: https://raw.githubusercontent.com/AnacletoLAB/RNA-KG/main/images/metagraph.png
    :alt: Metagraph

.. _LICENSE.md: https://github.com/AnacletoLAB/RNA-KG/blob/main/LICENSE

.. _`send us an email`: https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&to=emanuele.cavalleri@unimi.it&cc=marco.mesiti@unimi.it

.. _`create an issue`: https://github.com/AnacletoLAB/RNA-KG/issues/new/choose

.. _`more than 60 public databases`: https://github.com/AnacletoLAB/RNA-KG/tree/main/resources#readme

.. _`Discussion`: https://github.com/AnacletoLAB/RNA-KG/discussions

.. _`main.ipynb`: https://github.com/AnacletoLAB/RNA-KG/blob/main/main.ipynb

.. _`RNA-KG_Preparation.ipynb`: https://github.com/AnacletoLAB/RNA-KG/blob/main/notebooks/RNA-KG_Preparation.ipynb

.. _`inteRNA-KG_Preparation.ipynb`: https://github.com/AnacletoLAB/RNA-KG/blob/main/notebooks/inteRNA-KG_Preparation.ipynb

.. _`resources/resource_info.txt`: https://github.com/AnacletoLAB/RNA-KG/blob/main/resources/resource_info.txt

.. _`resources/ontology_source_list.txt`: https://github.com/AnacletoLAB/RNA-KG/blob/main/resources/ontology_source_list.txt

.. _`resources/edge_source_list.txt`: https://github.com/AnacletoLAB/RNA-KG/blob/main/resources/edge_source_list.txt
