class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        count = 0
        counter = [0]*n
        counter[0] = 1

        for i in range(1, n):
            count += counter[i-delay]
            count -= counter[i-forget]
            count %= (10**9 + 7)
            counter[i] = count

        count = sum(counter[-forget:])
        return count % (10**9 + 7)