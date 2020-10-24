def towerOfHanoi(n_disks, source, destin, temp):
    if n_disks == 1:
        print ("Move disk 1 from rod",source,"to rod",destin)
        return
    towerOfHanoi(n_disks-1, source, temp, destin)
    print ("Move disk",n_disks,"from rod",source,"to rod",destin)
    towerOfHanoi(n_disks-1, temp, destin, source)

n_disks = 3
towerOfHanoi(n_disks, 'A', 'C', 'B')
