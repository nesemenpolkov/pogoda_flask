from flask import Blueprint, request
from api.api_ext import success, error
import pandas as pd
from api.prediction import get_predictions

api = Blueprint("api", __name__)


@api.route("/api/makegraph", methods=["POST"])
def build_fucking_graph():
    data = request.get_json(force=True)
    get_pred = data.get("flag", None)
    data = data["data"]
    print(get_pred)
    try:
        df = pd.DataFrame(data)

        nodes = {}
        edges = {}
        layouts = {}
        edge_counter = 1
        unique_nodes = []
        node_to_num = {}
        for _, row in df.iterrows():
            if row["f1"] not in unique_nodes:
                unique_nodes.append(row["f1"])
                node_to_num[row["f1"]] = len(unique_nodes)
                nodes[f"node{node_to_num[row['f1']]}"] = {"name": row["f1"]}
                layouts[f"node{node_to_num[row['f1']]}"] = {"x": node_to_num[row['f1']],
                                                            "y": node_to_num[row['f1']]}

            f1 = row["f1"]
            f1_n = node_to_num[f1]

            if row["f2"] not in unique_nodes:
                unique_nodes.append(row["f2"])
                node_to_num[row["f2"]] = len(unique_nodes)
                nodes[f"node{node_to_num[row['f2']]}"] = {"name": row["f2"]}
                layouts[f"node{node_to_num[row['f2']]}"] = {"x": node_to_num[row['f2']],
                                                            "y": node_to_num[row['f2']]}

            f2 = row["f2"]
            f2_n = node_to_num[f2]

            edges[f"edge{edge_counter}"] = {"source": f"node{f1_n}",
                                            "target": f"node{f2_n}",
                                            "label": row["r"]}
            edge_counter += 1

        if not get_pred:
            return success({"nodes": nodes,
                            "edges": edges,
                            "layouts": layouts})
        else:
            return success({"nodes": nodes,
                            "edges": edges,
                            "layouts": layouts,
                            "table": get_predictions(df)})
    except Exception as e:
        return error({"Message": str(e)})
