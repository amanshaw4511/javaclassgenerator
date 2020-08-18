# javaclassgenerator

this python script is used to create java class with constructor, getters and setters

## usage

```sh
$ python generator.py -c 'className' -v[cgs] 'type1 var1' -v[cgs] 'type2 var2'
```

  - -c      : class 
  - -v      : variable
  - -c      : constructor (optional)
  - -g      : getter (optional)
  - -s      : setter (optional)

## example       

```sh
$ python generator.py -c Employee -vg 'int id' -vcgs 'String name' -vcgs 'double salary'
```


```java
class Employee{
        private int id;
        private String name;
        private double salary;

        //constructor
        public Employee(String name, double salary ){
                this.name = name;
                this.salary = salary;
        
        }

        //getters
        public int getId(){
                 return this.id;
        
        }
        public String getName(){
                 return this.name;
        
        }
        public double getSalary(){
                 return this.salary;
        
        }

        //setters
        public void setName(String name){
                 this.name = name;
        
        }
        public void setSalary(double salary){
                 this.salary = salary;
        
        }

}
```
