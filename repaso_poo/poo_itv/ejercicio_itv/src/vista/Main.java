package vista;

import java.util.Scanner;

import excepciones.DniException;
import excepciones.MatriculaException;
import modelo.DatosVehiculo;
import modelo.Vehiculo;

public class Main {
    public static void main(String[] args) {
        Scanner sc1 = new Scanner(System.in);
        String nombre = "Luis";
        String apellidos = "Garcia Perez";
        String dni = "31452329J";
        String matricula = "1224ABC";
        String identificador = "";
        Vehiculo vehiculo = null;
        try {
        vehiculo = new Vehiculo(nombre, apellidos, dni, matricula);
        System.out.println(vehiculo);

        DatosVehiculo datoVehivulo1 = new DatosVehiculo(vehiculo);
        sc1.nextLine();
            
        datoVehivulo1.atiende();
        System.out.println(datoVehivulo1.getTiempoEspera());
        

        } catch (DniException | MatriculaException e) {
        System.out.println(e.getMessage());
        }
    }

}
