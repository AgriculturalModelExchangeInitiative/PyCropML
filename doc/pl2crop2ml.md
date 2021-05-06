=================================================
From crop modeling platforms to Crop2ML framework
=================================================

Motivation
==========
Crop2ML framework provides a number of shared concepts that allows creating a crop model component regardless of crop modeling platforms specificities. Based on its transformation 
system, a Crop2ML model can be transformed to platform model components in taking into account the constraints of the target platforms. To manage the evolution of generated components and to make them available for other platforms, it is required to develop an inverse transformation system in order to achieve an interoperable system.
The goal of this part of the system is to reproduce automatically a Crop2ML model from a platform model component.

Approach
========
It consits of generating both the Crop2ML-based xml files of meta-information and the model algorithms and external functions in CyML from a component of BioMA (C#), APSIM (C#), Simplace (Java), DSSAT (F90), OpenAlea (Python), Record (C++), STICS (F90) or Sirius (C#) which use different programming languages.
Our approach is to analyze the source code of the component by converting it into a Common Abstract Semantic Graph (ASG), extracting the required information and translating them into Crop2ML/CyML.
Our work is based on platforms, that means that the strcuture of the component is well known. This makes easily the search of information. 

Transformation process
======================
The transformation process involves five steps:

1. Provide the [ANTLR grammar] (https://github.com/antlr/grammars-v4) of each programming language that our system supports. 
2. Generate the python files to parse the grammar by following [here](https://github.com/antlr/antlr4/blob/master/doc/python-target.md). 
3. Use `parsef` to parse the grammar based on the generated files and to get the Concrete Syntax Tree of the model component. 
4. Use `simplifyAntlrTree` on the output of the precedent tree to generate an abstract syntax tree (AST) based on [antlr-ast](https://github.com/datacamp/antlr-ast)
5. Use a `transformer` method implemented for each grammar to transform each kind of nodes of the precedent output. The output is an abstract semantic graph that still contains some nodes specific to the grammar. However some nodes providing from the common concepts of our supported languages are described by the same way. 
6. Use `MetaExtraction` methods to extract information from the ASG according to the specificities of platforms. Thus, for each platform, a specific class could inherit this class to achieve this extraction. The outputs will be a `ModelUnit`and `ModelComposite`objects, the part of code where model algorithm, and external functions are implemented. An example is `BiomaExtraction`class.
7. Use `run` method of `Pl2Crop2ml` class to transform `ModelUnit`and `ModelComposite` python objects into Crop2ML-based xml files.
8. Provide a `transform` method to transform algorithm and external function in a complete CASG by eliminating or transforming the rest of nodes specific to the platform. 
9. Use the common class `CymlGenerator` to convert them into CyML.




