import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.*;

public class day1 {
    public static void main(String[] args) throws Exception {
        File file = new File("day1.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String st;
        HashMap<Character, Integer> x;
        ArrayList<Integer> vals = new ArrayList<>();
        while ((st = br.readLine()) != null) {
            vals.add(Integer.parseInt(st));
        }
        int count = 0;
        for(int i: vals) {
            int temp = i;
            while(temp > 0) {
                temp = (temp/3) - 2;
                if (temp > 0)
                    count += temp;
            }
        }
        System.out.println(count);
    }
}