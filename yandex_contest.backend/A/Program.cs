﻿using System;
 
public class Solution {
    static void Main(string[] args) {
        string j = Console.ReadLine();
        string s = Console.ReadLine();
 
        int result = 0;
        foreach (char ch in s) {
            if (j.IndexOf(ch) >= 0) {
                ++result;
            }
        }
 
        Console.WriteLine(result);
    }
}