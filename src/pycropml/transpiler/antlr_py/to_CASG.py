from pycropml.transpiler.antlr_py import parse, simplifyAntlrTree
from  pycropml.transpiler.antlr_py.csharp  import csharpTransformer
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from path import Path
import pycropml.transpiler.antlr_py

languages = ['cs',"bioma"]
NAMES = {'cs':'csharp','sirius':'csharp',"bioma":"csharp"}

GENERATORS = {
    format: getattr(getattr(
                    pycropml.transpiler.antlr_py,
                    '%s' % NAMES[format]), '%sTransformer'% NAMES[format])
    for format in languages
}

def to_CASG(filePath, language):
    """Transform CST provided from ANTLR parsers into a common ASG

    Args:
        filePath (Path): path of the class

    Returns:
        Node: A common Abstract Semantic Graph CASG
    """
    tree = parse.parsef(filePath,language, start="compilation_unit", strict=False)
    ast_proc = simplifyAntlrTree.process_tree(tree,transformer_cls =GENERATORS[language].Transformer )
    trans = GENERATORS[language].AstTransformer(ast_proc).transformer()
    #print(trans)
    csag= transform_to_syntax_tree(trans["body"])[0]
    return csag