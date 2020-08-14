
import sys

def getClass(cls,varss):
    # create class 
    print(f"class {cls}{{")
    
    #print vars
    for var in varss:
        print("\tprivate "+var,end=';\n')

    #creat constructors
    print("\n\t//constructor")
    print(f"\tpublic {cls}(", end="")
    param = ""
    for var in varss:
        param += var + ", "
    print(param[:-2],"){")

    # constructor vars
    for var in varss:
        tpe,name = var.split()
        print(f"\t\tthis.{name} = {name};")
    print("\t}")

    # getters
    print("\n\t//getters")
    for var in varss:
        tpe,name = var.split()
        print(f"\tpublic {tpe} get{name.title()}(){{\n\t\t return this.{name};\n\t}}")

    # setters
    print("\n\t//setters")
    for var in varss:
        tpe,name = var.split()
        print(f"\tpublic void set{name.title()}({var}){{\n\t\t this.{name} = {name};\n\t}}")

    print("}")


def createSolution(cls,varss):
    getClass(cls,varss)
    print("\npublic class Solution{")
    print("\tpublic static void main(String[] argv){\n\t\t\n\t}\n}")


if __name__ == "__main__":
    cls = sys.argv[1]
    n = len(sys.argv)
    varss = []
    for i in range(2,n):
        varss.append(sys.argv[i])

#    print(cls,varss)
    getClass(cls,varss)
        


