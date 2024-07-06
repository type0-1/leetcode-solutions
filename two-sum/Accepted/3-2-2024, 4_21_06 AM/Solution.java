// https://leetcode.com/problems/two-sum

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        boolean flag = false;

        for(int i = 0; i < nums.length; ++i){
            for(int j = i+1; j < nums.length; ++j){
                if(nums[i] + nums[j] == target){
                    flag = true;
                    result[0] = i;
                    result[1] = j;
                    if(flag){
                        break;
                    }
                }
            }
            if(flag){
                break;
            }
        }

        return result;
    }
}