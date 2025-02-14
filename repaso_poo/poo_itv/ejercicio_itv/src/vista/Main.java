package vista;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

import excepciones.DniException;
import excepciones.MatriculaException;
import modelo.DatosVehiculo;
import modelo.Vehiculo;

public class Main {

    public static void main(String[] args) {

        try {
            File f;
            BufferedReader br;
            FileReader fr;
            f = new File("propietarios.txt");

            if (!f.exists()) {
                System.out.println("Creando fichero");
                f.createNewFile();
            }

            fr = new FileReader(f);
            br = new BufferedReader(fr);
            ArrayList<Vehiculo>guardarVehiculos = new ArrayList<Vehiculo>();
            String linea;
            while ((linea = br.readLine()) != null) {
                
                String[] guardarLinea = linea.split(",");

                guardarVehiculos.add(new Vehiculo(guardarLinea[0], guardarLinea[1], guardarLinea[2], guardarLinea[3]));

                
            }
            System.out.println(guardarVehiculos);

        } catch (IOException | MatriculaException | DniException e) {
            System.out.println(e.getMessage());
        }

    }

}
