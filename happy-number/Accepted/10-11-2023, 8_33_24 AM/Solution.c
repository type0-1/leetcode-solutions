// https://leetcode.com/problems/happy-number

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int happy_num(int);
int sum(int);

int happy_num(int n){
    int limit = 0;
    while(n != 1){
        
        int temp = n;
        n = sum(temp);
        
        if(limit == 100){
            return false;
        }
        limit++;
    }
    
    return n;
    
}

int sum(int n){
    int total = 0;
    while(n != 0){
        total += (n%10)*(n%10);
        n/=10;
    }
    return total;
}

bool isHappy(int n){

    bool result = happy_num(n);
    return result;
    
}