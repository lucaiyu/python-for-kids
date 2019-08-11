
def spaceship_building(cans):
    total_cans=0
    weeks=53
    for week in range(0,weeks):
        total_cans=total_cans+cans
        print('week %s=%s cans' % (week,total_cans))



spaceship_building(2)