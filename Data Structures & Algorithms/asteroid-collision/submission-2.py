class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            while stack and stack[-1] > 0 and asteroid < 0:

                # top asteroid smaller
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue

                # equal size
                elif stack[-1] == abs(asteroid):
                    stack.pop()

                break

            else:
                stack.append(asteroid)

        return stack
            
            