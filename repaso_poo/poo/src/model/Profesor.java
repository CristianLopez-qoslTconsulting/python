package model;

import interfaz.Trebajador;

public class Profesor extends  Persona implements Trebajador {
    private String especialidad;

    @Override
    public void trabajar() {
        System.out.println(this.getNombre() + " esta enseñando "+ especialidad );
    }

    public Profesor(String nombre, int edad, String especialidad) {
        super(nombre, edad);
        this.setEspecialidad(especialidad);
    }

    public void mostrarInformacion(){
        System.out.println("Nombre: " + this.getNombre() + " | Especialidad: " + getEspecialidad());
    }

    public String getEspecialidad() {
        return especialidad;
    }

    public void setEspecialidad(String especialidad) {
        this.especialidad = especialidad;
    }

    

    

}
