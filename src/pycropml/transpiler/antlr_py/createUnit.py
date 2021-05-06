from py.xml import Namespace



class ns(Namespace):
    "Custom xml namespace"

class Pl2Crop2ml(object):
    """ Export a platform component into a Crop2ML Model unit.

    """
    def __init__(self, md, pkgname):
        """ Export a workflow into Crop.

        :Parameters:
          - md : A platform component metainformation

        """
        self.md = md
        self.pkgname = pkgname

    def run(self):
        """ Generate Crop2ML specification of a simple strategy. """
        md = self.md

        # ModelUnit name id version timestep
        xml = ns.ModelUnit(modelid=self.pkgname + "." + md.name, name=md.name, timestep="1", version="001")
        doc = md.description
        desc = ns.Description(
            ns.Title(doc.Title),
            ns.Authors(doc.Authors),
            ns.Institution(doc.Institution),
            ns.Reference(doc.Reference),
            ns.Abstract(doc.Abstract)
            )
        inputs = ns.Inputs()
        outputs = ns.Outputs()
        for inp in md.inputs:
            if "variablecategory" in dir(inp):
                inputs.append(ns.Input(name=inp.name, description=inp.description, variablecategory=inp.variablecategory,  datatype=inp.datatype, max=inp.max, min = inp.min, default=inp.default, units=inp.units))
            else: inputs.append(ns.Input(name=inp.name, description=inp.description, parametercategory=inp.parametercategory, datatype=inp.datatype, max=inp.max, min = inp.min, default=inp.default, units=inp.units))
        for inp in md.outputs:
            outputs.append(ns.Output(name=inp.name, description=inp.description, datatype=inp.datatype, variablecategory=inp.variablecategory, max=inp.max, min = inp.min, units=inp.units))
        algo =ns.Algorithm(language = "cyml", platform ="", filename="algo/pyx/%s.pyx"%md.name)
        xml.append(desc)
        xml.append(inputs)
        xml.append(outputs)
        xml.append(algo)
        if md.function:
            for f in md.function:
                print(f)
                func = ns.Function(name = f, description="", filename="algo/pyx/%s.pyx"%f)
                xml.append(func)
        parametersets=ns.Parametersets()
        parametersets.append(ns.Parameterset(name="", description=""))
        testsets=ns.Testsets()
        testsets.append(ns.Testset(name="", parameterset="",description=""))
        xml.append(parametersets)
        xml.append(testsets)

        return xml