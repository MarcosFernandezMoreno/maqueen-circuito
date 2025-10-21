music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 10)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 40)
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 40)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 10)
basic.forever(on_forever)
