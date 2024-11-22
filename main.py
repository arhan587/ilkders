meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict:
    print(word + " kelimesinin anlamı: " + meme_dict[word])
else:
    print("'" + word + "' kelimesini bulamadık.")
