import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.*;

public class day2 {
    public static void main(String[] args) throws Exception {
        File file = new File("day2.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String st;
        HashMap<Character, Integer> x;
        int[] arr = new int[0];
        ArrayList<Integer> vals = new ArrayList<>();
        while ((st = br.readLine()) != null) {
            String[] s = st.split(",");
            arr = new int[s.length];
            for(int i = 0; i < s.length; i++) {
                arr[i] = Integer.parseInt(s[i]);
            }
        }
        int[] master = arr.clone();
        for(int i = 0; i <= 99; i++) {
            for (int j = 0; j <= 99; j++) {
                arr = master.clone();
                arr[1] = i;
                arr[2] = j;
                int ind = 0;
                while (arr[ind] != 99) {
                    if (arr[ind] == 1) {
                        arr[arr[ind + 3]] = arr[arr[ind + 1]] + arr[arr[ind + 2]];
                    } else if (arr[ind] == 2) {
                        arr[arr[ind + 3]] = arr[arr[ind + 1]] * arr[arr[ind + 2]];
                    } else {
                        System.out.println("something went wrong");
                    }
                    ind += 4;
                }
                if(arr[0] == 19690720) { //4484226, 19690720
                    System.out.println(100 * i + j);
                }
            }
        }
    }
}