## Genetic Programming

GP is a new method to generate computer programs. It was derived from the model of biological evolution. Programs are "bred" through continuous improvement of an initially random population of programs. 

Improvements are made possible by stochastic variation of programs and selection according to prespecified criteria for judging the quality of a solution.

### Methods:

**Loosely Typed GP:** 
It does not enforce a specific type between the nodes. More specifically, primitives arguments can be any primitives or terminals present in the primitive set. 

**Strongly Typed GP:**
In strongly typed GP, every primitive and terminal is assigned a specific type. The output type of a primitive must match the input type of another one for them to be connected.

**Ephemeral Constants:**
An ephemeral constant is a terminal encapsulating a value that is generated from a given function at run time. It is determined when it is inserted in the tree and never changes unless it is replaced by another constant.

## Implementation:

I will be using DEAP (Distributed Evolutionary Algorithms in Python) to implement GP. DEAP is a novel evolutionary computation framework for rapid prototyping and testing of ideas. It seeks to make algorithms explicit and data structures transparent. It works in perfect harmony with parallelisation mechanism such as multiprocessing and SCOOP.

Random numerical constants (RNCs) can easily be implemented in GEP. For that an additional domain DC is introduced in GEP genes. 

Problems that will be covered:
* Symbolic regression 
* Even-parity problem
* Artificial Ant
* Spambase problem
* TSP problem

> The most significant difference between GEP (Gene expression programming) and GP is that GEP adopts a linear fixed-length representation of computer programs, which can later be translated into an expression tree. By contrast, GP typically uses a variable-size syntax tree representation directly.
