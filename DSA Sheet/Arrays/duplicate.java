public class duplicate {
    public static void dupli(int nums[]) {
        for (int i = 0; i < nums.length; i++) {
            boolean alreadyCounted = false;

            // Check if already counted
            for (int k = 0; k < i; k++) {
                if (nums[k] == nums[i]) {
                    alreadyCounted = true;
                    break;
                }
            }
            if (alreadyCounted) {
                continue;
            }

            // Count frequency
            int count = 1;
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    count++;
                }
            }

            System.out.println(nums[i] + " is repeated " + count + " times");
        }
    }

    public static void main(String args[]) {
        int nums[] = {1, -2, 3, -4, 5, 3, 1, -2};
        dupli(nums);
    }
}
