// https://leetcode.com/problems/valid-anagram

#include <string.h>


bool isAnagram(char * s, char * t){
    if(strlen(s) != strlen(t)){
        return false;
    }
    else{
        
        int count = 0;
        
        for(int i = 0; i < strlen(s); ++i){
            for(int j = 0; j < strlen(t); ++j){
                if(s[i] == t[j]){
                    count = 1;
                }
            }
            if(!count){
                return false;
            }
            count = 0;
        }

    }
    return true;
}