package vista;

import interfaz.Trebajador;
import model.Direccion;
import model.Estudiante;
import model.Persona;
import model.Profesor;

public class Main {
    public static void main(String[] args) {

        Profesor profesor1 = new Profesor("Diego", 25, "Informatica");

        profesor1.trabajar();
    

        
        Estudiante estudiante1 = new Estudiante("Cristian", 21, "Informatica");
        System.out.println(estudiante1);

        estudiante1.estudiar();
        

   
        Persona persona1 = new Persona("Cristian", 2);
        Persona persona2 = new Persona("Cristian", 21);

        System.out.println(persona1.equals(persona2));

        Persona [] listaPersonas = new Persona[3];

        listaPersonas[0] = profesor1;
        listaPersonas[1] = persona2;
        listaPersonas[2] = estudiante1;

        for (Persona persona : listaPersonas) {
            if (persona instanceof Trebajador ) {
                ((Trebajador)persona).trabajar();
                System.out.println(persona);
                
            }else{
                System.out.println(persona);
            }
        }

        Direccion direccion1 = new Direccion("calle villa playa", "trebujena", "11540");
        persona1.setDireccion(direccion1);
        persona1.mostrarDireccion();

        /*  0 si son iguales.
            1 si el objeto actual es mayor.
            -1 si el objeto actual es menor. 
            */
       int resultado1 = persona1.compareTo(persona2);
       System.out.println(resultado1);
    }

    
        
        

    

}
