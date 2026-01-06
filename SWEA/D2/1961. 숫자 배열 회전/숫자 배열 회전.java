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

            for (int y = 0; y < N; y++) {
                int k = 0;
                int l = 0;

                for (int x = 0; x < N * 3; x++) {
                    if (k == N) {
                        k = 0;
                        l++;

                        bw.write(" ");
                    }

                    if (l == 0) { // 90도
                        bw.write(String.valueOf(mat[N - 1 - k][y]));
                    } else if (l == 1) { // 180도
                        bw.write(String.valueOf(mat[N - 1 - y][N - 1 - k]));
                    } else { // 270도
                        bw.write(String.valueOf(mat[k][N - 1 - y]));
                    }

                    k++;
                }

                bw.write("\n");
            }

        }

        bw.flush();
        bw.close();
    }
}