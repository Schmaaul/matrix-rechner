

class Matrix:
    rows = []
    sizeX = 0
    sizeY = 0
    def __init__(self) -> None:
        pass
    
    def __init__(self, sizeX, sizeY) -> None:
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.rows = []
        for y in range(sizeY):
            self.rows.append([])
            for x in range(sizeX):
                self.rows[-1].append(0)
    
    def __str__(self) -> str:
        out = ""
        for row in self.rows:
            out += str(row) + "\n"
        out = out[:-1]
        return out
    
    def multiplyRow(self, rowIndex, factor):
        collect = []
        for num in self.rows[rowIndex]:
            num *= factor
            collect.append(num)
        self.rows[rowIndex] = collect
    def divideRow(self, rowIndex, divisor):
        collect = []
        for num in self.rows[rowIndex]:
            num /= divisor
            collect.append(num)
        self.rows[rowIndex] = collect
    def setRow(self, rowIndex, input):
        if self.sizeX != len(input): 
            raise "Wrong length"
        self.rows[rowIndex] = input
    
    def addRowsTogether(self, tagetIndex, usingIndex):
        for x in range(self.sizeX):
            self.rows[tagetIndex][x] += self.rows[usingIndex][x]
                
def main():
    mat = Matrix(4, 3)
    print(mat, "\n")
    mat.setRow(1, [1,2,3,4])
    print(mat, "\n")
    mat.multiplyRow(1, 2)
    print(mat, "\n")
    mat.addRowsTogether(0,1)
    print(mat, "\n")
if __name__ == "__main__":
    main()