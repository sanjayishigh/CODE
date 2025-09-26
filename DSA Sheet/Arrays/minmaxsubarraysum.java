public class minmaxsubarraysum {
    public static int[] minmaxans(int nums[]) {
        int currMax = nums[0];
        int maxSum = nums[0];

        int currMin = nums[0];
        int minSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currMax = Math.max(nums[i], currMax + nums[i]);
            maxSum = Math.max(maxSum, currMax);

            currMin = Math.min(nums[i], currMin + nums[i]);
            minSum = Math.min(minSum, currMin);
        }

        return new int[]{minSum, maxSum};
    }

    public static void main(String args[]) {
        int nums[] = {1, -2, 3, -4, 5};
        int result[] = minmaxans(nums);
        System.out.println("Minimum Subarray Sum: " + result[0]);
        System.out.println("Maximum Subarray Sum: " + result[1]);
    }
}
