package vista;

import model.Curso;
import model.Estudiante;
import model.Persona;
import model.Profesor;

public class Main {

    public static void main(String[] args) {
        // Crear profesores
        Profesor profesor1 = new Profesor("Dr. García", 45, "Matemáticas");
        Profesor profesor2 = new Profesor("Dra. López", 50, "Física");
        // Crear estudiantes
        Estudiante estudiante1 = new Estudiante("Juan", 20, "Ingeniería");
        Estudiante estudiante2 = new Estudiante("Ana", 22, "Medicina");
        Estudiante estudiante3 = new Estudiante("Carlos", 21, "Derecho");

        // Crear cursos
        Curso curso1 = new Curso("Álgebra Lineal", profesor1);
        Curso curso2 = new Curso("Mecánica Clásica", profesor2);

        // Matricular estudiantes en los cursos
        curso1.matricularEstudiante(estudiante1);
        curso1.matricularEstudiante(estudiante2);
        curso2.matricularEstudiante(estudiante3);
        // Mostrar información de los cursos
        curso1.mostrarProfesor();
        curso1.mostrarEstudiantes();
        curso2.mostrarProfesor();
        curso2.mostrarEstudiantes();
        // Hacer trabajar a los profesores
        profesor1.trabajar();
        profesor2.trabajar();

    }

}
