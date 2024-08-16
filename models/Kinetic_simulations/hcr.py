def hcr(y,t,ke,kb,kd,kf,kr,kc):
    dy0=-kb*y[0]*y[1]+kd*y[2]-ke*y[0]
    dy1=-kb*y[0]*y[1]+kd*y[2]
    dy2=kb*y[0]*y[1]-kd*y[2]-kf*y[2]*y[3]+kr*y[4]+kc*y[4]
    dy3=-kf*y[2]*y[3]+kr*y[4]
    dy4=kf*y[2]*y[3]-kr*y[4]-kc*y[4]
    dy5=kc*y[4]
    return(dy0,dy1,dy2,dy3,dy4,dy5)
