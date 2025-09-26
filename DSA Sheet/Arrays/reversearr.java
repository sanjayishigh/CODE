public class reversearr {
    public static int[] reversearray(int nums[]) {
        int first = 0;
        int last = nums.length - 1;
        while(first<last){
           int temp = nums[first];
           nums[first] = nums[last];
           nums[last] = temp;
           first ++;
           last --;
        }
        return nums;
    }

    public static void main(String args[]) {
        int nums[] = {1, -2, 3, -4, 5};

        reversearray(nums);
        for(int i = 0;i< nums.length ; i++){
            System.out.print(nums[i] + " ");
        }

    }
}
