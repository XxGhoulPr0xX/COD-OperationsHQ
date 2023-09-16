public class P17 extends Thread
{
    int impar=0;
    int par=0;
    public void run(){
        ParImpar();
    }
    public void ParImpar()
    {
        long time;
        int min=1;
        int max=10;
        double randomNum=Math.random()*(max-min);
        int value=(int)randomNum;
        switch(value)
        {
            case 10:
                setPriority(Thread.MAX_PRIORITY);
            break;
            case 5:
                setPriority(Thread.NORM_PRIORITY);
            break;
            case 1:
                setPriority(Thread.MIN_PRIORITY);
            break;
        }
        for(int i=1;i<=20;i++){
            time=(long)(Math.random() * 1000);
            if(i%2==0){
                par=i+par;
                System.out.println(i+" Par y con proridad "+getPriority());
            }
            else{
            impar=i+impar;
            System.out.println(i+" Impar y con proridad "+getPriority());
            }
            try {
                sleep(time);
            } 
            catch (InterruptedException e){
                
            } 
        }
        System.out.println("Suma total: "+par+" Suma total: "+impar+","+value+","+randomNum);
    }
    public static void main (String[] args){
        P17 t1=new P17();
        t1.start();
    }
}
