package modelo;

public class DatosVehiculo {
    private Vehiculo vehiculo;
    private long entrada;
    private long salida;
    private long tiempoEspera;

    public DatosVehiculo(Vehiculo vehiculo) {
        this.setEntrada(entrada);
    }

    public void atiende() {
        this.salida = Reloj.ahora();
        this.tiempoEspera = this.salida - this.entrada;
    }

    public long getTiempoEspera() {
        this.tiempoEspera = this.tiempoEspera / 1000;

        return this.tiempoEspera;
    }

    public void setVehiculo(Vehiculo vehiculo) {
        this.vehiculo = vehiculo;
    }

    public void setEntrada(long entrada) {
        this.entrada = Reloj.ahora();
    }

    public void setSalida(long salida) {
        this.salida = salida;
    }

    public void setTiempoEspera(long tiempoEspera) {

        this.tiempoEspera = tiempoEspera;
    }

    public Vehiculo getVehiculo() {
        return vehiculo;
    }

    public long getEntrada() {
        return entrada;
    }

    public long getSalida() {
        return salida;
    }

}
