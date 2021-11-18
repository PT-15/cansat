#include <bits/stdc++.h>
using namespace std;

int main(){
	ofstream temperatura;
	ofstream humedad;
	ofstream presion;
	ofstream altitud;

	altitud.open("altitud.txt");
	temperatura.open("temperatura.txt");
	presion.open("presion.txt");
	humedad.open("humedad.txt");
	if (!altitud || !temperatura || !presion || !humedad){
		cerr << "Error: una de los ficheros no pudo ser abierto" << endl;
		exit(1);
	}

	int time, temp, hum, pres, alt;
	while (cin >> time){
		cin >> temp >> hum >> pres >> alt;
		temperatura << time << " " << temp << "\n";
		humedad << time << " " << hum << "\n";
		presion << time << " " << pres << "\n";
		altitud << time << " " << alt << "\n";
	}
	temperatura.close();
	humedad.close();
	presion.close();
	altitud.close();
	return 0;
}
