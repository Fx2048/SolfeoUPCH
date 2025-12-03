Hanoi n origen desti aux |:
    if n > 0 |:
        temp <- n - 1
        Hanoi temp origen aux desti
        nota <- 60 + n
        (:) nota
        <w> origen "-->" desti
        Hanoi temp aux desti origen
    :|
:|

Main |:
    Hanoi 4 1 3 2
:|