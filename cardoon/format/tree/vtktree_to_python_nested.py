from cardoon.format import vtkrow_to_dict
import vtk

def process_node(vtknode, node):
    num_children = input.GetNumberOfChildren(vtknode)
    if num_children > 0:
        node["children"] = []
    for c in range(num_children):
        vtkchild = input.GetChild(vtknode, c)
        v = vtkrow_to_dict(input.GetVertexData(), vtkchild)
        edge = vtk.vtkGraphEdge()
        input.GetInEdge(vtkchild, 0, edge)
        vtkparentedge = edge.GetId();
        e = vtkrow_to_dict(input.GetEdgeData(), vtkparentedge)
        n = {"edge_data": e, "node_data": v}
        process_node(vtkchild, n)
        node["children"].append(n)

vtkroot = input.GetRoot()
output = {"node_data": vtkrow_to_dict(input.GetVertexData(), vtkroot)}
process_node(vtkroot, output)
