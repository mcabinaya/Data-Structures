class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        // get size
        int numRows = matrix.size();
        int numCols = matrix[0].size();
            
        // initialize temp row and col 
        vector<int> row (numRows, 0);
        vector<int> col (numCols, 0);
        
        // set temp rows and cols to 1, when the index matches
        for(int i=0; i<numRows; i++){
            for(int j=0; j<numCols; j++){
                if (matrix[i][j] == 0){
                    row[i] = 1;
                    col[j] = 1;          
                }               
            }
        }
        
        // again traverse through matrix
        for(int i=0; i<numRows; i++){
            for(int j=0; j<numCols; j++){
                if((row[i] == 1) or (col[j] == 1)){
                    matrix[i][j] = 0;
                }
            }
        }        
    }
};
