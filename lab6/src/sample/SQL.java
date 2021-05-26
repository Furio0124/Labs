package sample;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class SQL {

    public static String last(int id) {
        try {
            String url = "jdbc:mysql://localhost/selfs";
            String username = "root";
            String password = "Danik0124";

            Class.forName("com.mysql.cj.jdbc.Driver").getDeclaredConstructor().newInstance();
            try (Connection conn = DriverManager.getConnection(url, username, password)) {
                Statement statement = conn.createStatement();
                ResultSet resultSet1 = statement.executeQuery("select last_name from users where ID="+id);
                while (resultSet1.next()) {
                    String last = resultSet1.getString(1);
                    return last;
                }
                System.out.println("Connection to Store DB succesfull!");
            }
        } catch (Exception ex) {
            System.out.println("Connection failed...");

            System.out.println(ex);
        } return "Не получилось вернуть last";
    }

    public static int ID() {
        try {
            String url = "jdbc:mysql://localhost/selfs";
            String username = "root";
            String password = "Danik0124";

            Class.forName("com.mysql.cj.jdbc.Driver").getDeclaredConstructor().newInstance();
            try (Connection conn = DriverManager.getConnection(url, username, password)) {
                Statement statement = conn.createStatement();
                ResultSet resultSet = statement.executeQuery("select count(*)\n" +
                        "from users");
                while (resultSet.next()) {
                    int ID = resultSet.getInt(1);
                    return ID;
                }
                System.out.println("Connection to Store DB succesfull!");
            }

        } catch (Exception ex) {
            System.out.println("Connection failed...");

            System.out.println(ex);
        }
        return 0;
    }

    public static String first(int id) {
        try {
            String url = "jdbc:mysql://localhost/selfs";
            String username = "root";
            String password = "Danik0124";

            Class.forName("com.mysql.cj.jdbc.Driver").getDeclaredConstructor().newInstance();
            try (Connection conn = DriverManager.getConnection(url, username, password)) {
                Statement statement = conn.createStatement();
                ResultSet resultSet1 = statement.executeQuery("select first_name from users where ID="+id);
                while (resultSet1.next()) {
                    String first = resultSet1.getString(1);
                    return first;
                }
                System.out.println("Connection to Store DB succesfull!");
            }
        } catch (Exception ex) {
            System.out.println("Connection failed...");

            System.out.println(ex);
        } return "Не получилось вернуть first";
    }
}



