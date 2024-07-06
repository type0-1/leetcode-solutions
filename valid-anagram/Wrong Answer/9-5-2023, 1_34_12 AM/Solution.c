// https://leetcode.com/problems/valid-anagram

#include <string.h>


bool isAnagram(char * s, char * t){
    if(strlen(s) != strlen(t)){
        return false;
    }
    return true;
}