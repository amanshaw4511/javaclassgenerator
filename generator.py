# version 1.2

# whats new ??
# created command line argment
# now you can customize the varibale u want to create constructor , getter or setter ( just like eclipse )

import sys

def createConstructor(clss, cvars):
    print("\n\t//constructor")
    print(f"\tpublic {clss}(", end="")
    param = ""
    for var in cvars:
        param += var + ", "
    print(param[:-2],"){")

    # constructor vars
    for var in cvars:
        _,name = var.split()
        print(f"\t\tthis.{name} = {name};")
    print("\t}")

def createGetters(gvars):
    # getters
    print("\n\t//getters")
    for var in gvars:
        tpe,name = var.split()
        print(f"\tpublic {tpe} get{name.title()}(){{\n\t\t return this.{name};\n\t}}")

def createSetters(svars):
    # setters
    print("\n\t//setters")
    for var in svars:
        _,name = var.split()
        print(f"\tpublic void set{name.title()}({var}){{\n\t\t this.{name} = {name};\n\t}}")



def createClass(clss, varss, cvars, gvars, svars):
    # begin class 
    print(f"class {clss}{{")
    
    #print vars
    for var in varss:
        print("\tprivate "+var,end=';\n')

    createConstructor(clss, cvars)
    createGetters(gvars)
    createSetters(cvars)

    # end class
    print("}")


def createSolution(clss,varss,cvars,gvars,svars) :
    createClass(clss,varss,cvars,gvars,svars)
    print("\npublic class Solution{")
    print("\tpublic static void main(String[] argv){\n\t\t\n\t}\n}")


def go():
    argv = sys.argv[1:]
    usage = '.....error.....'
    clss = ''
    varss = []
    gvars = []
    svars = []
    cvars = []
    i = 0
    while i < len(argv) :
        if argv[i] == '-c' :
            clss = argv[i+1]
#            print(i,'cls')
            i = i + 2

        elif argv[i].startswith('-v'):
            varss.append(argv[i+1])
#            print(i,argv[i])
            if 'g' in argv[i] : 
                gvars.append(argv[i+1])
            if 's' in argv[i] : 
                svars.append(argv[i+1])
            if 'c' in argv[i]:
                cvars.append(argv[i+1])
            i = i + 2

        else :
            print(usage)
            break
#    print(argv, clss, varss, cvars, gvars, svars, sep='\n')
    createClass(clss,varss,cvars,gvars,svars)


if __name__ == "__main__":
    go()

