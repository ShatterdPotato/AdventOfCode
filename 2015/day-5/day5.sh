!#/bin/bash
grep -E '[aeiou].*[aeiou].*[aeiou]' 2015-5 | grep -E "([a-z])\1" | grep -v -E 'ab|cd|pq|xy' | wc -l
