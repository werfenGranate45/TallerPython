public class Cafe{
    private String estilo;
    private String ingrediente;
    private String tamaño;
    private double capacidad;
    private boolean temperatura;

    

    //Codificar los setters y los getters correspondiente de cada atributo
    public boolean setEstilo(String est){
        if(est.length() > 0){
            this.estilo = est;
            return true;
        }else return false;
    }

   public String getEstilo(){return this.estilo; }

   public void Quemar(){
    System.out.println("Te queme a jaja xd");
   }

   public void Despertar(){
    System.out.println("When como cuando te despiertan");
   }

   public String toString(){
    String toStr = "Estilo: "+this.estilo;
    toStr += "Ingrediente: "+this.ingrediente;
    toStr += "Tamaño: "+this.tamaño;
    toStr += "Capacidad "+this.capacidad;
    toStr += "Temperatura: "+this.temperatura;
    return toStr;
   }  
}