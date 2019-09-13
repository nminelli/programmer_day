letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shift_values = {
    1: 3,
    2: 3,
    3: 5,
    4: 5,
    5: 7,
    6: 2,
    7: 2,
    8: 4,
    9: 4,
    10: 1,
    11: 6,
    12: 3,
    13: 8,
    14: 5,
    15: 3,
    16: 2
}
letters_with_value = {}

def decrypt():
    decripted_words = []

    for i, l in enumerate(letters):
        letters_with_value.update({i+1: l})

    string_to_decrypt = "wr zepmhexi ymj eqttgev cpuygt dtz mfaj wr jr wr zshzo gpkioc zshzo oguucig zshzo ywqhbelbwvlhkcgy fsi dtz hfs yjqq ymj wjxy ri ymj yjfr ymfy dtz bts ymj gleppirki"
    array = string_to_decrypt.split(' ')
    for word in array:
        new_word = word
        shift_value = shift_values.get(len(word))

        for k, v in letters_with_value.items():
            new_k = k-shift_value
            print("new_k", new_k)
            if new_k == 0:
                new_k = len(letters)
            elif new_k < 0:
                new_k = len(letters) + new_k
            new_l = letters_with_value.get(new_k)
            if word.count(v) > 0:
                new_word = new_word.replace(v, new_l)

        decripted_words.append(new_word)

    print(' '.join(decripted_words))


decrypt()
