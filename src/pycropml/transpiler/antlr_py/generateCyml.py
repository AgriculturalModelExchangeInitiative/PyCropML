from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
from pycropml.transpiler.ast_transform import transform_to_syntax_tree


def writeCyml(node):
    """Generate CyML code from an ASG 

    Args:
        node (Node): Common Abstract Syntax Graph

    Returns:
        [str]: CyML code
    """
    p = CymlGenerator(node)
    p.visit(node)
    code= ''.join(p.result)
    return code