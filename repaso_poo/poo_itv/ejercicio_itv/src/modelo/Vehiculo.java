package modelo;

import excepciones.DniException;

public class Vehiculo {

    private String nombre;
    private String apellidos;
    private String dni;
    private String matricula;
    private String identificador;

    public Vehiculo() {

    }

    public Vehiculo(String nombre, String apellidos, String dni, String matricula)
            throws DniException {
        this.setNombre(nombre);
        this.setApellidos(apellidos);
        this.setDni(dni);
        this.setMatricula(matricula);
        this.setIdentificador(identificador);
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public void setDni(String dni) throws DniException {
        comprobarDni(dni);
        this.dni = dni;
        
    }

    // ! ======================= METODO PARA COMPROBAR DNI =======================
    private void comprobarDni(String dni) throws DniException {

        String checks="TRWAGMYFPDXBNJZSQVHLCKE";

        if (dni.length() != 9) {
            throw new DniException();
        }

        int numDniSinLetra = Integer.parseInt(dni.substring(0, 8));
        char letraDni =  dni.charAt(8);
        
        char supuestaLetra = checks.charAt(numDniSinLetra%23);

        if (supuestaLetra != letraDni) {
            throw new DniException();
        }


    }

    // ! ================= FIN DE METODO PARA COMPROBAR DNI =================

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public void setIdentificador(String identificador) {
        this.identificador = identificador;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public String getDni() {
        return dni;
    }

    public String getMatricula() {
        return matricula;
    }

    public String getIdentificador() {
        return identificador;
    }

    @Override
    public String toString() {
        return "Vehiculo [nombre=" + nombre + ", apellidos=" + apellidos + ", dni=" + dni + ", matricula=" + matricula
                + ", identificador=]";
    }

}
