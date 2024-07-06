// https://leetcode.com/problems/rotate-image

void rotate(int** matrix, int matrixSize, int* matrixColSize){

    for(int i = 0; i < matrixSize; ++i){
        for(int j = 0; j < *matrixColSize; ++j){
            if(i == j){
                break;
            }
            else{
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }

    for(int i = 0; i < matrixSize; ++i){
        for(int j = 0; j < matrixSize/2; ++j){
            int temp = matrix[i][j];
            matrix[i][j] = matrix[i][matrixSize-j-1];
            matrix[i][matrixSize-j-1] = temp;
        }
    }

    
}