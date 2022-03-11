# paper_data

in paper_data/misc sind die txt Dateien mit den Daten:

basic.txt

pid3.txt
compass.txt

pid_comp.txt
pid_kalman.txt

kalman2.txt

in paper_data/misc/test_list.txt steht, welche txt datei durch welche 'Einstellungen' entstanden sind


paper_data/misc/test_list.txt:

raw - motor | basic
	einfach nur motor_power(speed)
// raw - motor motoren aufeiner abgestimmt im hardcode (vordefiniert) | na

pid - motor | pid3
pid - compass | compass
	ein pid um mit dem Errorwert die Fahrtrichtung zu ändern

pid - motor kalmann | pid_kalman
	2 Kalmannfilter über die motortick rückgabe beider Motoren (also eigentlich 2 Filter)
pid - compass kalmann | pid_comp
	ein Kalmann über die Rückgabe des Kompass

// pid - motor + compass kalmann | kalmann
2x pid - motor + compass kalmann | kalmann2
	3 Kalmann für Motor1, Motor2, Kompass; 1 pid für beide Motoren; 1 pid für den Kompass
