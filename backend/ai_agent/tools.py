from langchain_core.tools import tool

# Define tools for AI to use
@tool
def get_nodes() -> int:
    """ Returns the total number of nodes for the current user"""
    return 20


# def insert_node_space(node_name: str, parent_node_name: str = None) -> int:
#     """
#     Returns the total number of items or nodes in the system.
#     If user didn't tell you about parent node name put 0
#     """
#     # Your database logic here (e.g., querying thoughtsravel or nodes table)
#     return 42
