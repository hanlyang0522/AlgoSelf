def dsearch(pnow, dungeon):
    dmax = 0

    for d in dungeon:
        if pnow >= d[0]:
            dg_tmp = dungeon.copy()
            dg_tmp.remove(d)
            dmax = max(dmax, dsearch(pnow - d[1], dg_tmp) + 1)
        else:
            continue

    return dmax


def solution(k, dungeons):
    return dsearch(k, dungeons)


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
