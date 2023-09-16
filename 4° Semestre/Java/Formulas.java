package Formulas;

public class Formulas {

    private double l=0;private double b=0;private double h=0;private double r=0;private double d=0;private double a=0;
    public Formulas(double a, double b, double h, double r, double d, double l){
        this.l=l; this.b=b; this.r=r; this.h=h; this.d=d; this.a=a;
    }
    public Formulas(){
        this.l=1; this.b=2; this.r=3; this.h=4; this.d=5; this.a=6;
    }
   public double hipotenusa(){
       double areaH=(Math.pow(a,2))+(Math.pow(b, 2));
       return areaH;
   }
   public double CuadradoArea(){
       double areaC=(l*l);
        return areaC;
   } 
    public double CuadradoPerimetro(){
       double perimetroC=l+l+l+l;
       return perimetroC;
   }
    public double RectanguloArea(){
       double areaR=(b*h);
       return areaR;
   }
    public double RectanguloPerimetro(){
       double perimetroR=(b+h)*2;
       return perimetroR;
   }
    public double TrainguloArea(){
       double areaT=(h*b)/2;
       return areaT;
   }
    public double TraginuloPerimetro(){
       double perimetroT=(b+h);
        return perimetroT;
   }
    public double CirculoArea(){
       double areaCir=(r*r)*Math.PI;
       return areaCir;
   }
    public double CirculoPerimetro(){
       double perimetroCir=(d*d)*Math.PI;
        return perimetroCir;

   }
}