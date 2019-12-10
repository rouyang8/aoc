import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashSet;
import java.util.*;

public class day4 {
    public static void main(String[] args) throws Exception {
        day4.run("day4test.txt");
        day4.run("day4.txt");
    }
    public static void run(String f) throws Exception{
        File file = new File(f);
        BufferedReader br = new BufferedReader(new FileReader(file));
        String st;
        HashMap<Point,Point> vals = new HashMap<Point, Point>();
        ArrayList<Integer> inter = new ArrayList<Integer>();
        int count = 0;
        while ((st = br.readLine()) != null) {
            String[] ss = st.split("-");
            int min = Integer.parseInt(ss[0]);
            int max = Integer.parseInt(ss[1]);
            for(int i = min; i <= max; i++) {
                String s = Integer.toString(i);
                boolean ff = false;
                boolean d = true;
                boolean dead = false;
                boolean skip = false;
                for(int j = 0; j < s.length(); j++) {
                    if(j < (s.length()-1) && s.charAt(j) > s.charAt(j+1)) {
                        d = false;
                    }
                    if(j < (s.length()-1) && s.charAt(j) == s.charAt(j+1)) {
                        ff = true;
                        j+=1;
                        if(j < (s.length()-1) && s.charAt(j) > s.charAt(j+1)) {
                            d = false;
                        }
                        if(!(j < s.length()-1 && s.charAt(j) == s.charAt(j+1)))
                            skip = true;
                        while(j < s.length()-1 && s.charAt(j) == s.charAt(j+1)) {
                            j += 1;
                            if(j < (s.length()-1) && s.charAt(j) > s.charAt(j+1)) {
                                d = false;
                            }
                            ff = false;
                        }
                    }
                }
                if((skip == true || ff == true) && d == true) {
                    System.out.println(i);
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}