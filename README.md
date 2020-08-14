# javaclassgenerator
this python script is used to create java class with constructor, getters and setters

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
        }

        //getters
        public int getId(){
                 return this.id;
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
