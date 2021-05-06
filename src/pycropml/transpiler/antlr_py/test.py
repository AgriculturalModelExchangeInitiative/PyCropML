
from __future__ import absolute_import
from __future__ import print_function
from path import Path
import os
from pycropml.transpiler.antlr_py.to_CASG import to_CASG
from pycropml.transpiler.antlr_py.bioma.biomaExtraction import BiomaExtraction
from pycropml.transpiler.pseudo_tree import Node
from pycropml.transpiler.antlr_py.csharp import cs_cyml
from pycropml.transpiler.generators.cymlGenerator import CymlGenerator
from pycropml.transpiler.ast_transform import transform_to_syntax_tree
from pycropml.transpiler.antlr_py.generateCyml import writeCyml
from pycropml.transpiler.antlr_py.createUnit import Pl2Crop2ml

""" Read BioMA component and extract metadata

"""

cwd = Path(__file__).dirname()
data = cwd/'examples'/'SiriusComponent'/'phenology'/'Strategies'

compositeStrat= data.glob('*Component.cs')[0]
simpleStrat = [f for f in data.glob('*.cs')  if f not in compositeStrat]

data = cwd/'examples'/'SiriusComponent'/'phenology'/'DomainClass'
varInfo = data.glob('*VarInfo.cs')

output = cwd/'examples'/'SiriusComponent'/'phenology'
crop2ml_rep = Path(os.path.join(output, 'crop2ml'))
if not crop2ml_rep.isdir():
    crop2ml_rep.mkdir()
algo_rep = Path(os.path.join(crop2ml_rep, 'algo'))
if not algo_rep.isdir():
    algo_rep.mkdir()
cyml_rep = Path(os.path.join(algo_rep, 'pyx'))
if not cyml_rep.isdir():
    cyml_rep.mkdir()


vinfoAsg = []
for v in varInfo:
    asg = to_CASG(v, 'cs')
    vinfoAsg.append(asg)

models = []
for strat in simpleStrat:
    print(strat)
    strAsg = to_CASG(strat,'cs')
    z = BiomaExtraction()
    p2 = z.prec_cur_states(strAsg)
    funcs = z.externFunction(strAsg)
    algo = z.getAlgo(strAsg)
    var =  z.totalvar(strAsg)
    cd = cs_cyml.Cs_Cyml_ast(algo.block, var = var)
    h = cd.transform()
    nd = transform_to_syntax_tree(h)
    code = writeCyml(nd)
    filename = Path(os.path.join(cyml_rep, "%s.pyx"%(strat.basename().split(".")[0])))
    with open(filename, "wb") as tg_file:
        tg_file.write(code.encode('utf-8'))
    
    if funcs:
        for m in funcs:
            cd = cs_cyml.Cs_Cyml_ast(m)
            h = cd.transform()
            nd = transform_to_syntax_tree(h)
            code = writeCyml(nd)
            filename = Path(os.path.join(cyml_rep, "%s.pyx"%(m.name)))
            with open(filename, "wb") as tg_file:
                tg_file.write(code.encode('utf-8'))
    
    z.modelunit(strAsg,vinfoAsg)
    models.append(z.model)
    xml_ = Pl2Crop2ml(z.model, "SQ.Pheno_Pkg").run()
    filename = Path(os.path.join(crop2ml_rep, "unit.%s.xml"%(strat.basename().split(".")[0])))
    with open(filename, "wb") as xml_file:
        xml_file.write(xml_.unicode(indent=4).encode('utf-8'))


