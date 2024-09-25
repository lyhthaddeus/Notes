def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    dic = {}
    start = 0
    ans = 0
    for end, ch in enumerate(s):
        if ch in dic and dic[ch >= start:
            start = dic[ch] + 1
        dic[ch] = end
        ans = max(ans,  end - start + 1)
    return ans

