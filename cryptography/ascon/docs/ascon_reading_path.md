# Ascon Cryptography — Reading Path

A structured guide to the key literature on Ascon, from the official standard to advanced cryptanalysis and implementation research.

---

## 1. Start Here: Official Standards & Design Rationale

- **NIST SP 800-232 (2025)** — Turan, McKay, Chang, Kang, Kelsey.
  *Ascon-Based Lightweight Cryptography Standards for Constrained Devices: Authenticated Encryption, Hash, and XOF.*
  \[[doi](https://doi.org/10.6028/NIST.SP.800-232)\]
  → The current official standard. Read this first for the normative specification.

- **Journal of Cryptology (2021)** — Dobraunig, Eichlseder, Mendel, Schläffer.
  *Ascon v1.2: Lightweight Authenticated Encryption and Hashing.*
  \[[doi](https://doi.org/10.1007/s00145-021-09398-9)\]
  → The peer-reviewed reference paper. Best companion to the standard.

- **NIST Submission (2019)** — Dobraunig et al.
  *Ascon v1.2 — Submission to the NIST Lightweight Cryptography competition.*
  \[[nist](https://csrc.nist.gov/Projects/lightweight-cryptography)\] \[[web](https://ascon.iaik.tugraz.at)\]
  → Full design rationale, parameter choices, and designers' security analysis.

- **CAESAR Submission (2016)** — Dobraunig et al.
  *Ascon v1.2 — Round 3 CAESAR submission.*
  \[[caesar](https://competitions.cr.yp.to/caesar-submissions.html)\] \[[web](https://ascon.iaik.tugraz.at)\]
  → Original competition document; useful for historical context.

---

## 2. Security of the Mode

Understanding how the Ascon sponge/duplex mode achieves its security guarantees.

- Jovanovic, Luykx, Mennink. **Beyond 2^(c/2) Security in Sponge-Based AE Modes.** ASIACRYPT 2014.
  \[[doi](https://doi.org/10.1007/978-3-662-45611-8_11)\] \[[eprint](https://eprint.iacr.org/2014/373)\]

- Daemen, Mennink, Van Assche. **Full-State Keyed Duplex with Built-In Multi-user Support.** ASIACRYPT 2017.
  \[[doi](https://doi.org/10.1007/978-3-319-70700-6_7)\] \[[eprint](https://eprint.iacr.org/2017/498)\]

- Mennink, Lefevre. **Generic Security of the Ascon Mode: On the Power of Key Blinding.** ePrint 2023/796.
  \[[eprint](https://eprint.iacr.org/2023/796)\]

- Chakraborty, Dhar, Nandi. **Exact Security Analysis of ASCON.** ASIACRYPT 2023.
  \[[doi](https://doi.org/10.1007/978-981-99-8727-6_1)\]

- Lefevre, Mennink. **SoK: Security of the Ascon Modes.** ePrint 2024/1969.
  \[[eprint](https://eprint.iacr.org/2024/1969)\]
  → Comprehensive survey of mode-level security results.

### Preimage & Collision Security (Hash/XOF Mode)

- Lefevre, Mennink. **Tight Preimage Resistance of the Sponge Construction.** CRYPTO 2022.
  \[[doi](https://doi.org/10.1007/978-3-031-15982-4_8)\]
  → Improves the generic preimage bound to 2^192.

---

## 3. Cryptanalysis of the Permutation

The heart of Ascon's security rests on its 5-round (or 12-round) permutation. These papers attack reduced-round variants.

### Differential & Linear Attacks

- Dobraunig et al. **Cryptanalysis of Ascon.** CT-RSA 2015.
  \[[doi](https://doi.org/10.1007/978-3-319-16715-2_16)\] \[[eprint](https://eprint.iacr.org/2015/030)\]
  *(Starting point — covers 6-round key recovery)*

- Erlacher, Mendel, Eichlseder. **Bounds for the Security of Ascon against Differential and Linear Cryptanalysis.** ToSC 2022(1).
  \[[doi](https://doi.org/10.46586/tosc.v2022.i1.64-87)\]

- El Hirch, Mella, Mehrdad, Daemen. **Improved Differential and Linear Trail Bounds for ASCON.** ToSC 2022(4).
  \[[doi](https://doi.org/10.46586/tosc.v2022.i4.145-178)\] \[[eprint](https://eprint.iacr.org/2022/1377)\]
  → Proves 6-round bounds beyond 2^128.

- Degré, Derbez, Lahaye, Schrottenloher. **New Models for the Cryptanalysis of ASCON.** ePrint 2024/298.
  \[[eprint](https://eprint.iacr.org/2024/298)\]
  → Improved 7-round lower bounds for differential characteristics.

### Differential-Linear Attacks

- Bar-On, Dunkelman, Keller, Weizman. **DLCT: A New Tool for Differential-Linear Cryptanalysis.** EUROCRYPT 2019.
  \[[eprint](https://eprint.iacr.org/2019/256)\]

- Liu, Lu, Lin. **Differential-Linear Cryptanalysis from an Algebraic Perspective.** CRYPTO 2021.
  \[[doi](https://doi.org/10.1007/978-3-030-84252-9_14)\]

- Hu, Peyrin, Tan, Yap. **Revisiting Higher-Order Differential-Linear Attacks from an Algebraic Perspective.** ASIACRYPT 2023.
  \[[doi](https://doi.org/10.1007/978-981-99-8727-6_3)\]
  *(8-round distinguisher at 2^48; full-round zero-sum at 2^55)*

- Peng, Zhang, Weng, Ding. **New Approaches for Estimating the Bias of Differential-Linear Distinguishers.** CRYPTO 2024.
  \[[doi](https://doi.org/10.1007/978-3-031-68385-5_12)\] \[[eprint](https://eprint.iacr.org/2024/871)\]

### Cube Attacks

- Li, Dong, Wang. **Conditional Cube Attack on Round-Reduced ASCON.** ToSC 2017(1).
  \[[doi](https://doi.org/10.13154/tosc.v2017.i1.175-202)\] \[[eprint](https://eprint.iacr.org/2017/160)\]

- Li, Zhang, Wang, Wang. **Cryptanalysis of Round-Reduced ASCON.** Science China Information Sciences 2017.
  \[[doi](https://doi.org/10.1007/s11432-016-9114-3)\]

- Rohit, Hu, Sarkar, Sun. **Misuse-Free Key-Recovery and Distinguishing Attacks on 7-Round Ascon.** ToSC 2021(1).
  \[[doi](https://doi.org/10.46586/tosc.v2021.i1.130-155)\] \[[eprint](https://eprint.iacr.org/2021/194)\]

- Rohit, Sarkar. **Diving Deep into the Weak Keys of Round Reduced Ascon.** ToSC 2021(4).
  \[[doi](https://doi.org/10.46586/tosc.v2021.i4.74-99)\] \[[eprint](https://eprint.iacr.org/2021/1556)\]

- Hu. **Improved Conditional Cube Attacks on Ascon AEADs with a Break-Fix Strategy.** ToSC 2024(2).
  \[[doi](https://doi.org/10.46586/tosc.v2024.i2.118-140)\] \[[eprint](https://eprint.iacr.org/2024/743)\]
  *(7-round attack on Ascon-128a with 2^70 data and 2^72.4 time)*

### Integral & Division Property

- Todo. **Structural Evaluation by Generalized Integral Property.** EUROCRYPT 2015.
  \[[doi](https://doi.org/10.1007/978-3-662-46800-5_13)\] \[[eprint](https://eprint.iacr.org/2015/090)\]

- Ghosh, Dunkelman. **Automatic Search for Bit-Based Division Property.** LATINCRYPT 2021.
  \[[doi](https://doi.org/10.1007/978-3-030-88238-9_4)\] \[[eprint](https://eprint.iacr.org/2021/965)\]

- Hadipour et al. **Improved Search for Integral, Impossible Differential and Zero-Correlation Attacks.** ToSC 2024(1).
  \[[doi](https://doi.org/10.46586/tosc.v2024.i1.234-325)\] \[[eprint](https://eprint.iacr.org/2023/1701)\]

### Preimage Attacks on Hash/XOF

- Qin, Hua, Dong, Yan, Wang. **MitM Preimage Attacks on Sponge-Based Hashing.** EUROCRYPT 2023.
  \[[doi](https://doi.org/10.1007/978-3-031-30634-1_13)\]

- Li, He, Chen, Guo, Qiu. **Automatic Preimage Attack Framework on Ascon (Linearize-and-Guess).** ToSC 2023(3).
  \[[doi](https://doi.org/10.46586/tosc.v2023.i3.74-100)\] \[[eprint](https://eprint.iacr.org/2023/1266)\]

- Baek, Kim, Kim. **Preimage Attacks on Reduced-Round Ascon-Xof.** Des. Codes Cryptogr. 92(8), 2024.
  \[[doi](https://doi.org/10.1007/s10623-024-01383-2)\] \[[eprint](https://eprint.iacr.org/2024/371)\]

- Niu, Hu, Sun, Zhang, Wang. **Speeding Up Preimage and Key-Recovery Attacks with Highly Biased Differential-Linear Approximations.** CRYPTO 2024.
  \[[doi](https://doi.org/10.1007/978-3-031-68385-5_11)\] \[[eprint](https://eprint.iacr.org/2024/857)\]

### Collision Attacks on Hash

- Zong, Dong, Wang. **Collision Attacks on Round-Reduced Ascon-Hash/Xof.** ePrint 2019/1115.
  \[[eprint](https://eprint.iacr.org/2019/1115)\]

- Gérault, Peyrin, Tan. **Exploring Differential-Based Distinguishers and Forgeries for ASCON.** ToSC 2021(3).
  \[[doi](https://doi.org/10.46586/tosc.v2021.i3.102-136)\] \[[eprint](https://eprint.iacr.org/2021/1103)\]

- Yu, Liu, Wang, Sun, Meier. **A Closer Look at the S-Box: Deeper Analysis of Round-Reduced ASCON-HASH.** SAC 2023.
  \[[doi](https://doi.org/10.1007/978-3-031-53368-6_14)\]

- Dong, Zhao, Qin, Hou, Zhang, Wang. **Generic MitM Attack Frameworks on Sponge Constructions.** CRYPTO 2024.
  \[[doi](https://doi.org/10.1007/978-3-031-68385-5_13)\] \[[eprint](https://eprint.iacr.org/2024/604)\]

---

## 4. Structural Properties

- Göloglu, Rijmen, Wang. **On the Division Property of S-Boxes.** ePrint 2016/188.
  \[[eprint](https://eprint.iacr.org/2016/188)\]

- Leander, Tezcan, Wiemer. **Searching for Subspace Trails and Truncated Differentials.** ToSC 2018(1).
  \[[doi](https://doi.org/10.13154/tosc.v2018.i1.74-100)\]
  → Shows no good subspace trails exist for Ascon.

- Makarim, Rohit. **Towards Tight Differential Bounds of Ascon — A Hybrid Usage of SMT and MILP.** ToSC 2022(3).
  \[[doi](https://doi.org/10.46586/tosc.v2022.i3.303-340)\]

- Udovenko. **MILP Modeling of Boolean Functions by Minimum Number of Inequalities.** ePrint 2021/1099.
  \[[eprint](https://eprint.iacr.org/2021/1099)\]

- Beierle, Felke, Leander, Neumann, Stennes. **On Perfect Linear Approximations and Differentials over Two-Round SPNs.** CRYPTO 2023.
  \[[doi](https://doi.org/10.1007/978-3-031-38548-3_22)\]

- Naito, Sasaki, Sugawara. **Committing Security of Ascon: Cryptanalysis on Primitive and Proof on Mode.** ToSC 2023(4).
  \[[doi](https://doi.org/10.46586/tosc.v2023.i4.420-451)\]

- Pal, Chandratreya, Chowdhury. **New Techniques for Modeling SBoxes: An MILP Approach.** CANS 2023.
  \[[doi](https://doi.org/10.1007/978-981-99-7563-1_17)\]

---

## 5. Related Functionality: MAC, PRF, Leakage

- Dobraunig et al. **Ascon MAC, PRF, and Short-Input PRF.** CT-RSA 2024.
  \[[doi](https://doi.org/10.1007/978-3-031-58868-6_10)\] \[[eprint](https://eprint.iacr.org/2021/1574)\]
  → Extends Ascon to standalone message authentication.

- Vaudenay, Vizár. **Can Caesar Beat Galois? — Robustness Against Nonce Reusing and High Data Complexity Attacks.** ACNS 2018.
  \[[doi](https://doi.org/10.1007/978-3-319-93387-0_13)\] \[[eprint](https://eprint.iacr.org/2017/1147)\]

- Forler, List, Lucks, Wenzel. **Reforgeability of Authenticated Encryption Schemes.** ACISP 2017.
  \[[doi](https://doi.org/10.1007/978-3-319-59870-3_16)\] \[[eprint](https://eprint.iacr.org/2017/332)\]

- Guo, Pereira, Peters, Standaert. **Towards Lighter Leakage-Resilient AE from the Duplex Construction.** ePrint 2019/193.
  \[[eprint](https://eprint.iacr.org/2019/193)\]

---

## 6. Implementations & Side-Channel Analysis

- Groß, Wenger, Dobraunig, Ehrenhöfer. **Suit up! — Made-to-Measure Hardware Implementations of Ascon.** DSD 2015.
  \[[doi](https://doi.org/10.1109/DSD.2015.70)\] \[[eprint](https://eprint.iacr.org/2015/034)\]

- Groß, Wenger, Dobraunig, Ehrenhöfer. **Ascon Hardware Implementations and Side-Channel Evaluation.** Microprocessors and Microsystems 52, 2017.
  \[[doi](https://doi.org/10.1016/j.micpro.2017.05.003)\]

- Gross, Mangard. **Reconciling d+1 Masking in Hardware and Software.** CHES 2017.
  \[[eprint](https://eprint.iacr.org/2017/103)\]

- Gross, Iusupov, Bloem. **Generic Low-Latency Masking in Hardware.** TCHES 2018(2).
  \[[doi](https://doi.org/10.13154/tches.v2018.i2.1-21)\] \[[eprint](https://eprint.iacr.org/2017/1223)\]

- Adomnicai, Fournier, Masson. **Masking ACORN and Ascon in Software.** ePrint 2018/708.
  \[[eprint](https://eprint.iacr.org/2018/708)\]

- Samwel, Daemen. **DPA on Hardware Implementations of Ascon and Keyak.** CF 2017.
  \[[doi](https://doi.org/10.1145/3075564.3075573)\]

- Bellizia et al. **Mode-Level vs. Implementation-Level Physical Security in Symmetric Cryptography.** CRYPTO 2020.
  \[[doi](https://doi.org/10.1007/978-3-030-56784-2_13)\]

- Dhooghe. **Analyzing Masked Ciphers Against Transition and Coupling Effects.** ePrint 2021/1095.
  \[[eprint](https://eprint.iacr.org/2021/1095)\]

- Luo, Wu, Li, Zhang, Liu. **An Efficient Soft Analytical Side-Channel Attack on Ascon.** WASA 2022.
  \[[doi](https://doi.org/10.1007/978-3-031-19214-2_21)\]

---

## Suggested Reading Order

```
[1] NIST SP 800-232 (standard)
 └─► Dobraunig et al., JoC 2021 (design paper)
      └─► NIST/CAESAR submission (design rationale)
           ├─► Mode security: Daemen 2017 → Mennink 2023 → SoK 2024
           └─► Permutation cryptanalysis:
                ├─► CT-RSA 2015 (baseline attacks)
                ├─► ToSC 2022 bounds (Erlacher / El Hirch)
                └─► ASIACRYPT 2023 / CRYPTO 2024 (state of the art)
```

---

*Compiled from the official Ascon publications page: [ascon.iaik.tugraz.at](https://ascon.iaik.tugraz.at)*
