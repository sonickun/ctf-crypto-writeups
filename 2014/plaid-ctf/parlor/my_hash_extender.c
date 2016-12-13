// Refered hash_extender: https://github.com/iagox86/hash_extender

#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>
 
unsigned int extend(unsigned int A, unsigned int B, unsigned int C, unsigned int D, char *testhash2) {
    MD5_CTX ctx;
    unsigned char buffer[MD5_DIGEST_LENGTH];
    int i;
 
    MD5_Init(&ctx);
    MD5_Update(&ctx, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", 64);
 
    ctx.A = htonl(A);
    ctx.B = htonl(B);
    ctx.C = htonl(C);
    ctx.D = htonl(D);
 
    MD5_Update(&ctx, "b", 1);
    MD5_Final(buffer, &ctx);
 
    char res[40];
    for (i = 0; i < 16; i++) {
      sprintf(&res[2*i], "%02x", buffer[i]);
    }
    if (!memcmp(res + 16, testhash2 + 16, 8)) {
        return A;
    }
    return 0;
}
 
 
unsigned int brute(unsigned int A, unsigned int B, unsigned int C, unsigned int D, char *testhash2) {
    unsigned int i;
    for (i = 0; i < 1 << 28; i++) {
        A = (A & 0xf) | (i << 4);
 
        if ((i & 0xfffff) == 0)
            printf("%08x\n", i);
 
        unsigned int res = extend(A, B, C, D, testhash2);
        if (res != 0) {
            return res;
        }
    }
    return 0;
}