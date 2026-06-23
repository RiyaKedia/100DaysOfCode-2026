int lengthOfLastWord(char* s) {
    int i = 0, len = 0;

    // Move to end of string
    while (s[i] != '\0') {
        i++;
    }

    // Skip trailing spaces
    i--;
    while (i >= 0 && s[i] == ' ') {
        i--;
    }

    // Count characters of last word
    while (i >= 0 && s[i] != ' ') {
        len++;
        i--;
    }

    return len;
}