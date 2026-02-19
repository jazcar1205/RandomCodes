class Main {
  public static void main(String[] args) {
    String result =""; 
    String str = "Bello Human";
    for(int i = str.length(); i>0; i--){
      result = result + str.substring(i-1,i);
    }
    System.out.println("Original Word is: "+str+"\nReversed Word is : "+ result);
  }
}