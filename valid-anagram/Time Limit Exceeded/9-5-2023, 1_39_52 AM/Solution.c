// https://leetcode.com/problems/valid-anagram

#include <string.h>


bool isAnagram(char * s, char * t){
    if(strlen(s) != strlen(t)){
        return false;
    }
    else{
        
        for(int i = 0; i < strlen(s); ++i){
            for(int j = i+1; j < strlen(s); ++j){
                if(s[i] < s[j]){
                    char temp = s[i];
                    s[i] = s[j];
                    s[j] = temp;
                }
            }
        }

        for(int i = 0; i < strlen(t); ++i){
            for(int j = i+1; j < strlen(t); ++j){
                if(t[i] < t[j]){
                    char temp = t[i];
                    t[i] = t[j];
                    t[j] = temp;
                }
            }
        }

        for(int i = 0; i < strlen(s); ++i){
            if(s[i] != t[i]){
                return false;
            }
        }

        return true;

    }
    return true;
}