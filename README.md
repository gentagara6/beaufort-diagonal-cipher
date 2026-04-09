Beaufort Cipher Decryption
Përshkrimi i Projektit
Ky projekt implementon algoritmin Beaufort Cipher për dekriptimin e tekstit të shifruar.
Beaufort është një algoritëm klasik në kriptografi që përdor një çelës për të kthyer tekstin e koduar në formën e tij origjinale.
Algoritmi është reciprok, që do të thotë se e njëjta formulë përdoret si për enkriptim ashtu edhe për dekriptim.

Si funksionon algoritmi
Formula e përdorur është:
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

 Çfarë demonstron ky projekt
	• Implementimin korrekt të algoritmit Beaufort
	• Përdorimin e operacioneve matematikore (modulo 26)
	• Manipulimin e stringjeve në Python
	• Strukturimin e kodit me funksione
	• Validimin e inputit nga përdoruesi

 Shënime
	• Çelësi duhet të përmbajë vetëm shkronja
	• Programi nuk ndryshon karakteret jo-alfabetike (hapësira, numra, etj.)

 Autori
	• Emri: Fiona Grabovci 
