Beaufort Cipher 

Përshkrimi i Projektit
Beaufort Cipher është një algoritëm klasik kriptografik që përdor një çelës për të transformuar tekstin e lexueshëm (plaintext) në tekst të koduar (ciphertext) dhe anasjelltas.
Është një algoritëm reciprok (simetrik), që do të thotë se e njëjta formulë matematikore përdoret si për enkriptim ashtu edhe për dekriptim.

Si funksionon algoritmi
Formula e përdorur është:
C = (K − M) mod 26
M = (K - C) mod 26
Ku:
	• M → shkronja e mesazhit (plaintext)
	• K → shkronja e çelësit (key)
	• C → shkronja e tekstit të shifruar (ciphertext)
Çdo shkronjë konvertohet në një numër:
A = 0, B = 1, ..., Z = 25

 Si të ekzekutohet programi
1. Kërkesat
	• Python 3 i instaluar
2. Hapat
	1. Shkarko projektin nga GitHub
	2. Hap terminalin në folderin e projektit
	3. Ekzekuto komandën:
python main.py

Shembull ekzekutimi
Input:
Teksti: HELLO
Celesi: KEY
Output:
Teksti i shifruar: HELLO
Celesi i perdorur: KEY
Teksti i dekriptuar: DANZQ

Veçoritë:
	• Punon vetëm me shkronja A–Z 
	• Hapësirat dhe karakteret e tjera nuk ndryshohen 
	• Çelësi duhet të përmbajë vetëm shkronja 
	• Implementim me funksione (encrypt & decrypt) 
	• Përdor operacionin modulo 26 për kriptim


Diagonal Transposition Cipher

Përshkrimi:
Ky është një algoritëm transpozimi ku teksti vendoset në një matricë me kolona të caktuara dhe më pas lexohet në mënyrë diagonale për të krijuar ciphertext.

Enkriptimi
Hapat:
1.Teksti pastrohet:
- hiqen hapësirat
- konvertohet në shkronja të mëdha (uppercase)
2.Zgjidhet numri i kolonave (cols)
3.Teksti vendoset në një matricë rresht pas rreshti
4.Nëse teksti nuk mbush matricën plotësisht:
- shtohen karaktere mbushëse (zakonisht X)
5.Teksti lexohet diagonalisht nga matrica për të krijuar ciphertext.

Shembull:

Teksti: HELLO
Kolonat: 3

Matrica:
H E L
L O X

Leximi diagonal: H → E L → L O → X

Ciphertext: HLEOLX


Dekriptimi

Përshkrimi:
Dekriptimi ne Diagonal Transposition Cipher është procesi i rikthimit të tekstit origjinal nga ciphertext duke përdorur të njëjtin numër kolonash që është përdorur gjatë enkriptimit.
Ky proces është i kundërti i enkriptimit: matrica mbushet në mënyrë diagonale dhe më pas lexohet rresht pas rreshti.

Hapat:
1. Merret ciphertext dhe numri i kolonave (cols)
2. Llogaritet numri i rreshtave:
	- rows = ceil(len(ciphertext)/cols)
3. Krijohet një matricë bosh
4. Matrica mbushet diagonalisht me tekstin e koduar
5. Teksti lexohet normalisht:
	- rresht pas rreshti(majtas -> djathtas)
6. Hiqen karakteret mbushëse (X) në fund

Shembull:
Ciphertext: HLEOLX
Kolonat: 3

Matrica (pas mbushjes diagonale):
	H E L
	L O X
Rezultati:
	HELLO

Shënim:
- Gjatë enkriptimit shtohen karaktere X për të plotësuar matricën
- Gjatë dekriptimit këto karaktere hiqen
- Teksti përpunohet pa hapsira

