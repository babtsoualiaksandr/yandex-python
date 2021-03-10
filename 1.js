for (let i=10000; i<99999; i++) {
    setTimeout(() => 
        AES()
            .decrypt(encrypted, i)
            .then((decrypted) => console.log('decrypted', decrypted))
            .cath(_ => console.log('bad key', _)))
}




