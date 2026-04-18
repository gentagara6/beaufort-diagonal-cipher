Përshkrimi i Projektit

Ky projekt implementon dy algoritme të kriptografisë:
• Beaufort Cipher
• Diagonal Transposition Cipher

Programi është i ndarë në tre pjesë:
• beaufort.py → përmban enkriptimin dhe dekriptimin Beaufort
• diagonal.py → përmban enkriptimin dhe dekriptimin diagonal
• main.py → programi kryesor që lejon përdoruesin të zgjedhë algoritmin dhe operacionin

Si të ekzekutohet programi
1. Kërkesat
	• Python 3 i instaluar
2. Hapat
	1. Klono repository:
	   git clone https://github.com/gentagara6/beaufort-diagonal-cipher.git
	2. Hyr në folderin e projektit:
	   cd beaufort-diagonal-cipher
	3. Ekzekuto programin:
	   python main.py

Çfarë ndodh pas ekzekutimit

Programi shfaq menunë:
1. Beaufort Encrypt
2. Beaufort Decrypt
3. Diagonal Encrypt
4. Diagonal Decrypt
0. Exit

Përdoruesi zgjedh opsionin dhe fut inputet përkatëse.

Algoritmet e implementuara:

1. Beaufort Cipher 
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

Shembull ekzekutimi

Input:
Teksti: HELLO
Celesi: KEY

Output:
Teksti i enkriptuar: DANZQ
Celesi i perdorur: KEY
Teksti i dekriptuar: HELLO

Veçoritë:
	• Punon vetëm me shkronja A–Z 
	• Hapësirat dhe karakteret e tjera nuk ndryshohen 
	• Çelësi duhet të përmbajë vetëm shkronja 
	• Implementim me funksione (encrypt & decrypt) 
	• Përdor operacionin modulo 26 për kriptim


2. Diagonal Transposition Cipher
Ky është një algoritëm transpozimi ku teksti vendoset në një matricë me kolona të caktuara dhe më pas lexohet në mënyrë diagonale për të krijuar ciphertext.

Enkriptimi
Hapat:
1.Teksti pastrohet:
- hiqen hapësirat
- konvertohet në shkronja të mëdha (uppercase)
2.Zgjidhet numri i kolonave (cols)
3.Teksti vendoset në një matricë rresht pas rreshti
4.Nëse është e nevojshme, shtohen karaktere mbushëse (X)
5.Teksti lexohet diagonalisht nga matrica për të krijuar ciphertext.

Shembull

Teksti: HELLO
Kolonat: 2

Matrica:
H E 
L L 
O X

Leximi diagonal: HL → E → L X → O

Ciphertext: HLELXO


Dekriptimi
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

Shembull

Ciphertext: HLELXO
Kolonat: 2

Matrica (pas mbushjes diagonale):
	H E 
	L L 
	O X
Rezultati:
	HELLO

Shënim:
- Gjatë enkriptimit shtohen karaktere X për të plotësuar matricën
- Gjatë dekriptimit këto karaktere hiqen
- Teksti përpunohet pa hapsira

