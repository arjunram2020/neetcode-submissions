class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> n = new ArrayList<Integer>();
        for(int i = 0; i<nums.length; i++){
            if(n.contains(nums[i])){
                return true;
            }
            n.add(nums[i]);
        }
        return false;
    }
}
