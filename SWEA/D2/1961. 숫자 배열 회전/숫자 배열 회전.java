import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Solution {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            int[][] mat = new int[N][N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < N; j++) {
                    mat[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            bw.write("#" + test_case + "\n");

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    bw.write(String.valueOf(mat[N - 1 - j][i]));
                }
                bw.write(" ");

                for (int j = 0; j < N; j++) {
                    bw.write(String.valueOf(mat[N - 1 - i][N - 1 - j]));
                }
                bw.write(" ");

                for (int j = 0; j < N; j++) {
                    bw.write(String.valueOf(mat[j][N - 1 - i]));
                }
                bw.write("\n");
            }

        }

        bw.flush();
        bw.close();
    }
}