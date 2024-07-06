// https://leetcode.com/problems/check-if-it-is-a-straight-line



bool checkStraightLine(int** coordinates, int coordinatesSize, int* coordinatesColSize){
    for(int i = 1; i < coordinatesSize; ++i){
        if(coordinates[i][0] != coordinates[i-1][0]+1 || coordinates[i][1] != coordinates[i-1][1]+1){
            return false;
        }
    }
    return true;
}