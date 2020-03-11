# 这个问题等价于将数组分为两组，计算他们差的绝对值的最小值， 即最小化abs(sum(groupA)-sum(groupB)).
# 由于sum(groupA)+sum(groupB)=sum(stones), 此问题又等价于在stones数组找到一组数，使他们的和离sum/2最近，即最小化abs(sum/2-sum(groupA)).
# 获取一个数组中可能得到的所有的和的值，这本身就是一个有子结构的问题。
# 假设我们有个数组[a_0, a_1, ..., a_n-1], 我们已经计算出这个数组中所有的和的可能为集合{sum_0, sum_1, ..., sum_M-1}， 那么在原数组中再增加一个数a_n之后，这个数可能会被分配到{sum_0, sum_1, ..., sum_M-1}中的任意一个，也有可能不加入任意一个。 所以新数组的所有可能的和的集合为{sum_0, sum_1, ..., sum_M-1, sum_0+a_n, sum_1+a_n, ..., sum_M-1+a_n}
# 使用 dp 来 denote 可能取到的所有的和的值
# 最接近sum/2的就是能使两组重量差最小的

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
       
        dp = set([0])
        sum_ = sum(stones)
        for a in stones:
            dp |= set([a+i for i in dp])
        return min(abs(sum_ - 2*i) for i in dp)
