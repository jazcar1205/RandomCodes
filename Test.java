class Main {
  //Instance variables
  private String msg;
  private String secret = new String("secret");
  private int msgCount = 1; 
  
  //Constructer
  public Main(String msg){
    this.msg = msg;
  }
  
  //Setters and Getters
  public int getMsgCount(){
    return msgCount; 
  }
  
  public String getSecret(){
    return secret; 
  }

  public void setMsg(String msg){
    this.msg = new String(msg+" Bro!");
    addMsg();
  }
  
  //Brain Methods
  public void addMsg(){
    msgCount++;
  }
  
  public String toString(){
    return msg;
  }
  
  public static void main(String[] args) {
    Main hW =  new Main("Hey Human");
    System.out.println(hW);
    System.out.println(hW.getMsgCount());
    hW.setMsg("Hello");
    System.out.println(hW);
    System.out.println(hW.getMsgCount());
  }
}
