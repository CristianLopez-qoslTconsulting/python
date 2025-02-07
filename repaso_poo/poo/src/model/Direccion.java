package model;

public class Direccion {
    private String calle;
    private String ciudad;
    private String codigoPostal;

    public Direccion(){

    }

    public Direccion(String calle, String ciudad, String codigoPostal) {
        this.setCalle(calle);
        this.setCiudad(ciudad);
        this.setCodigoPostal(codigoPostal);
    }

    public String getCalle() {
        return calle;
    }
    public String getCiudad() {
        return ciudad;
    }
    public String getCodigoPostal() {
        return codigoPostal;
    }

    public void setCalle(String calle) {
        this.calle = calle;
    }

    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }

    public void setCodigoPostal(String codigoPostal) {
        this.codigoPostal = codigoPostal;
    }

    @Override
    public String toString() {
        return "Direccion [calle=" + calle + ", ciudad=" + ciudad + ", codigoPostal=" + codigoPostal + "]";
    }

    
    

    

}
