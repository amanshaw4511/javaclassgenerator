# javaclassgenerator
this python script is used to create java class with constructor, getters and setters

<<<<<<< HEAD

# usage

$ python generator.py -c 'className' -v[cgs] 'type1 var1' -v[cgs] 'type2 var2'

-c      : class 
-v      : variable
-c      : constructor (optional)
-g      : getter (optional)
-s      : setter (optional)

## example

$ python generator.py -c Employee -vg 'int id' -vcgs 'String name' -vcgs 'double salary'

class Employee{
        private int id;
        private String name;
        private double salary;

        //constructor
        public Employee(String name, double salary ){
                this.name = name;
                this.salary = salary;
        
=======
## usage
$ python generator.py className 'type1 var1' 'type2 var2' 'type3 var3' 

Example :

$ python generator.py Book 'int id' 'String name' 'float price'


class Book{

        private int id;
        private String name;
        private float price;

        //constructor
        public Book(int id, String name, float price ){
                this.id = id;
                this.name = name;
                this.price = price;
>>>>>>> af875bc914430a2925d81bc3f53b4c423425ad48
        }

        //getters
        public int getId(){
                 return this.id;
<<<<<<< HEAD
        
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

=======
        }
        public String getName(){
                 return this.name;
        }
        public float getPrice(){
                 return this.price;
        }

        //setters
        public void setId(int id){
                 this.id = id;
        }
        public void setName(String name){
                 this.name = name;
        }
        public void setPrice(float price){
                 this.price = price;
        }
}
>>>>>>> af875bc914430a2925d81bc3f53b4c423425ad48