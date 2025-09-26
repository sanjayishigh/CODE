public class minmaxelement {
    public static int[] minmaxans(int nums[]) {
        int max = nums[0];
        int min = nums[0];

        for (int i = 1; i < nums.length; i++) {
            max =  Math.max(max,nums[i]);
            min =  Math.min(min,nums[i]);
        }

        return new int[]{max, min};
    }

    public static void main(String args[]) {
        int nums[] = {1, -2, 3, -4, 5};
        int result[] = minmaxans(nums);
        System.out.println("Minimum : " + result[0]);
        System.out.println("Maximum : " + result[1]);
    }
}
