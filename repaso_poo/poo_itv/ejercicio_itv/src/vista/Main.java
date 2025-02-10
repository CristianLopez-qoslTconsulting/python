package vista;

import excepciones.DniException;
import excepciones.MatriculaException;
import modelo.Vehiculo;

public class Main {
    public static void main(String[] args) {
        String nombre = "Luis";
        String apellidos = "Garcia Perez";
        String dni = "31452329J";
        String matricula = "1224ABC";
        String identificador = "";
        Vehiculo vehiculo = null;
        try {
        vehiculo = new Vehiculo(nombre, apellidos, dni, matricula);
        System.out.println(vehiculo);
        } catch (DniException | MatriculaException e) {
        System.out.println(e.getMessage());
        }
    }

}
