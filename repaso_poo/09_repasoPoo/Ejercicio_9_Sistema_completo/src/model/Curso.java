package model;

import java.util.ArrayList;
import java.util.List;

public class Curso {
    private String nombreCurso;
    private Profesor profesor;
    private List<Estudiante> estudiantes;

    public String getNombreCurso() {
        return nombreCurso;
    }

    public void setNombreCurso(String nombreCurso) {
        this.nombreCurso = nombreCurso;
    }

    public Profesor getProfesor() {
        return profesor;
    }

    public void setProfesor(Profesor profesor) {
        this.profesor = profesor;
    }

    public Curso(String nombreCurso, Profesor profesor) {
        this.setNombreCurso(nombreCurso);
        this.setProfesor(profesor);
        this.estudiantes = new ArrayList<>();
    }

    public void matricularEstudiante(Estudiante estudiante) {
        estudiantes.add(estudiante);
    }

    // Método para mostrar la lista de estudiantes
    public void mostrarEstudiantes() {
        System.out.println("Estudiantes matriculados en " + nombreCurso + ":");
        for (Estudiante estudiante : estudiantes) {
            System.out.println(estudiante);
        }
    }

    // Método para mostrar la información del profesor
    public void mostrarProfesor() {
        System.out.println("Profesor de " + nombreCurso + ": " + profesor);
    }

    public String toString() {
        return nombreCurso + " - Profesor: " + profesor.getNombre();
    }

}
