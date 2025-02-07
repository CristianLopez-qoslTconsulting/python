package model;



public class Persona implements Comparable {
    private String nombre;
    private int edad;
    private Direccion direccion;

    public Persona() {

    }

    public Persona(String nombre, int edad) {
        this.setNombre(nombre);
        this.setEdad(edad);

    }

    public void mostrarDireccion() {
        System.out.println("Nombre: " + getNombre() + "| Direccion: " + direccion);
    }

    public void mostrarInformacion() {
        System.out.println("Nombre: " + getNombre() + " | Edad: " + getEdad());
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((nombre == null) ? 0 : nombre.hashCode());
        result = prime * result + edad;
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Persona other = (Persona) obj;
        if (nombre == null) {
            if (other.nombre != null)
                return false;
        } else if (!nombre.equals(other.nombre))
            return false;
        if (edad != other.edad)
            return false;
        return true;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    @Override
    public String toString() {
        return "Persona [nombre=" + nombre + ", edad=" + edad + "]";
    }

    public Direccion getDireccion() {
        return direccion;
    }

    public void setDireccion(Direccion direccion) {
        this.direccion = direccion;
    }

    @Override
    public int compareTo(Object otro) {

        if (otro instanceof Persona) {
            Persona otraPersona = (Persona) otro;

            if (this.edad == otraPersona.getEdad()) {
                return 0;
            } else if (this.edad > otraPersona.getEdad()) {
                return 1; 
            } else {
                return -1; 
            }
        }
        
        return edad; 
    
    }

}
