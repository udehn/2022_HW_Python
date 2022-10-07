
class MedianFinder:
    def __init__(self):
        self.sum = 0
        self.cnt = 0

    def addNum(self, value):
        # size <= 5*10^5
        if self.cnt >= 5*pow(10, 5):
            raise ValueError('The number of elements entered is more than 5*10^5')

        # −10^5 <= size of value <= 10^5
        if value > pow(10, 5) or value < -1 * pow(10, 5):
            raise ValueError('The entered value', value, ' < −10^5 or > 10^5')

        self.sum = self.sum + value
        self.cnt = self.cnt + 1

    def findMedian(self):
        if self.cnt == 0:
            return .0
        return round(self.sum / self.cnt, 5)

if __name__ == '__main__':
    median_finder = MedianFinder()
    assert median_finder.findMedian() == .0

    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5

    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.

    # median_finder.addNum(123456789)
    # median_finder.addNum(-111111111)

