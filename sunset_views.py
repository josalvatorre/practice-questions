def sunset_views(buildings, direction):
    _EAST = 'EAST'
    _WEST = 'WEST'

    def iter_from_sun():
        # sun comes from west
        range_ = range(len(buildings))
        if direction == _EAST:
            range_ = reversed(range_)
        return (index for index in range_)

    good_buildings = []

    max_height = 0
    for i in iter_from_sun():
        height = buildings[i]
        if max_height < height:
            good_buildings.append(i)
            max_height = height
        pass

    if len(good_buildings) < 2 or good_buildings[0] < good_buildings[-1]:
        return good_buildings
    else:
        return list(reversed(good_buildings))
