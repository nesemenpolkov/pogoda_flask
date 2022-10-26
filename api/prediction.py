import networkx as nx
import pandas as pd
import numpy as np


def get_predictions(df):
    graph = nx.from_pandas_edgelist(df, "f1", "f2", ["r"])
    preds = nx.adamic_adar_index(graph)
    pred_list = []
    for u, v, p in preds:
        obj = {
            "node1": u,
            "node2": v,
            "probability": p
        }
        pred_list.append(obj)
    return pred_list
