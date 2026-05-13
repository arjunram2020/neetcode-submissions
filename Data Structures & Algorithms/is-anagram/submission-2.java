class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sc = new char[s.length()];
        char[] tc = new char[t.length()];
        for(int i = 0; i<s.length(); i++){
            sc[i] = s.charAt(i);
        }
        for(int j = 0; j<t.length(); j++){
            tc[j] = t.charAt(j);
        }
        Arrays.sort(sc);
        Arrays.sort(tc);
        return(Arrays.toString(sc).equals(Arrays.toString(tc)));
    }
}
