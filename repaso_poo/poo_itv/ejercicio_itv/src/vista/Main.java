package vista;

import excepciones.DniException;
import modelo.Vehiculo;

public class Main {
    public static void main(String[] args) {

        try {
        
            Vehiculo vehiculo1 = new Vehiculo("Cristian", "Lopez", "49852630S", "1234ABC");

        } catch (DniException e) {
            e.printStackTrace();
        }
    }

}
