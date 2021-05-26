package sample;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.FlowPane;
import javafx.scene.control.TableView;
import javafx.scene.control.TableColumn;
import javafx.collections.ObservableList;
import javafx.collections.FXCollections;
import javafx.scene.control.cell.PropertyValueFactory;


public class Main extends Application{

    public static void main(String[] args) {

        Application.launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {

        int id1 = SQL.ID();

        ObservableList<Person> people = FXCollections.observableArrayList(

        );
        for(int i=1;i<=id1;i++){
            people.add(new Person(i,SQL.last(i),SQL.first(i)));
            System.out.println(i);
        }
        TableView<Person> table = new TableView<Person>(people);
        table.setPrefWidth(600);
        table.setPrefHeight(600);

        TableColumn<Person, Integer> IDColumn = new TableColumn<Person, Integer>("ID");
        IDColumn.setCellValueFactory(new PropertyValueFactory<Person, Integer>("id"));
        table.getColumns().add(IDColumn);

        TableColumn<Person, String> last_nameColumn = new TableColumn<Person, String>("Фамилия");
        last_nameColumn.setCellValueFactory(new PropertyValueFactory<Person, String>("last_name"));
        table.getColumns().add(last_nameColumn);

        TableColumn<Person, String> first_nameColumn = new TableColumn<Person, String>("Имя");
        first_nameColumn.setCellValueFactory(new PropertyValueFactory<Person, String>("first_name"));
        table.getColumns().add(first_nameColumn);
        
        FlowPane root = new FlowPane(10, 10, table);

        Scene scene = new Scene(root, 600, 400);

        stage.setScene(scene);
        stage.setTitle("TableView in JavaFX");
        stage.show();

    }
}