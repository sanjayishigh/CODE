/*Chocolate Distribution Problem
Last Updated : 23 Jul, 2025
Given an array arr[] of n integers where arr[i] represents the number of chocolates in ith packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that:

Each student gets exactly one packet.
The difference between the maximum and minimum number of chocolates in the packets given to the students is minimized.
        Examples:

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3
Output: 2
Explanation: If we distribute chocolate packets {3, 2, 4}, we will get the minimum difference, that is 2.

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 5
Output: 7
Explanation: If we distribute chocolate packets {3, 2, 4, 9, 7}, we will get the minimum difference, that is 9 - 2 = 7.
*/
import java.util.*;
public class chocdistribution {
    public static int findMinDifference(int[] arr, int m) {
        int n = arr.length;
        if (m == 0 || n == 0) {
            return 0;
        }
        if (n < m) {
            return -1;
        }

        Arrays.sort(arr);
        int minDifference = Integer.MAX_VALUE;

        for (int i = 0; i + m - 1 < n; i++) {
            int currentDifference = arr[i + m - 1] - arr[i];
            minDifference = Math.min(minDifference, currentDifference);
        }

        return minDifference;
    }

    public static void main(String[] args) {
        int[] packets = {7, 3, 2, 4, 9, 12, 56};
        int students = 3;
        System.out.println("Minimum difference is: " + findMinDifference(packets, students));
    }
}
