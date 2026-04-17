# Hill Cipher & Columnar Transposition

Ky projekt implementon dy algoritme klasike të kriptografisë në Python:
- Hill Cipher
- Columnar Transposition



## Udhëzimet për ekzekutim

### Kërkesat
- Python 3.7+
- Nuk nevojiten librari shtesë

### Hapat
1. Shkarkoni projektin nga GitHub (Code → Download ZIP)
2. Hapni terminalin në dosjen e projektit
3. Ekzekutoni:
```
python main.py
```



## Si të përdorni programin

```
--- MENU KRYESORE ---
1. Hill Cipher
2. Columnar Transposition
0. Dalje
```

- Zgjidhni algoritmin
- Shkruani tekstin
- Zgjidhni:
  - 1 = Enkriptim
  - 2 = Dekriptim



## Testimi veçmas

```
python hill_cipher.py
python columnar.py
```



## Përshkrimi i algoritmeve

### Hill Cipher
Hill Cipher është një algoritëm **zëvendësimi** që përdor matematikë (matrica) për të enkriptuar tekstin.  
Ai konsiderohet më i avancuar se metodat e thjeshta sepse përpunon disa shkronja njëkohësisht.

- Çdo shkronjë kthehet në numër (A=0,...,Z=25)
- Teksti ndahet në grupe (p.sh. çifte)
- Shumëzohet me një matricë çelës
- Rezultati merret modulo 26 dhe kthehet përsëri në shkronja

**Shembull:**
HE → [7,4]  
[7,4] × [[3,3],[2,5]] = [33,34]  
[33,34] mod 26 = [7,8] → HI  





