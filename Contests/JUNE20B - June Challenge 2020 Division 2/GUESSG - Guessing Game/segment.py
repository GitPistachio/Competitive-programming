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
            raise IndexError(str(idx) + ' index out of range')

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


#sgms = Segment([12, 18], [21, 21], [30, 41], [50, 52])
#print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())


#sgms.setMajorant(41)
#print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())

#sgms.setMinorant(7)
#print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())

#sgms.setMinorant(11)
#print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())

#sgms.exclude([19, 35])
# print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())

# sgms.exclude([37, 38])
# print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())

# sgms.exclude([29, 29])
# print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())

# sgms.exclude([29, 31])
# print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())


# sgms.exclude(21)
# print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())

# sgms.exclude([30, 36])
# print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())

# sgms.exclude([40, 53])
# print(sgms, len(sgms), sgms.size(), sgms[4], sgms.empty(), sgms.getMinorant(), sgms.getMajorant())
