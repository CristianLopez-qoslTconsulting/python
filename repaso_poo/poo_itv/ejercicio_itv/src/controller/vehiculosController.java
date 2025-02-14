package controller;

import java.util.LinkedList;
import java.util.Queue;
import modelo.DatosVehiculo;

public class vehiculosController {
    private Queue<DatosVehiculo> colaEspera;
    private Queue<DatosVehiculo> colaAtendidos;

   public vehiculosController() {
        colaEspera = new LinkedList<>();
        colaAtendidos = new LinkedList<>();
    }

    

    

}
