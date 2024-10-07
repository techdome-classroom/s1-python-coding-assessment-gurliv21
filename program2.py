def decode_message(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # Create a DP table with dimensions (n+1) x (m+1)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Base case: empty pattern matches empty string
    dp[0][0] = True
    
    # Fill the first row for cases where the pattern starts with stars
    for i in range(1, n + 1):
        if p[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]  # Match the current character
            elif p[i - 1] == '*':
                # * can match zero characters (dp[i-1][j]) or one/more characters (dp[i][j-1])
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    # The result is whether the entire pattern matches the entire string
    return dp[n][m]

# Test cases
print(decode_message("aa", "a"))       # Output: False
print(decode_message("aa", "*"))       # Output: True
print(decode_message("cb", "?a"))      # Output: False
