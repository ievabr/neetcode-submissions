class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        N = len(points)
        result = []

        for point in range(N):
            point_xy = points[point]
            distance = point_xy[0] ** 2 + point_xy[1] ** 2 
            point_distance = (point_xy, distance)
            result.append(point_distance)
            result.sort(key = lambda x: x[1])
        res = [item[0] for item in result]
        res = res[:k]
        return res
        