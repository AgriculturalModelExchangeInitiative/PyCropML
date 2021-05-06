
# coding: utf-8

from pycropml.transpiler.pseudo_tree import Node

class MetaExtraction():
    def __init__(self):
        self.parameters = {}
        self.getTree = []
    
    def getTypeNode(self, tree, nodetype, change=True):
        """get nodes of type nodetype

        Args:
            tree (Node): a tree in where the nodes are searched
            nodetype (str): the type of the nodes
            change (bool, optional): check if it is the same type of node which is searched. Defaults to True.
        """
        if change:
            self.getTree = []
            change = False
        if isinstance(tree, Node):
            if tree.type == nodetype:
                self.getTree.append(tree)
            for field, child in tree.__dict__.items():
                ztree = getattr(tree, field)
                if isinstance(ztree, Node):
                    self.getTypeNode(ztree, nodetype, False)
                if isinstance(ztree, list):
                    self.translist(ztree, nodetype)
        elif isinstance(tree, list):
            self.translist(tree, nodetype)   
        else:
            return 
                        
    def translist(self, tree, nodetype):
        for ch in tree:
            self.getTypeNode(ch, nodetype, False) 
    

    def getAttNode(self, tree, **attVal):
        """
        get the nodes (as a tree) with a specific value of attribute 

        Args:
            tree (Node): a tree in which the node will be searched
            attValue (dict): the value and the attribute of the node

        Returns:
            List[Node]: a list of nodes 
        """
        nodes = []
        for node in tree:
            check = [getattr(node,attName) == attValue for attName, attValue in attVal.items() if attName in dir(node)]
            if all(check):
                nodes.append(node)
        return nodes
    
    def getmethod(self, tree, nameMethod):
        """This method return a specific method name. It can be used to get the algorithm

        Args:\n
            - tree (Node): a tree where the method will be extracted \n
            - nameMethod (str): the name of the method described 

        Returns:
            Node: a specific method
        """
        self.getTypeNode(tree, "methodDef")
        methNode = self.getTree
        meth = self.getAttNode(methNode,**{"name":nameMethod})
        return meth[0] if meth else []
    



