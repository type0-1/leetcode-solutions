// https://leetcode.com/problems/length-of-last-word

int lengthOfLastWord(char * s){
    int length = 0, i = 0;
    while(s[i] != '\0'){
        i++;
    }
    i--;
    while(s[i] == ' '){
        printf("%c", s[i]);
        i--;
    }

    while(s[i] != ' '){
        i--;
        length++;
    }

    return length;
}