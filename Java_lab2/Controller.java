package sample;

import java.awt.event.MouseEvent;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Button;
import javafx.scene.paint.Color;

import static java.lang.Math.random;

public class Controller {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Button circle;

    @FXML
    private Button rhombus;

    @FXML
    private Button rect;

    @FXML
    private Canvas canv;

    @FXML
    int RandomNum(){
        int RandomNumbers = (int)(random()*250+5);
        return (RandomNumbers);
    }

    @FXML
    void draged(MouseEvent event){

    }

    @FXML
    void paintCircle(ActionEvent event) {
        GraphicsContext gc = canv.getGraphicsContext2D();
        int x =RandomNum();
        int y =RandomNum();
        int w= RandomNum();
        int h=w;
        gc.setFill(Color.rgb(x,y,w,1));
        gc.fillOval(x,y, w,h);
        gc.strokeOval(x+1,y+1,w+1,h+1);

    }

    @FXML
    void paintRect(ActionEvent event) {
        GraphicsContext gc = canv.getGraphicsContext2D();
        int x =RandomNum();
        int y =RandomNum();
        int w=RandomNum();
        int h=w;
        gc.setFill(Color.rgb(x,y,w,1));
        gc.fillRect(x,y, w,h);
        gc.strokeRect(x+1,y+1,w+1,h+1);;
    }

    @FXML
    void paintRhombus(ActionEvent event) {
        GraphicsContext gc = canv.getGraphicsContext2D();
        gc.beginPath();
        int x =RandomNum();
        int y =RandomNum();
        int w= RandomNum();
        gc.moveTo(x+100,y+50);
        gc.lineTo(x+100,y+50);
        gc.lineTo(x+50,y+100);
        gc.lineTo(x+0,y+50);
        gc.lineTo(x+50,y+0);
        gc.setFill(Color.rgb(x,y,w,1));
        gc.fill();
    }

    @FXML
    void initialize() {
        assert circle != null : "fx:id=\"circle\" was not injected: check your FXML file 'Untitled'.";
        assert rect != null : "fx:id=\"rect\" was not injected: check your FXML file 'Untitled'.";
        assert rhombus != null:"fx:id=\"rhombus\" was not injected: check your FXML file 'Untitled'.";
        assert canv != null : "fx:id=\"canv\" was not injected: check your FXML file 'Untitled'.";
    }

}
