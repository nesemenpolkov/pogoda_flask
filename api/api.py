from flask import Blueprint, request
from api.api_ext import success, error
import pandas as pd

api = Blueprint("api", __name__)


@api.route("/api/makegraph", methods=["POST"])
def build_fucking_graph():
    data = request.get_json(force=True)
    data = data["data"]
    print(data)
    try:
        df = pd.DataFrame(data)
        print(df)
        list_of_nodes = set(df["f1"].tolist() + df["f2"].tolist())
        nodes = {}
        edges = {}
        layouts = {}
        node_counter = 1
        edge_counter = 1
        for _, row in df.iterrows():
            nodes[f"node{node_counter}"] = {"name": row["f1"]}
            nodes[f"node{node_counter + 1}"] = {"name": row["f2"]}
            edges[f"edge{edge_counter}"] = {"source": f"node{node_counter}",
                                            "target": f"node{node_counter + 1}",
                                            "label": row["r"]}
            layouts[f"node{node_counter}"] = {"x": node_counter, "y": node_counter}
            layouts[f"node{node_counter + 1}"] = {"x": node_counter + 1, "y": node_counter + 1}
            node_counter += 2
            edge_counter += 1
        print(nodes)
        return success({"nodes": nodes,
                        "edges": edges,
                        "layouts": layouts})
    except Exception as e:
        return error({"Message": str(e)})
