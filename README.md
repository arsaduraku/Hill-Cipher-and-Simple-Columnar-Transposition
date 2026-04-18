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

# Columnar Transposition Cipher

Ky projekt implementon algoritmin klasik të kriptografisë **Columnar Transposition Cipher** në Python.

## Udhëzimet për ekzekutim

### Kërkesat

* Python 3.7+
* Nuk nevojiten libra shtesë

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
1. Columnar Transposition
0. Dalje
```

* Zgjidhni algoritmin
* Shkruani tekstin
* Zgjidhni:

  * 1 = Enkriptim
  * 2 = Dekriptim
* Jepni numrin e kolonave

## Testimi veçmas

```
python columnar.py
```

## Përshkrimi i algoritmit

**Columnar Transposition Cipher** është një algoritëm i kriptografisë që nuk ndryshon shkronjat, por vetëm renditjen e tyre duke përdorur një tabelë.

### Si funksionon:

* Teksti pastrohet (hiqen hapësirat dhe bëhet me shkronja të mëdha)
* Teksti vendoset në një tabelë me rreshta dhe kolona
* Nëse tabela nuk mbushet plotësisht, shtohen shkronja mbushëse (p.sh. `X`)
* Për enkriptim:

  * Lexohen kolonat nga lart-poshtë
* Për dekriptim:

  * Teksti vendoset kolonë pas kolone
  * Lexohen rreshtat për të marrë tekstin origjinal

### Shembull:

Teksti:

```
SIGURIAETEDHENAVE
```

Me 5 kolona:

```
S I G U R
I A E T E
D H E N A
V E X X X
```

**Enkriptimi (lexim sipas kolonave):**

```
SIDV IAH E GEE UXN RETAX
```

**Rezultati final:**

```
SIDVIAHEGEEUXNRETAX
```

### Vërejtje

* Shkronjat `X` përdoren për mbushje dhe hiqen gjatë dekriptimit
* Renditja e kolonave është nga e majta në të djathtë (pa çelës kompleks)

## Autori

Projekt për implementim të algoritmeve klasike të kriptografisë në Python.






