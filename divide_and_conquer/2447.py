def draw_stars(N):
    if N == 1:
        return ['*']

    Stars = draw_stars(N//3)
    A = []

    for star in Stars:
        A.append(star*3)
    for star in Stars:
        A.append(star+' '*(N//3)+star)
    for star in Stars:
        A.append(star*3)

    return A

N = int(input())
print('\n'.join(draw_stars(N)))