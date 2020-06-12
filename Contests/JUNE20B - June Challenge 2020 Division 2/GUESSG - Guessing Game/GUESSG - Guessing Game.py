# Project name : CodeChef: GUESSG - Guessing Game
# Link         : https://www.codechef.com/JUNE20B/problems/GUESSG
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-12
# Description  :
# Status       : Unaccepted (34235491)
# Tags         : python
# Comment      : 75

import sys

class Segment:
    def __init__(self, *sgms):
        self.data = []
        for sgm in sgms:
            if type(sgm) == int:
                sgm = [sgm, sgm]
            self.data.append(sgm)
        self.data = sorted(self.data)

        self.segments_length = []
        for a, b in self.data:
            self.segments_length.append(b - a + 1)

        self.length = sum(self.segments_length)

    def __getitem__(self, idx):
        """Return value represented at index idx."""
        if idx < -self.length or idx >= self.length:
            raise IndexError('index out of range')

        if idx < 0:
            idx += self.length

        moving_length = 0
        for sgm in self.data:
            length = sgm[1] - sgm[0] + 1
            if idx < length + moving_length:
                return sgm[0] + idx - moving_length
            moving_length += length

    def __len__(self):
        """Return length of all segments."""
        return self.length

    def __str__(self):
        return self.data.__str__()

    def getMinorant(self):
        if self.empty():
            raise ValueError('segment is empty')
        return self.data[0][0]

    def getMajorant(self):
        if self.empty():
            raise ValueError('segment is empty')
        return self.data[-1][1]

    def segmentIndex(self, x):
        if self.getMajorant() < x:
            return (self.size() - 1, None)

        if self.getMinorant() > x:
            return (None, 0)

        low = 0
        high = self.size() - 1
        while low <= high:
            mid = low + (high - low)//2
            if self.data[mid][0] <= x and x <= self.data[mid][1]:
                return (mid, mid)

            if self.data[mid][1] < x:
                low = mid + 1
            else:
                high = mid - 1

        return (high, low)

    def setMajorant(self, majorant):
        if not self.empty() and majorant < self.getMajorant():
            sgm_idx = self.segmentIndex(majorant)
            if sgm_idx == (None, 0):
                self.data = []
                self.segments_length = []
                self.length = 0
            else:
                idx = sgm_idx[0]
                if idx == sgm_idx[1]:
                    self.length -= self.data[idx][1] - majorant
                    self.data[idx][1] = majorant
                    self.segments_length[idx] = majorant - self.data[idx][0] + 1

                self.length -= sum(self.segments_length[idx + 1:])
                self.segments_length = self.segments_length[:idx + 1]
                self.data = self.data[:idx + 1]

    def setMinorant(self, minorant):
        if not self.empty() and minorant > self.getMinorant():
            sgm_idx = self.segmentIndex(minorant)
            if sgm_idx == (self.size() - 1, None):
                self.data = []
                self.segments_length = []
                self.length = 0
            else:
                idx = sgm_idx[1]
                if sgm_idx[0] == idx:
                    self.length -= minorant - self.data[idx][0]
                    self.data[idx][0] = minorant
                    self.segments_length[idx] = self.data[idx][1] - minorant + 1

                self.length -= sum(self.segments_length[:idx])
                self.segments_length = self.segments_length[idx:]
                self.data = self.data[idx:]

    def exclude(self, sgm):
        if type(sgm) == int:
            sgm = [sgm - 1, sgm + 1]
        else:
            sgm = [sgm[0] - 1, sgm[1] + 1]

        if self.empty() or sgm[0] > self.getMajorant() or sgm[1] < self.getMinorant():
            return

        if sgm[1] > self.getMajorant():
            self.setMajorant(sgm[0])
            return

        if sgm[0] < self.getMinorant():
            self.setMinorant(sgm[1])
            return

        lower_sgm_idx = self.segmentIndex(sgm[0])
        upper_sgm_idx = self.segmentIndex(sgm[1])

        lower_idx = lower_sgm_idx[0]
        upper_idx = upper_sgm_idx[1]

        if lower_idx == upper_idx:
            self.length -= sgm[1] - sgm[0] - 1
            self.data.insert(lower_idx + 1, [sgm[1], self.data[lower_idx][1]])
            self.data[lower_idx][1] = sgm[0]
            self.segments_length.insert(lower_idx + 1, self.data[lower_idx + 1][1] - self.data[lower_idx + 1][0] + 1)
            self.segments_length[lower_idx] = self.data[lower_idx][1] - self.data[lower_idx][0] + 1
            return

        if lower_idx == lower_sgm_idx[1]:
            self.length -= self.data[lower_idx][1] - sgm[0]
            self.data[lower_idx][1] = sgm[0]
            self.segments_length[lower_idx] = sgm[0] - self.data[lower_idx][0] + 1

        if upper_sgm_idx[0] == upper_idx:
            self.length -= sgm[1] - self.data[upper_idx][0]
            self.data[upper_idx][0] = sgm[1]
            self.segments_length[upper_idx] = self.data[upper_idx][1] - sgm[1] + 1

        lower_length = self.length - sum(self.segments_length[lower_idx + 1:])
        lower_segments_length = self.segments_length[:lower_idx + 1]
        lower_data = self.data[:lower_idx + 1]

        upper_length = self.length - sum(self.segments_length[:upper_idx])
        upper_segments_length = self.segments_length[upper_idx:]
        upper_data = self.data[upper_idx:]

        self.length = lower_length + upper_length
        self.segments_length = lower_segments_length + upper_segments_length
        self.data = lower_data + upper_data

    def empty(self):
        return (self.length == 0)

    def size(self):
        """Return number of segments."""
        return len(self.data)


def ask(y):
    print(y)
    ans1 = input()

    return ans1


def solveTrivialCase(sgms):
    for a, b in sgms.data:
        for y in range(a, b + 1):
            if ask(y) == 'E':
                return True

    return False


def solve(sgms):
    no_of_unknown_numbers = len(sgms)
    ans1 = ''
    ans2 = ''

    while no_of_unknown_numbers > 4:
        y1_idx = (no_of_unknown_numbers - 1)//2

        y1 = sgms[y1_idx]
        ans1 = ask(y1)
        if ans1 == 'E':
            return True

        if ans2 == 'G' and ans1 == 'L' and y2 > y1:
            sgms.exclude([y1, y2])
            no_of_unknown_numbers = len(sgms)

        elif ans2 == 'L' and ans1 == 'G' and y1 > y2:
            sgms.exclude([y2, y1])
            no_of_unknown_numbers = len(sgms)
        elif ans2 == 'L' and ans1 == 'L' and y1 > y2:
            sgms.setMajorant(y1 - 1)
            no_of_unknown_numbers = len(sgms)

        if ans1 == 'L':
            y2_idx = y1_idx + (no_of_unknown_numbers - 1 - y1_idx)//2
            y2 = sgms[y2_idx]
            ans2 = ask(y2)
            if ans2 == 'E':
                return True

            if ans2 == 'L':
                sgms.setMajorant(y2 - 1)
            else:
                sgms.exclude([y1, y2])
        else:
            y2_idx = y1_idx//2
            y2 = sgms[y2_idx]
            ans2 = ask(y2)
            if ans2 == 'E':
                return True

            if ans2 == 'G':
                sgms.setMinorant(y2 + 1)
            else:
                sgms.exclude([y2, y1])

        no_of_unknown_numbers = len(sgms)

    return solveTrivialCase(sgms)

n = int(input())
res = solve(Segment([1, n]))