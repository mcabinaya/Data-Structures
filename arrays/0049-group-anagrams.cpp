class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string,vector<int>> map = {};
        
        // fill map
        for(int i=0; i<strs.size(); i++){
            string tempStr = strs[i];
            sort(tempStr.begin(), tempStr.end());
            map[tempStr].push_back(i);
        }
        
        // iterate through map and fill result
        for(auto i: map){
            vector<string> temp;
            for(auto j: i.second){
                temp.push_back(strs[j]);
            }
            result.push_back(temp);  
        }
               
        return result;
    }
};
