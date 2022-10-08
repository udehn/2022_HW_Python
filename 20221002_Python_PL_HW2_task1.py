
class MedianFinder:
    def __init__(self):
        self.numlist = []
        self.cnt = 0

    def addNum(self, value):
        # size <= 5*10^5
        if self.cnt >= 5*pow(10, 5):
            raise ValueError('The number of elements entered is more than 5*10^5')

        if value > pow(10, 5) or value < -1 * pow(10, 5):
            raise ValueError('The entered value', value, ' < −10^5 or > 10^5')

        self.numlist.append(value)
        self.cnt = self.cnt + 1
        for i in range(self.cnt-1, -1, -1):
            if self.numlist[i-1] > self.numlist[i]:
                temp = self.numlist[i-1]
                self.numlist[i-1] = self.numlist[i]
                self.numlist[i] = temp
            else:
                break

    def findMedian(self):
        if self.cnt == 0:
            return .0
        elif self.cnt % 2 == 0:
            return (self.numlist[int(self.cnt / 2) - 1] + self.numlist[int(self.cnt / 2)]) / 2
        else:
            return self.numlist[int(self.cnt/ 2)]

if __name__ == '__main__':
    median_finder = MedianFinder()
    assert median_finder.findMedian() == .0

    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5

    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.

    median_finder.addNum(9)
    median_finder.addNum(6)
    median_finder.addNum(6)
    assert median_finder.findMedian() == 4.5

    median_finder.addNum(2)
    assert median_finder.findMedian() == 3.