#寻找interval之间是否有intersection
#interval之间没有intersection的条件： 前面interval的end小于后面interval的start
#对于新加入的interval[i]，需要检查interval[i-1]和interval[i+1]是否都与其无交集
import bisect
class MyCalendar(object):
    def __init__(self):
        self.starts = []
        self.ends = []
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        #查找最后一个比start小的interval
        index = bisect.bisect(self.starts, start)
        #前面的interval的index为index-1
        #检查前面interval的end是否小于等于当前的start
        if index>=1 and self.ends[index-1]>start:
            return False
        #后面的interval的index为index
        #检查后面interval的start是否大于等于当前的end
        if index<len(self.starts) and self.starts[index]<end:
            return False
        bisect.insort(self.starts, start)
        bisect.insort(self.ends, end)
        return True
        
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
