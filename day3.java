import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashSet;
import java.util.*;

public class day3 {
    public static void main(String[] args) throws Exception {
        day3.run("day3test.txt");
        day3.run("day3.txt");
    }
    public static void run(String f) throws Exception{
        File file = new File(f);
        BufferedReader br = new BufferedReader(new FileReader(file));
        String st;
        HashMap<Point,Point> vals = new HashMap<Point, Point>();
        ArrayList<Integer> inter = new ArrayList<Integer>();
        int id = 0;
        while ((st = br.readLine()) != null) {
            String[] s = st.split(",");
            int x = 0;
            int y = 0;
            int steps = 0;
            id += 1;
            for(int i = 0; i < s.length; i++) {
                char b = s[i].charAt(0);
                if (b == 'R') {
                    int z = Integer.parseInt(s[i].substring(1));
                    for (int a = x + 1; a <= x + z; a++) {
                        //System.out.println("add " + a + " " + y);
                        steps++;
                        if(id > 1) {
                            if (vals.containsKey(new Point(a, y, steps))) {
                                inter.add(steps + vals.get(new Point(a,y,0)).steps);
                            }
                        }
                        if(id == 1)
                        vals.put(new Point(a, y, steps),new Point(a, y, steps));
                    }
                    x += z;
                } else if (b == 'L') {
                    int z = Integer.parseInt(s[i].substring(1));
                    for (int a = x-1; a >= x-z; a--) {
                        //System.out.println("add " + a + " " + y);
                        steps++;
                        if(id > 1) {
                            if (vals.containsKey(new Point(a, y, steps))) {
                                inter.add(steps + vals.get(new Point(a,y,0)).steps);
                            }
                        }
                        if(id == 1)
                        vals.put(new Point(a, y, steps),new Point(a, y, steps));
                    }
                    x -= z;
                } else if (b == 'D') {
                    int z = Integer.parseInt(s[i].substring(1));
                    for (int a = y - 1; a >= y - z; a--) {
                        //System.out.println("add " + x + " " + a);
                        steps++;
                        if(id > 1) {
                            if (vals.containsKey(new Point(x, a, steps))) {
                                inter.add(steps + vals.get(new Point(x,a,0)).steps);
                            }
                        }
                        if(id == 1)
                        vals.put(new Point(x, a, steps),new Point(x, a, steps));
                    }
                    y -= z;
                } else {
                    int z = Integer.parseInt(s[i].substring(1));
                    for (int a = y + 1; a <= y + z; a++) {
                        //System.out.println("add " + x + " " + a);
                        steps++;
                        if(id > 1) {
                            if (vals.containsKey(new Point(x, a, steps))) {
                                inter.add(steps + vals.get(new Point(x,a,0)).steps);
                            }
                        }
                        if(id == 1) {
                            vals.put(new Point(x, a, steps), new Point(x, a, steps));
                        }
                    }
                    y += z;
                }
            }
        }
        /*for(Integer i: inter) {
            //System.out.println(i);
        }*/
        System.out.println(Collections.min(inter));
    }
}
class Point {
    public int x;
    public int y;
    public String name;
    public int steps;
    public Point (int i, int j, int s){
        x = i;
        y = j;
        steps = s;
        name = x+" "+y;
    }
    @Override
    public boolean equals (Object p) {
        if(p instanceof Point) {
            Point ped = (Point) p;
            //System.out.println("comparing...");
            return (ped.x == x && ped.y == y);
        }
        return false;
    }
    @Override
    public int hashCode() {
        return name.hashCode();
    }
}