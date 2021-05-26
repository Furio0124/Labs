package sample;

import javafx.beans.property.*;

public class Person{

    private SimpleIntegerProperty id;
    private SimpleStringProperty last_name;
    private SimpleStringProperty first_name;

    Person( int id,String name, String first_name){
        this.id = new SimpleIntegerProperty(id);
        this.last_name = new SimpleStringProperty(name);
        this.first_name = new SimpleStringProperty(first_name);

    }

    public int getId(){ return id.get();}
    public void setId(int value){ id.set(value);}

    public String getLast_name(){ return last_name.get();}
    public void setLast_name(String value){ last_name.set(value);}

    public String getFirst_name(){ return first_name.get();}
    public void setFirst_name(String value){ first_name.set(value);}

}