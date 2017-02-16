# CTF Crypto Writeups  by sonickun
これまでに自分が解いたCTFの暗号問題のWriteupをまとめた場所

[ToDoリスト](todo.md)

※Difficultyの評価は個人の主観に基づいて適当に決めています。

#### 問題一覧

| Year | CTF | Problem | Point | Crypto | Keywords | Difficulty|
| :--: | :-- | :------ | ----: | :----: | :------- | :-------: |
| 2016 | Sharif CTF | [LSB Oracle](2016/sharif-ctf/lsb-oracle) | 150 | RSA | LSB Oracle Attack | C |
| 2016 | Sharif CTF | [TPQ](2016/sharif-ctf/tpq) | 150 | RSA | Encryption Oracle, 10 primes | C |
| 2016 | 0CTF | [RSA?](2016/0ctf/rsa/) | 2    | RSA    | Multi-prime RSA, Low public exponent attack| B |
| 2016 | Boston Key Party CTF | [Bob's hat](2016/boston-key-party/bobs-hat/) | 4    | RSA | Felmat法, 素数の使いまわし, small prime, Wiener's Attack| C |
| 2016 | Boston Key Party CTF | [HMAC_CRC](2016/boston-key-party/hmac_crc/)  | 5    | - | CRC(巡回冗長検査) | B |
| 2016 | Google CTF | [Eucalypt Forest](2016/google-ctf/eucalypt-forest/) | 100 | AES | CBCモード, IV改ざん | C |
| 2016 | Google CTF | [Wolf Spider](2016/google-ctf/wolf-spider/) | 125 | AES | CBCモード, Padding oracle attack, length-extension attack | A |
| 2016 | H4ckIT CTF | [Ninja scheme](2016/h4ckit-ctf/ninja-scheme/) | 195 | Original | Feistel構造 | C |
| 2016 | Hack the Vote | [Babyhands](2016/hack-the-vote/babyhands/) | 300 | RSA | Wiener's attack | C |
| 2016 | Hack the Vote | [Box of Ballots](hack-the-vote/boxes-of-ballots/) | 200 | AES | CBCモード | B |
| 2016 | Hack the Vote | [Trunp Trump](2016/hack-the-vote/trump-trump/) | 100 | Original | デジタル署名, Modulo演算 | C |
| 2016 | Hack.lu CTF | [Cryptolocker](2016/hack.lu-ctf/cryptolocker/) | 200 | AES | CBCモード, Padding検査 | C |
| 2016 | Hack.lu CTF | [Redacted](2016/hack.lu-ctf/redacted/) | 200 | RSA | 秘密鍵読経 | C |
| 2016 | HITB Facebook CTF | [Capture Mexico-TLS](2016/hitb-facebook-ctf/capture-mexico-tls/) | 200 | RSA | TLS handshake, RSA-CRT fault Attack | B |
| 2016 | HITCON CTF quals | [Hackpad](2016/hitcon-ctf-quals/hackpad/) | 150 | AES | CBCモード, Paddin oracle attack | C |
| 2016 | HITCON CTF quals | [PAKE](2016/hitcon-ctf-quals/pake) | PAKE | | DH鍵共有 | B |
| 2016 | Insomni'hack Teaser CTF | [Bring the noise](2016/insomnihack-teaser/bring-the-noise/) | 200 | - | Programming, Modulo演算 | C |
| 2016 | Tokyo Westerns CTF | [Backpacker's cihper (easy mode)](2016/mma-ctf-2nd/backpackers-cipher-easy-mode/) | 200 | Original knapsack | Merkle-Hellmanナップサック暗号もどき | A |
| 2016 | Tokyo Westerns CTF | [ESPer](2016/mma-ctf-2nd/esper/) | 180 |  RSA | RSA-CRT Fault Attack | B |
| 2016 | Tokyo Westerns CTF | [Super Express](2016/mma-ctf-2nd/super-express/) | 100 | 換字式暗号 | 線形写像 | C |
| 2016 | Tokyo Westerns CTF | [Twin Primes](2016/mma-ctf-2nd/twin-primes/) | 50 | RSA | 双子素数 | C |
| 2016 | Tokyo Westerns CTF | [Vignere Cipher](2016/mma-ctf-2nd/vignere-cipher/) | 200 | Vignere | カシスキーテスト, Base64 | B |
| 2016 | Nuit du Hack CTF Quals | [Invest](2016/nuit-du-hack-ctf/invest/) | 50 | Original | Pcap Forensic, 論理回路 | C |
| 2016 | SECCON CTF quqls | [biscuiti](2016/seccon-ctf-quals/biscuiti/) | 300 | AES | SQLインジェクション, CBCモード, Paddin oracle attack | A |
| 2016 | Sharif University CTF | [High-speed RSA Keygen](2016/su-ctf/high-speed-rsa-keygen/) | 150 | RSA | Coppersmithの定理, High-bit Known Attack | B |  |
| 2016 | CSAW CTF | [regrexpire](2016/csaw-ctf-quals/regexpire/) | 100 | - | Programming, 正規表現 | C |
| 2015 | Hack.lu CTF | [Creative Cheating](2015/hack.lu-ctf/creative-cheating/) | 150 | RSA | Pcap Forensic, Signatures | C |
| 2015 | MMA CTF | [Alicegame](2015/mma-ctf/alice-game/) | 250 | ElGamal | Pohlig–Hellman algorithm, Baby-step Giant-step algorithm | A |
| 2015 | Plaid CTF | [Strength](2015/plaid-ctf/strength/) | 110 | RSA | Common Modulus Attack | C |
| 2015 | SECCON CTF Quals | [Find the prime numbers](2015/seccon-ctf-quals/find-the-prime-numbers/) | 200 | Paillier | 加法準同型暗号 | B |
| 2015 | セキュリティ・キャンプ | [Broken RSA](2015/security-camp/broken-rsa/) | ??? | RSA | Multi-prime RSA | C |
| 2015 | TETCON CTF | [The Poodle Attack](2015/tetcon-ctf/the-poodle-attack/) | 200 | AES | Poodle, CBCモード, Padding oracle attack | A |
| 2015 | Trend Micro CTF | [AnswerMe](2015/trend-micro-ctf/answerme/) | ??? | ChaCha | ChaCha, ストリーム暗号, Salsa20 | C |
| 2014 | Hack You | [Hashme](2014/hack-you/Hashme/) | 200 | - | Hash, Merkle-Damgård構造, Length-extension attack | B |
| 2014 | HITCON CTF | [rsaha](2014/hitcon-ctf/rsaha/) | 200 | RSA | Franklin-Reiterrelated-message attack | B |
| 2014 | Plaid CTF | [Parlor](2014/plaid-ctf/parlor/) | 200 | - | MD5, Length-extension attack | S |
| 2013 | SECCON CTF quals | [Cryptanalysis](2013/seccon-ctf-quals/cryptanalysis/) | 300 | 楕円曲線暗号 | 列挙法 | C |
| 2011 | CODEGATE CTF | [Crypto 400](2011/codegate-ctf/crypto-400/) | 400 | AES | CBDモード, Padding oracle attack | B |
| 2015 |  | []() |  |  |  |  |


Problem files are often exported from <https://github.com/ctfs>

#### Updates
- 2017/2/16 Added [PAKE](2016/hitcon-ctf-quals/pake)
- 2016/12/23 Added [LSB Oracle](2016/sharif-ctf/lsb-oracle)
- 2016/12/23 Added [TPQ](2016/sharif-ctf/tpq)
- 2016/12/19 Published "CTF Crypto Writeups by sonickun"
