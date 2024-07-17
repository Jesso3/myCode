package Graphics;

public class Person {
    private String name;
    private int age;
    private double height;

    public Person(){
        name = "Unknown";
        age = 0;
        height = 0.0;
    }

    public Person(String n){
        age = 0;
        height = 0.0;
    }

    public Person(String n, int a, double h){
        name = n;
        age = a;
        height = h;
    }



    public static void main(String[] args){
        Person person1 = new Person();
        Person person2 = new Person("hi");
        Person person3 = new Person("bye",25,8.5);

        

        

    }
}
