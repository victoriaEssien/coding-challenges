class Robot:

    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.dir = 0
        self.directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        self.labels = ["East", "North", "West", "South"]

    def step(self, num: int) -> None:
        num %= (self.width - 1 + self.height - 1) * 2
        if num == 0:
            num += (self.width - 1 + self.height - 1) * 2
        
        for _ in range(num):
            nx = self.x + self.directions[self.dir][0]
            ny = self.y + self.directions[self.dir][1]

            while not (0 <= nx < self.width and 0 <= ny < self.height):
                self.dir = (self.dir + 1) % 4
                nx = self.x + self.directions[self.dir][0]
                ny = self.y + self.directions[self.dir][1]

            self.x = nx
            self.y = ny
        

    def getPos(self) -> List[int]:
        return [self.x, self.y]
        

    def getDir(self) -> str:
        return self.labels[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()