package model;

public class Estudiante extends Persona {

    private String carrera;

    public Estudiante() {

    }

    public Estudiante(String nombre, int edad, String carrera) {
        super(nombre, edad);
        this.setCarrera(carrera);
    }

    public Estudiante(String carrera) {
        this.carrera = carrera;
    }
    public void mostrarInformacion(){
        System.out.println("Nombre: " + this.getNombre() + " | Carrera: " + this.getCarrera());
    }

    public void estudiar() {
        System.out.println(this.getNombre() + " esta estudiando " + getCarrera());
    }

    public String getCarrera() {
        return carrera;
    }

    public void setCarrera(String carrera) {
        this.carrera = carrera;
    }

    @Override
    public String toString() {
        return "Nombre: " + getNombre() + " | " + "Edad: " + getEdad() + " | " + "Carrera: " + carrera;
    }

}
