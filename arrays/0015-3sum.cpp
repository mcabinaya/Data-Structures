class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res = {};
        vector<int> temp_res(3);
        string temp;
        
        int n = nums.size();
        sort(nums.begin(), nums.begin()+n);
        
        for(int i=0; i<n; i++) {
            //to avoid duplicates
            if ((i==0) || nums[i] != nums[i-1]){
                int l= i+1;
                int r= n-1;
                while(l < r){
                    int sum = nums[i]+nums[l]+nums[r];
                    if( sum == 0){
                        temp_res[0] = nums[i];
                        temp_res[1] = nums[l];
                        temp_res[2] = nums[r];
                        res.push_back(temp_res);
                        l++;
                        r--;
                        //to avoid duplicates
                        while((l<r) && (nums[l] == nums[l-1])){
                            l++;
                        }
                        //to avoid duplicates
                        while((l<r) && (nums[r] == nums[r+1])){
                            r--;
                        }
                    }
                    else if(sum < 0){ l++; }
                    else{ r--; }
                }
            }
        }
        
        return res;   
    }
}
